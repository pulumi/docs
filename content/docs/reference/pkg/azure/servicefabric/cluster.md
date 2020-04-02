
---
title: "Cluster"
block_external_search_index: true
---

Manages a Service Fabric Cluster.

> This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/service_fabric_cluster.html.markdown.



## Create a Cluster Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/servicefabric/#Cluster">Cluster</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/servicefabric/#ClusterArgs">ClusterArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Cluster</span><span class="p">(resource_name, opts=None, </span>add_on_features=None<span class="p">, </span>azure_active_directory=None<span class="p">, </span>certificate=None<span class="p">, </span>certificate_common_names=None<span class="p">, </span>client_certificate_common_names=None<span class="p">, </span>client_certificate_thumbprints=None<span class="p">, </span>cluster_code_version=None<span class="p">, </span>diagnostics_config=None<span class="p">, </span>fabric_settings=None<span class="p">, </span>location=None<span class="p">, </span>management_endpoint=None<span class="p">, </span>name=None<span class="p">, </span>node_types=None<span class="p">, </span>reliability_level=None<span class="p">, </span>resource_group_name=None<span class="p">, </span>reverse_proxy_certificate=None<span class="p">, </span>tags=None<span class="p">, </span>upgrade_mode=None<span class="p">, </span>vm_image=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewCluster<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/servicefabric?tab=doc#ClusterArgs">ClusterArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/servicefabric?tab=doc#Cluster">Cluster</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Servicefabric.Cluster.html">Cluster</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.ServiceFabric.ClusterArgs.html">ClusterArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Add<wbr>On<wbr>Features</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A List of one or more features which should be enabled, such as `DnsService`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Azure<wbr>Active<wbr>Directory</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterazureactivedirectory">Cluster<wbr>Azure<wbr>Active<wbr>Directory<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}An `azure_active_directory` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustercertificate">Cluster<wbr>Certificate<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `certificate` block as defined below. Conflicts with `certificate_common_names`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Certificate<wbr>Common<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustercertificatecommonnames">Cluster<wbr>Certificate<wbr>Common<wbr>Names<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `certificate_common_names` block as defined below. Conflicts with `certificate`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Certificate<wbr>Common<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclientcertificatecommonname">List&lt;Cluster<wbr>Client<wbr>Certificate<wbr>Common<wbr>Name<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}A `client_certificate_common_name` block as defined below. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Certificate<wbr>Thumbprints</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclientcertificatethumbprint">List&lt;Cluster<wbr>Client<wbr>Certificate<wbr>Thumbprint<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}One or two `client_certificate_thumbprint` blocks as defined below. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cluster<wbr>Code<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Required if Upgrade Mode set to `Manual`, Specifies the Version of the Cluster Code of the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Diagnostics<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterdiagnosticsconfig">Cluster<wbr>Diagnostics<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `diagnostics_config` block as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fabric<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterfabricsetting">List&lt;Cluster<wbr>Fabric<wbr>Setting<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}One or more `fabric_settings` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the Azure Region where the Service Fabric Cluster should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Management<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Management Endpoint of the cluster such as `http://example.com`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the Service Fabric Cluster. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Node<wbr>Types</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodetype">List&lt;Cluster<wbr>Node<wbr>Type<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}One or more `node_type` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Reliability<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Reliability Level of the Cluster. Possible values include `None`, `Bronze`, `Silver`, `Gold` and `Platinum`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group in which the Service Fabric Cluster exists. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Reverse<wbr>Proxy<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterreverseproxycertificate">Cluster<wbr>Reverse<wbr>Proxy<wbr>Certificate<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `reverse_proxy_certificate` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Upgrade<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Upgrade Mode of the cluster. Possible values are `Automatic` or `Manual`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Vm<wbr>Image</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Image expected for the Service Fabric Cluster, such as `Windows`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Add<wbr>On<wbr>Features</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A List of one or more features which should be enabled, such as `DnsService`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Azure<wbr>Active<wbr>Directory</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterazureactivedirectory">*Cluster<wbr>Azure<wbr>Active<wbr>Directory</a></span>
    </dt>
    <dd>{{% md %}}An `azure_active_directory` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustercertificate">*Cluster<wbr>Certificate</a></span>
    </dt>
    <dd>{{% md %}}A `certificate` block as defined below. Conflicts with `certificate_common_names`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Certificate<wbr>Common<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustercertificatecommonnames">*Cluster<wbr>Certificate<wbr>Common<wbr>Names</a></span>
    </dt>
    <dd>{{% md %}}A `certificate_common_names` block as defined below. Conflicts with `certificate`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Certificate<wbr>Common<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclientcertificatecommonname">[]Cluster<wbr>Client<wbr>Certificate<wbr>Common<wbr>Name</a></span>
    </dt>
    <dd>{{% md %}}A `client_certificate_common_name` block as defined below. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Certificate<wbr>Thumbprints</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclientcertificatethumbprint">[]Cluster<wbr>Client<wbr>Certificate<wbr>Thumbprint</a></span>
    </dt>
    <dd>{{% md %}}One or two `client_certificate_thumbprint` blocks as defined below. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cluster<wbr>Code<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Required if Upgrade Mode set to `Manual`, Specifies the Version of the Cluster Code of the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Diagnostics<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterdiagnosticsconfig">*Cluster<wbr>Diagnostics<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}A `diagnostics_config` block as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fabric<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterfabricsetting">[]Cluster<wbr>Fabric<wbr>Setting</a></span>
    </dt>
    <dd>{{% md %}}One or more `fabric_settings` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the Azure Region where the Service Fabric Cluster should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Management<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Management Endpoint of the cluster such as `http://example.com`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the Service Fabric Cluster. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Node<wbr>Types</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodetype">[]Cluster<wbr>Node<wbr>Type</a></span>
    </dt>
    <dd>{{% md %}}One or more `node_type` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Reliability<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Reliability Level of the Cluster. Possible values include `None`, `Bronze`, `Silver`, `Gold` and `Platinum`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group in which the Service Fabric Cluster exists. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Reverse<wbr>Proxy<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterreverseproxycertificate">*Cluster<wbr>Reverse<wbr>Proxy<wbr>Certificate</a></span>
    </dt>
    <dd>{{% md %}}A `reverse_proxy_certificate` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Upgrade<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Upgrade Mode of the cluster. Possible values are `Automatic` or `Manual`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Vm<wbr>Image</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Image expected for the Service Fabric Cluster, such as `Windows`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>add<wbr>On<wbr>Features</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A List of one or more features which should be enabled, such as `DnsService`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>azure<wbr>Active<wbr>Directory</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterazureactivedirectory">Cluster<wbr>Azure<wbr>Active<wbr>Directory?</a></span>
    </dt>
    <dd>{{% md %}}An `azure_active_directory` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustercertificate">Cluster<wbr>Certificate?</a></span>
    </dt>
    <dd>{{% md %}}A `certificate` block as defined below. Conflicts with `certificate_common_names`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>certificate<wbr>Common<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustercertificatecommonnames">Cluster<wbr>Certificate<wbr>Common<wbr>Names?</a></span>
    </dt>
    <dd>{{% md %}}A `certificate_common_names` block as defined below. Conflicts with `certificate`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>client<wbr>Certificate<wbr>Common<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclientcertificatecommonname">Cluster<wbr>Client<wbr>Certificate<wbr>Common<wbr>Name[]?</a></span>
    </dt>
    <dd>{{% md %}}A `client_certificate_common_name` block as defined below. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>client<wbr>Certificate<wbr>Thumbprints</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclientcertificatethumbprint">Cluster<wbr>Client<wbr>Certificate<wbr>Thumbprint[]?</a></span>
    </dt>
    <dd>{{% md %}}One or two `client_certificate_thumbprint` blocks as defined below. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cluster<wbr>Code<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Required if Upgrade Mode set to `Manual`, Specifies the Version of the Cluster Code of the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>diagnostics<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterdiagnosticsconfig">Cluster<wbr>Diagnostics<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}A `diagnostics_config` block as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fabric<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterfabricsetting">Cluster<wbr>Fabric<wbr>Setting[]?</a></span>
    </dt>
    <dd>{{% md %}}One or more `fabric_settings` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the Azure Region where the Service Fabric Cluster should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>management<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Management Endpoint of the cluster such as `http://example.com`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the Service Fabric Cluster. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>node<wbr>Types</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodetype">Cluster<wbr>Node<wbr>Type[]</a></span>
    </dt>
    <dd>{{% md %}}One or more `node_type` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>reliability<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Reliability Level of the Cluster. Possible values include `None`, `Bronze`, `Silver`, `Gold` and `Platinum`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group in which the Service Fabric Cluster exists. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>reverse<wbr>Proxy<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterreverseproxycertificate">Cluster<wbr>Reverse<wbr>Proxy<wbr>Certificate?</a></span>
    </dt>
    <dd>{{% md %}}A `reverse_proxy_certificate` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>upgrade<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Upgrade Mode of the cluster. Possible values are `Automatic` or `Manual`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>vm<wbr>Image</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Image expected for the Service Fabric Cluster, such as `Windows`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>add_<wbr>on_<wbr>features</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A List of one or more features which should be enabled, such as `DnsService`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>azure_<wbr>active_<wbr>directory</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterazureactivedirectory">Dict[Cluster<wbr>Azure<wbr>Active<wbr>Directory]</a></span>
    </dt>
    <dd>{{% md %}}An `azure_active_directory` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustercertificate">Dict[Cluster<wbr>Certificate]</a></span>
    </dt>
    <dd>{{% md %}}A `certificate` block as defined below. Conflicts with `certificate_common_names`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>certificate_<wbr>common_<wbr>names</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustercertificatecommonnames">Dict[Cluster<wbr>Certificate<wbr>Common<wbr>Names]</a></span>
    </dt>
    <dd>{{% md %}}A `certificate_common_names` block as defined below. Conflicts with `certificate`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>client_<wbr>certificate_<wbr>common_<wbr>names</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclientcertificatecommonname">List[Cluster<wbr>Client<wbr>Certificate<wbr>Common<wbr>Name]</a></span>
    </dt>
    <dd>{{% md %}}A `client_certificate_common_name` block as defined below. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>client_<wbr>certificate_<wbr>thumbprints</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclientcertificatethumbprint">List[Cluster<wbr>Client<wbr>Certificate<wbr>Thumbprint]</a></span>
    </dt>
    <dd>{{% md %}}One or two `client_certificate_thumbprint` blocks as defined below. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cluster_<wbr>code_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Required if Upgrade Mode set to `Manual`, Specifies the Version of the Cluster Code of the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>diagnostics_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterdiagnosticsconfig">Dict[Cluster<wbr>Diagnostics<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}A `diagnostics_config` block as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fabric_<wbr>settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterfabricsetting">List[Cluster<wbr>Fabric<wbr>Setting]</a></span>
    </dt>
    <dd>{{% md %}}One or more `fabric_settings` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the Azure Region where the Service Fabric Cluster should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>management_<wbr>endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the Management Endpoint of the cluster such as `http://example.com`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the Service Fabric Cluster. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>node_<wbr>types</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodetype">List[Cluster<wbr>Node<wbr>Type]</a></span>
    </dt>
    <dd>{{% md %}}One or more `node_type` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>reliability_<wbr>level</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the Reliability Level of the Cluster. Possible values include `None`, `Bronze`, `Silver`, `Gold` and `Platinum`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>resource_<wbr>group_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group in which the Service Fabric Cluster exists. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>reverse_<wbr>proxy_<wbr>certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterreverseproxycertificate">Dict[Cluster<wbr>Reverse<wbr>Proxy<wbr>Certificate]</a></span>
    </dt>
    <dd>{{% md %}}A `reverse_proxy_certificate` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>upgrade_<wbr>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the Upgrade Mode of the cluster. Possible values are `Automatic` or `Manual`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>vm_<wbr>image</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the Image expected for the Service Fabric Cluster, such as `Windows`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## Cluster Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Add<wbr>On<wbr>Features</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A List of one or more features which should be enabled, such as `DnsService`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Azure<wbr>Active<wbr>Directory</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterazureactivedirectory">Cluster<wbr>Azure<wbr>Active<wbr>Directory?</a></span>
    </dt>
    <dd>{{% md %}}An `azure_active_directory` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustercertificate">Cluster<wbr>Certificate?</a></span>
    </dt>
    <dd>{{% md %}}A `certificate` block as defined below. Conflicts with `certificate_common_names`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Certificate<wbr>Common<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustercertificatecommonnames">Cluster<wbr>Certificate<wbr>Common<wbr>Names?</a></span>
    </dt>
    <dd>{{% md %}}A `certificate_common_names` block as defined below. Conflicts with `certificate`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Client<wbr>Certificate<wbr>Common<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclientcertificatecommonname">List&lt;Cluster<wbr>Client<wbr>Certificate<wbr>Common<wbr>Name&gt;?</a></span>
    </dt>
    <dd>{{% md %}}A `client_certificate_common_name` block as defined below. 
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Client<wbr>Certificate<wbr>Thumbprints</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclientcertificatethumbprint">List&lt;Cluster<wbr>Client<wbr>Certificate<wbr>Thumbprint&gt;?</a></span>
    </dt>
    <dd>{{% md %}}One or two `client_certificate_thumbprint` blocks as defined below. 
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Cluster<wbr>Code<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Required if Upgrade Mode set to `Manual`, Specifies the Version of the Cluster Code of the cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Cluster<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Cluster Endpoint for this Service Fabric Cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Diagnostics<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterdiagnosticsconfig">Cluster<wbr>Diagnostics<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}A `diagnostics_config` block as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Fabric<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterfabricsetting">List&lt;Cluster<wbr>Fabric<wbr>Setting&gt;?</a></span>
    </dt>
    <dd>{{% md %}}One or more `fabric_settings` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Azure Region where the Service Fabric Cluster should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Management<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Management Endpoint of the cluster such as `http://example.com`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Service Fabric Cluster. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Node<wbr>Types</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodetype">List&lt;Cluster<wbr>Node<wbr>Type&gt;</a></span>
    </dt>
    <dd>{{% md %}}One or more `node_type` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Reliability<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Reliability Level of the Cluster. Possible values include `None`, `Bronze`, `Silver`, `Gold` and `Platinum`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group in which the Service Fabric Cluster exists. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Reverse<wbr>Proxy<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterreverseproxycertificate">Cluster<wbr>Reverse<wbr>Proxy<wbr>Certificate?</a></span>
    </dt>
    <dd>{{% md %}}A `reverse_proxy_certificate` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Upgrade<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Upgrade Mode of the cluster. Possible values are `Automatic` or `Manual`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vm<wbr>Image</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Image expected for the Service Fabric Cluster, such as `Windows`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Add<wbr>On<wbr>Features</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A List of one or more features which should be enabled, such as `DnsService`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Azure<wbr>Active<wbr>Directory</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterazureactivedirectory">*Cluster<wbr>Azure<wbr>Active<wbr>Directory</a></span>
    </dt>
    <dd>{{% md %}}An `azure_active_directory` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustercertificate">*Cluster<wbr>Certificate</a></span>
    </dt>
    <dd>{{% md %}}A `certificate` block as defined below. Conflicts with `certificate_common_names`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Certificate<wbr>Common<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustercertificatecommonnames">*Cluster<wbr>Certificate<wbr>Common<wbr>Names</a></span>
    </dt>
    <dd>{{% md %}}A `certificate_common_names` block as defined below. Conflicts with `certificate`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Client<wbr>Certificate<wbr>Common<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclientcertificatecommonname">[]Cluster<wbr>Client<wbr>Certificate<wbr>Common<wbr>Name</a></span>
    </dt>
    <dd>{{% md %}}A `client_certificate_common_name` block as defined below. 
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Client<wbr>Certificate<wbr>Thumbprints</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclientcertificatethumbprint">[]Cluster<wbr>Client<wbr>Certificate<wbr>Thumbprint</a></span>
    </dt>
    <dd>{{% md %}}One or two `client_certificate_thumbprint` blocks as defined below. 
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Cluster<wbr>Code<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Required if Upgrade Mode set to `Manual`, Specifies the Version of the Cluster Code of the cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Cluster<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Cluster Endpoint for this Service Fabric Cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Diagnostics<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterdiagnosticsconfig">*Cluster<wbr>Diagnostics<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}A `diagnostics_config` block as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Fabric<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterfabricsetting">[]Cluster<wbr>Fabric<wbr>Setting</a></span>
    </dt>
    <dd>{{% md %}}One or more `fabric_settings` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Azure Region where the Service Fabric Cluster should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Management<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Management Endpoint of the cluster such as `http://example.com`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Service Fabric Cluster. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Node<wbr>Types</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodetype">[]Cluster<wbr>Node<wbr>Type</a></span>
    </dt>
    <dd>{{% md %}}One or more `node_type` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Reliability<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Reliability Level of the Cluster. Possible values include `None`, `Bronze`, `Silver`, `Gold` and `Platinum`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group in which the Service Fabric Cluster exists. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Reverse<wbr>Proxy<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterreverseproxycertificate">*Cluster<wbr>Reverse<wbr>Proxy<wbr>Certificate</a></span>
    </dt>
    <dd>{{% md %}}A `reverse_proxy_certificate` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Upgrade<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Upgrade Mode of the cluster. Possible values are `Automatic` or `Manual`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vm<wbr>Image</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Image expected for the Service Fabric Cluster, such as `Windows`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>add<wbr>On<wbr>Features</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A List of one or more features which should be enabled, such as `DnsService`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>azure<wbr>Active<wbr>Directory</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterazureactivedirectory">Cluster<wbr>Azure<wbr>Active<wbr>Directory?</a></span>
    </dt>
    <dd>{{% md %}}An `azure_active_directory` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustercertificate">Cluster<wbr>Certificate?</a></span>
    </dt>
    <dd>{{% md %}}A `certificate` block as defined below. Conflicts with `certificate_common_names`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>certificate<wbr>Common<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustercertificatecommonnames">Cluster<wbr>Certificate<wbr>Common<wbr>Names?</a></span>
    </dt>
    <dd>{{% md %}}A `certificate_common_names` block as defined below. Conflicts with `certificate`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>client<wbr>Certificate<wbr>Common<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclientcertificatecommonname">Cluster<wbr>Client<wbr>Certificate<wbr>Common<wbr>Name[]?</a></span>
    </dt>
    <dd>{{% md %}}A `client_certificate_common_name` block as defined below. 
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>client<wbr>Certificate<wbr>Thumbprints</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclientcertificatethumbprint">Cluster<wbr>Client<wbr>Certificate<wbr>Thumbprint[]?</a></span>
    </dt>
    <dd>{{% md %}}One or two `client_certificate_thumbprint` blocks as defined below. 
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>cluster<wbr>Code<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Required if Upgrade Mode set to `Manual`, Specifies the Version of the Cluster Code of the cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>cluster<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Cluster Endpoint for this Service Fabric Cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>diagnostics<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterdiagnosticsconfig">Cluster<wbr>Diagnostics<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}A `diagnostics_config` block as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>fabric<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterfabricsetting">Cluster<wbr>Fabric<wbr>Setting[]?</a></span>
    </dt>
    <dd>{{% md %}}One or more `fabric_settings` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Azure Region where the Service Fabric Cluster should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>management<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Management Endpoint of the cluster such as `http://example.com`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Service Fabric Cluster. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>node<wbr>Types</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodetype">Cluster<wbr>Node<wbr>Type[]</a></span>
    </dt>
    <dd>{{% md %}}One or more `node_type` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>reliability<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Reliability Level of the Cluster. Possible values include `None`, `Bronze`, `Silver`, `Gold` and `Platinum`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group in which the Service Fabric Cluster exists. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>reverse<wbr>Proxy<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterreverseproxycertificate">Cluster<wbr>Reverse<wbr>Proxy<wbr>Certificate?</a></span>
    </dt>
    <dd>{{% md %}}A `reverse_proxy_certificate` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>upgrade<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Upgrade Mode of the cluster. Possible values are `Automatic` or `Manual`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vm<wbr>Image</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Image expected for the Service Fabric Cluster, such as `Windows`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>add_<wbr>on_<wbr>features</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A List of one or more features which should be enabled, such as `DnsService`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>azure_<wbr>active_<wbr>directory</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterazureactivedirectory">Dict[Cluster<wbr>Azure<wbr>Active<wbr>Directory]</a></span>
    </dt>
    <dd>{{% md %}}An `azure_active_directory` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustercertificate">Dict[Cluster<wbr>Certificate]</a></span>
    </dt>
    <dd>{{% md %}}A `certificate` block as defined below. Conflicts with `certificate_common_names`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>certificate_<wbr>common_<wbr>names</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustercertificatecommonnames">Dict[Cluster<wbr>Certificate<wbr>Common<wbr>Names]</a></span>
    </dt>
    <dd>{{% md %}}A `certificate_common_names` block as defined below. Conflicts with `certificate`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>client_<wbr>certificate_<wbr>common_<wbr>names</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclientcertificatecommonname">List[Cluster<wbr>Client<wbr>Certificate<wbr>Common<wbr>Name]</a></span>
    </dt>
    <dd>{{% md %}}A `client_certificate_common_name` block as defined below. 
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>client_<wbr>certificate_<wbr>thumbprints</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclientcertificatethumbprint">List[Cluster<wbr>Client<wbr>Certificate<wbr>Thumbprint]</a></span>
    </dt>
    <dd>{{% md %}}One or two `client_certificate_thumbprint` blocks as defined below. 
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>cluster_<wbr>code_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Required if Upgrade Mode set to `Manual`, Specifies the Version of the Cluster Code of the cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>cluster_<wbr>endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Cluster Endpoint for this Service Fabric Cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>diagnostics_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterdiagnosticsconfig">Dict[Cluster<wbr>Diagnostics<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}A `diagnostics_config` block as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>fabric_<wbr>settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterfabricsetting">List[Cluster<wbr>Fabric<wbr>Setting]</a></span>
    </dt>
    <dd>{{% md %}}One or more `fabric_settings` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the Azure Region where the Service Fabric Cluster should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>management_<wbr>endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the Management Endpoint of the cluster such as `http://example.com`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the Service Fabric Cluster. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>node_<wbr>types</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodetype">List[Cluster<wbr>Node<wbr>Type]</a></span>
    </dt>
    <dd>{{% md %}}One or more `node_type` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>reliability_<wbr>level</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the Reliability Level of the Cluster. Possible values include `None`, `Bronze`, `Silver`, `Gold` and `Platinum`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>resource_<wbr>group_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group in which the Service Fabric Cluster exists. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>reverse_<wbr>proxy_<wbr>certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterreverseproxycertificate">Dict[Cluster<wbr>Reverse<wbr>Proxy<wbr>Certificate]</a></span>
    </dt>
    <dd>{{% md %}}A `reverse_proxy_certificate` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>upgrade_<wbr>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the Upgrade Mode of the cluster. Possible values are `Automatic` or `Manual`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vm_<wbr>image</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the Image expected for the Service Fabric Cluster, such as `Windows`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing Cluster Resource

Get an existing Cluster resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/servicefabric/#ClusterState">ClusterState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/servicefabric/#Cluster">Cluster</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>add_on_features=None<span class="p">, </span>azure_active_directory=None<span class="p">, </span>certificate=None<span class="p">, </span>certificate_common_names=None<span class="p">, </span>client_certificate_common_names=None<span class="p">, </span>client_certificate_thumbprints=None<span class="p">, </span>cluster_code_version=None<span class="p">, </span>cluster_endpoint=None<span class="p">, </span>diagnostics_config=None<span class="p">, </span>fabric_settings=None<span class="p">, </span>location=None<span class="p">, </span>management_endpoint=None<span class="p">, </span>name=None<span class="p">, </span>node_types=None<span class="p">, </span>reliability_level=None<span class="p">, </span>resource_group_name=None<span class="p">, </span>reverse_proxy_certificate=None<span class="p">, </span>tags=None<span class="p">, </span>upgrade_mode=None<span class="p">, </span>vm_image=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetCluster<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/servicefabric?tab=doc#ClusterState">ClusterState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/servicefabric?tab=doc#Cluster">Cluster</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Servicefabric.Cluster.html">Cluster</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Servicefabric.ClusterState.html">ClusterState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Add<wbr>On<wbr>Features</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A List of one or more features which should be enabled, such as `DnsService`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Azure<wbr>Active<wbr>Directory</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterazureactivedirectory">Cluster<wbr>Azure<wbr>Active<wbr>Directory<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}An `azure_active_directory` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustercertificate">Cluster<wbr>Certificate<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `certificate` block as defined below. Conflicts with `certificate_common_names`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Certificate<wbr>Common<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustercertificatecommonnames">Cluster<wbr>Certificate<wbr>Common<wbr>Names<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `certificate_common_names` block as defined below. Conflicts with `certificate`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Certificate<wbr>Common<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclientcertificatecommonname">List&lt;Cluster<wbr>Client<wbr>Certificate<wbr>Common<wbr>Name<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}A `client_certificate_common_name` block as defined below. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Certificate<wbr>Thumbprints</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclientcertificatethumbprint">List&lt;Cluster<wbr>Client<wbr>Certificate<wbr>Thumbprint<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}One or two `client_certificate_thumbprint` blocks as defined below. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cluster<wbr>Code<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Required if Upgrade Mode set to `Manual`, Specifies the Version of the Cluster Code of the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cluster<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Cluster Endpoint for this Service Fabric Cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Diagnostics<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterdiagnosticsconfig">Cluster<wbr>Diagnostics<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `diagnostics_config` block as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fabric<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterfabricsetting">List&lt;Cluster<wbr>Fabric<wbr>Setting<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}One or more `fabric_settings` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the Azure Region where the Service Fabric Cluster should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Management<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the Management Endpoint of the cluster such as `http://example.com`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the Service Fabric Cluster. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Types</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodetype">List&lt;Cluster<wbr>Node<wbr>Type<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}One or more `node_type` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Reliability<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the Reliability Level of the Cluster. Possible values include `None`, `Bronze`, `Silver`, `Gold` and `Platinum`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group in which the Service Fabric Cluster exists. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Reverse<wbr>Proxy<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterreverseproxycertificate">Cluster<wbr>Reverse<wbr>Proxy<wbr>Certificate<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `reverse_proxy_certificate` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Upgrade<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the Upgrade Mode of the cluster. Possible values are `Automatic` or `Manual`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vm<wbr>Image</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the Image expected for the Service Fabric Cluster, such as `Windows`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Add<wbr>On<wbr>Features</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A List of one or more features which should be enabled, such as `DnsService`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Azure<wbr>Active<wbr>Directory</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterazureactivedirectory">*Cluster<wbr>Azure<wbr>Active<wbr>Directory</a></span>
    </dt>
    <dd>{{% md %}}An `azure_active_directory` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustercertificate">*Cluster<wbr>Certificate</a></span>
    </dt>
    <dd>{{% md %}}A `certificate` block as defined below. Conflicts with `certificate_common_names`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Certificate<wbr>Common<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustercertificatecommonnames">*Cluster<wbr>Certificate<wbr>Common<wbr>Names</a></span>
    </dt>
    <dd>{{% md %}}A `certificate_common_names` block as defined below. Conflicts with `certificate`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Certificate<wbr>Common<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclientcertificatecommonname">[]Cluster<wbr>Client<wbr>Certificate<wbr>Common<wbr>Name</a></span>
    </dt>
    <dd>{{% md %}}A `client_certificate_common_name` block as defined below. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Certificate<wbr>Thumbprints</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclientcertificatethumbprint">[]Cluster<wbr>Client<wbr>Certificate<wbr>Thumbprint</a></span>
    </dt>
    <dd>{{% md %}}One or two `client_certificate_thumbprint` blocks as defined below. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cluster<wbr>Code<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Required if Upgrade Mode set to `Manual`, Specifies the Version of the Cluster Code of the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cluster<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Cluster Endpoint for this Service Fabric Cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Diagnostics<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterdiagnosticsconfig">*Cluster<wbr>Diagnostics<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}A `diagnostics_config` block as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fabric<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterfabricsetting">[]Cluster<wbr>Fabric<wbr>Setting</a></span>
    </dt>
    <dd>{{% md %}}One or more `fabric_settings` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the Azure Region where the Service Fabric Cluster should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Management<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the Management Endpoint of the cluster such as `http://example.com`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the Service Fabric Cluster. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Types</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodetype">[]Cluster<wbr>Node<wbr>Type</a></span>
    </dt>
    <dd>{{% md %}}One or more `node_type` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Reliability<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the Reliability Level of the Cluster. Possible values include `None`, `Bronze`, `Silver`, `Gold` and `Platinum`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group in which the Service Fabric Cluster exists. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Reverse<wbr>Proxy<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterreverseproxycertificate">*Cluster<wbr>Reverse<wbr>Proxy<wbr>Certificate</a></span>
    </dt>
    <dd>{{% md %}}A `reverse_proxy_certificate` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Upgrade<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the Upgrade Mode of the cluster. Possible values are `Automatic` or `Manual`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vm<wbr>Image</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the Image expected for the Service Fabric Cluster, such as `Windows`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>add<wbr>On<wbr>Features</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A List of one or more features which should be enabled, such as `DnsService`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>azure<wbr>Active<wbr>Directory</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterazureactivedirectory">Cluster<wbr>Azure<wbr>Active<wbr>Directory?</a></span>
    </dt>
    <dd>{{% md %}}An `azure_active_directory` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustercertificate">Cluster<wbr>Certificate?</a></span>
    </dt>
    <dd>{{% md %}}A `certificate` block as defined below. Conflicts with `certificate_common_names`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>certificate<wbr>Common<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustercertificatecommonnames">Cluster<wbr>Certificate<wbr>Common<wbr>Names?</a></span>
    </dt>
    <dd>{{% md %}}A `certificate_common_names` block as defined below. Conflicts with `certificate`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>client<wbr>Certificate<wbr>Common<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclientcertificatecommonname">Cluster<wbr>Client<wbr>Certificate<wbr>Common<wbr>Name[]?</a></span>
    </dt>
    <dd>{{% md %}}A `client_certificate_common_name` block as defined below. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>client<wbr>Certificate<wbr>Thumbprints</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclientcertificatethumbprint">Cluster<wbr>Client<wbr>Certificate<wbr>Thumbprint[]?</a></span>
    </dt>
    <dd>{{% md %}}One or two `client_certificate_thumbprint` blocks as defined below. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cluster<wbr>Code<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Required if Upgrade Mode set to `Manual`, Specifies the Version of the Cluster Code of the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cluster<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Cluster Endpoint for this Service Fabric Cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>diagnostics<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterdiagnosticsconfig">Cluster<wbr>Diagnostics<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}A `diagnostics_config` block as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fabric<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterfabricsetting">Cluster<wbr>Fabric<wbr>Setting[]?</a></span>
    </dt>
    <dd>{{% md %}}One or more `fabric_settings` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the Azure Region where the Service Fabric Cluster should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>management<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the Management Endpoint of the cluster such as `http://example.com`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the Service Fabric Cluster. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node<wbr>Types</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodetype">Cluster<wbr>Node<wbr>Type[]?</a></span>
    </dt>
    <dd>{{% md %}}One or more `node_type` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>reliability<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the Reliability Level of the Cluster. Possible values include `None`, `Bronze`, `Silver`, `Gold` and `Platinum`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group in which the Service Fabric Cluster exists. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>reverse<wbr>Proxy<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterreverseproxycertificate">Cluster<wbr>Reverse<wbr>Proxy<wbr>Certificate?</a></span>
    </dt>
    <dd>{{% md %}}A `reverse_proxy_certificate` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>upgrade<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the Upgrade Mode of the cluster. Possible values are `Automatic` or `Manual`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vm<wbr>Image</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the Image expected for the Service Fabric Cluster, such as `Windows`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>add_<wbr>on_<wbr>features</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A List of one or more features which should be enabled, such as `DnsService`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>azure_<wbr>active_<wbr>directory</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterazureactivedirectory">Dict[Cluster<wbr>Azure<wbr>Active<wbr>Directory]</a></span>
    </dt>
    <dd>{{% md %}}An `azure_active_directory` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustercertificate">Dict[Cluster<wbr>Certificate]</a></span>
    </dt>
    <dd>{{% md %}}A `certificate` block as defined below. Conflicts with `certificate_common_names`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>certificate_<wbr>common_<wbr>names</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustercertificatecommonnames">Dict[Cluster<wbr>Certificate<wbr>Common<wbr>Names]</a></span>
    </dt>
    <dd>{{% md %}}A `certificate_common_names` block as defined below. Conflicts with `certificate`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>client_<wbr>certificate_<wbr>common_<wbr>names</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclientcertificatecommonname">List[Cluster<wbr>Client<wbr>Certificate<wbr>Common<wbr>Name]</a></span>
    </dt>
    <dd>{{% md %}}A `client_certificate_common_name` block as defined below. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>client_<wbr>certificate_<wbr>thumbprints</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclientcertificatethumbprint">List[Cluster<wbr>Client<wbr>Certificate<wbr>Thumbprint]</a></span>
    </dt>
    <dd>{{% md %}}One or two `client_certificate_thumbprint` blocks as defined below. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cluster_<wbr>code_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Required if Upgrade Mode set to `Manual`, Specifies the Version of the Cluster Code of the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cluster_<wbr>endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Cluster Endpoint for this Service Fabric Cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>diagnostics_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterdiagnosticsconfig">Dict[Cluster<wbr>Diagnostics<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}A `diagnostics_config` block as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fabric_<wbr>settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterfabricsetting">List[Cluster<wbr>Fabric<wbr>Setting]</a></span>
    </dt>
    <dd>{{% md %}}One or more `fabric_settings` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the Azure Region where the Service Fabric Cluster should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>management_<wbr>endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the Management Endpoint of the cluster such as `http://example.com`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the Service Fabric Cluster. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node_<wbr>types</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodetype">List[Cluster<wbr>Node<wbr>Type]</a></span>
    </dt>
    <dd>{{% md %}}One or more `node_type` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>reliability_<wbr>level</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the Reliability Level of the Cluster. Possible values include `None`, `Bronze`, `Silver`, `Gold` and `Platinum`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource_<wbr>group_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group in which the Service Fabric Cluster exists. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>reverse_<wbr>proxy_<wbr>certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterreverseproxycertificate">Dict[Cluster<wbr>Reverse<wbr>Proxy<wbr>Certificate]</a></span>
    </dt>
    <dd>{{% md %}}A `reverse_proxy_certificate` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>upgrade_<wbr>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the Upgrade Mode of the cluster. Possible values are `Automatic` or `Manual`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vm_<wbr>image</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the Image expected for the Service Fabric Cluster, such as `Windows`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Cluster<wbr>Azure<wbr>Active<wbr>Directory</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#ClusterAzureActiveDirectory">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#ClusterAzureActiveDirectory">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/servicefabric?tab=doc#ClusterAzureActiveDirectoryArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/servicefabric?tab=doc#ClusterAzureActiveDirectoryOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Client<wbr>Application<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Azure Active Directory Client ID which should be used for the Client Application.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Cluster<wbr>Application<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Azure Active Directory Cluster Application ID.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Azure Active Directory Tenant ID.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Client<wbr>Application<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Azure Active Directory Client ID which should be used for the Client Application.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Cluster<wbr>Application<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Azure Active Directory Cluster Application ID.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Azure Active Directory Tenant ID.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>client<wbr>Application<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Azure Active Directory Client ID which should be used for the Client Application.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>cluster<wbr>Application<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Azure Active Directory Cluster Application ID.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Azure Active Directory Tenant ID.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>client<wbr>Application<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Azure Active Directory Client ID which should be used for the Client Application.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>cluster<wbr>Application<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Azure Active Directory Cluster Application ID.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>tenant_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Azure Active Directory Tenant ID.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Certificate</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#ClusterCertificate">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#ClusterCertificate">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/servicefabric?tab=doc#ClusterCertificateArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/servicefabric?tab=doc#ClusterCertificateOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Thumbprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Thumbprint of the Certificate.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Thumbprint<wbr>Secondary</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Secondary Thumbprint of the Certificate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>X509Store<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The X509 Store where the Certificate Exists, such as `My`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Thumbprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Thumbprint of the Certificate.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Thumbprint<wbr>Secondary</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Secondary Thumbprint of the Certificate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>X509Store<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The X509 Store where the Certificate Exists, such as `My`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>thumbprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Thumbprint of the Certificate.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>thumbprint<wbr>Secondary</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Secondary Thumbprint of the Certificate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>x509Store<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The X509 Store where the Certificate Exists, such as `My`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>thumbprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Thumbprint of the Certificate.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>thumbprint<wbr>Secondary</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Secondary Thumbprint of the Certificate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>x509Store<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The X509 Store where the Certificate Exists, such as `My`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Certificate<wbr>Common<wbr>Names</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#ClusterCertificateCommonNames">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#ClusterCertificateCommonNames">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/servicefabric?tab=doc#ClusterCertificateCommonNamesArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/servicefabric?tab=doc#ClusterCertificateCommonNamesOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Common<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustercertificatecommonnamescommonname">List&lt;Cluster<wbr>Certificate<wbr>Common<wbr>Names<wbr>Common<wbr>Name<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}A `common_names` block as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>X509Store<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The X509 Store where the Certificate Exists, such as `My`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Common<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustercertificatecommonnamescommonname">[]Cluster<wbr>Certificate<wbr>Common<wbr>Names<wbr>Common<wbr>Name</a></span>
    </dt>
    <dd>{{% md %}}A `common_names` block as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>X509Store<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The X509 Store where the Certificate Exists, such as `My`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>common<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustercertificatecommonnamescommonname">Cluster<wbr>Certificate<wbr>Common<wbr>Names<wbr>Common<wbr>Name[]</a></span>
    </dt>
    <dd>{{% md %}}A `common_names` block as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>x509Store<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The X509 Store where the Certificate Exists, such as `My`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>common<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustercertificatecommonnamescommonname">List[Cluster<wbr>Certificate<wbr>Common<wbr>Names<wbr>Common<wbr>Name]</a></span>
    </dt>
    <dd>{{% md %}}A `common_names` block as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>x509Store<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The X509 Store where the Certificate Exists, such as `My`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Certificate<wbr>Common<wbr>Names<wbr>Common<wbr>Name</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#ClusterCertificateCommonNamesCommonName">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#ClusterCertificateCommonNamesCommonName">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/servicefabric?tab=doc#ClusterCertificateCommonNamesCommonNameArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/servicefabric?tab=doc#ClusterCertificateCommonNamesCommonNameOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Certificate<wbr>Common<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The common or subject name of the certificate.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Certificate<wbr>Issuer<wbr>Thumbprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Issuer Thumbprint of the Certificate.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Certificate<wbr>Common<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The common or subject name of the certificate.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Certificate<wbr>Issuer<wbr>Thumbprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Issuer Thumbprint of the Certificate.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>certificate<wbr>Common<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The common or subject name of the certificate.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>certificate<wbr>Issuer<wbr>Thumbprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Issuer Thumbprint of the Certificate.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>certificate<wbr>Common<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The common or subject name of the certificate.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>certificate<wbr>Issuer<wbr>Thumbprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Issuer Thumbprint of the Certificate.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Client<wbr>Certificate<wbr>Common<wbr>Name</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#ClusterClientCertificateCommonName">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#ClusterClientCertificateCommonName">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/servicefabric?tab=doc#ClusterClientCertificateCommonNameArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/servicefabric?tab=doc#ClusterClientCertificateCommonNameOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Common<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Is<wbr>Admin</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Does the Client Certificate have Admin Access to the cluster? Non-admin clients can only perform read only operations on the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Issuer<wbr>Thumbprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Common<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Is<wbr>Admin</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Does the Client Certificate have Admin Access to the cluster? Non-admin clients can only perform read only operations on the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Issuer<wbr>Thumbprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>common<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>is<wbr>Admin</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Does the Client Certificate have Admin Access to the cluster? Non-admin clients can only perform read only operations on the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>issuer<wbr>Thumbprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>common<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>is<wbr>Admin</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Does the Client Certificate have Admin Access to the cluster? Non-admin clients can only perform read only operations on the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>issuer<wbr>Thumbprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Client<wbr>Certificate<wbr>Thumbprint</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#ClusterClientCertificateThumbprint">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#ClusterClientCertificateThumbprint">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/servicefabric?tab=doc#ClusterClientCertificateThumbprintArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/servicefabric?tab=doc#ClusterClientCertificateThumbprintOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Is<wbr>Admin</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Does the Client Certificate have Admin Access to the cluster? Non-admin clients can only perform read only operations on the cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Thumbprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Thumbprint associated with the Client Certificate.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Is<wbr>Admin</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Does the Client Certificate have Admin Access to the cluster? Non-admin clients can only perform read only operations on the cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Thumbprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Thumbprint associated with the Client Certificate.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>is<wbr>Admin</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Does the Client Certificate have Admin Access to the cluster? Non-admin clients can only perform read only operations on the cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>thumbprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Thumbprint associated with the Client Certificate.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>is<wbr>Admin</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Does the Client Certificate have Admin Access to the cluster? Non-admin clients can only perform read only operations on the cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>thumbprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Thumbprint associated with the Client Certificate.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Diagnostics<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#ClusterDiagnosticsConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#ClusterDiagnosticsConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/servicefabric?tab=doc#ClusterDiagnosticsConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/servicefabric?tab=doc#ClusterDiagnosticsConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Blob<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Blob Endpoint of the Storage Account.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Protected<wbr>Account<wbr>Key<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The protected diagnostics storage key name, such as `StorageAccountKey1`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Queue<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Queue Endpoint of the Storage Account.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Storage<wbr>Account<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Storage Account where the Diagnostics should be sent to.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Table<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Table Endpoint of the Storage Account.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Blob<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Blob Endpoint of the Storage Account.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Protected<wbr>Account<wbr>Key<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The protected diagnostics storage key name, such as `StorageAccountKey1`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Queue<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Queue Endpoint of the Storage Account.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Storage<wbr>Account<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Storage Account where the Diagnostics should be sent to.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Table<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Table Endpoint of the Storage Account.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>blob<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Blob Endpoint of the Storage Account.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>protected<wbr>Account<wbr>Key<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The protected diagnostics storage key name, such as `StorageAccountKey1`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>queue<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Queue Endpoint of the Storage Account.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>storage<wbr>Account<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Storage Account where the Diagnostics should be sent to.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>table<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Table Endpoint of the Storage Account.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>blob<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Blob Endpoint of the Storage Account.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>protected<wbr>Account<wbr>Key<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The protected diagnostics storage key name, such as `StorageAccountKey1`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>queue<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Queue Endpoint of the Storage Account.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>storage_<wbr>account_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the Storage Account where the Diagnostics should be sent to.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>table<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Table Endpoint of the Storage Account.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Fabric<wbr>Setting</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#ClusterFabricSetting">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#ClusterFabricSetting">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/servicefabric?tab=doc#ClusterFabricSettingArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/servicefabric?tab=doc#ClusterFabricSettingOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Fabric Setting, such as `Security` or `Federation`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Parameters</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}A map containing settings for the specified Fabric Setting.
{{% /md %}}</dd>

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
    <dd>{{% md %}}The name of the Fabric Setting, such as `Security` or `Federation`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Parameters</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A map containing settings for the specified Fabric Setting.
{{% /md %}}</dd>

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
    <dd>{{% md %}}The name of the Fabric Setting, such as `Security` or `Federation`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>parameters</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}A map containing settings for the specified Fabric Setting.
{{% /md %}}</dd>

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
    <dd>{{% md %}}The name of the Fabric Setting, such as `Security` or `Federation`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>parameters</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A map containing settings for the specified Fabric Setting.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Node<wbr>Type</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#ClusterNodeType">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#ClusterNodeType">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/servicefabric?tab=doc#ClusterNodeTypeArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/servicefabric?tab=doc#ClusterNodeTypeOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Application<wbr>Ports</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodetypeapplicationports">Cluster<wbr>Node<wbr>Type<wbr>Application<wbr>Ports<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `application_ports` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Capacities</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}The capacity tags applied to the nodes in the node type, the cluster resource manager uses these tags to understand how much resource a node has.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Client<wbr>Endpoint<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The Port used for the Client Endpoint for this Node Type. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Durability<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Durability Level for this Node Type. Possible values include `Bronze`, `Gold` and `Silver`. Defaults to `Bronze`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ephemeral<wbr>Ports</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodetypeephemeralports">Cluster<wbr>Node<wbr>Type<wbr>Ephemeral<wbr>Ports<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `ephemeral_ports` block as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Http<wbr>Endpoint<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The Port used for the HTTP Endpoint for this Node Type. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Instance<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The number of nodes for this Node Type.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Is<wbr>Primary</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Is this the Primary Node Type? Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Node Type. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Placement<wbr>Properties</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}The placement tags applied to nodes in the node type, which can be used to indicate where certain services (workload) should run.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Reverse<wbr>Proxy<wbr>Endpoint<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The Port used for the Reverse Proxy Endpoint  for this Node Type. Changing this will upgrade the cluster.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Application<wbr>Ports</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodetypeapplicationports">*Cluster<wbr>Node<wbr>Type<wbr>Application<wbr>Ports</a></span>
    </dt>
    <dd>{{% md %}}A `application_ports` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Capacities</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}The capacity tags applied to the nodes in the node type, the cluster resource manager uses these tags to understand how much resource a node has.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Client<wbr>Endpoint<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The Port used for the Client Endpoint for this Node Type. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Durability<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Durability Level for this Node Type. Possible values include `Bronze`, `Gold` and `Silver`. Defaults to `Bronze`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ephemeral<wbr>Ports</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodetypeephemeralports">*Cluster<wbr>Node<wbr>Type<wbr>Ephemeral<wbr>Ports</a></span>
    </dt>
    <dd>{{% md %}}A `ephemeral_ports` block as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Http<wbr>Endpoint<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The Port used for the HTTP Endpoint for this Node Type. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Instance<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The number of nodes for this Node Type.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Is<wbr>Primary</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Is this the Primary Node Type? Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Node Type. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Placement<wbr>Properties</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}The placement tags applied to nodes in the node type, which can be used to indicate where certain services (workload) should run.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Reverse<wbr>Proxy<wbr>Endpoint<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The Port used for the Reverse Proxy Endpoint  for this Node Type. Changing this will upgrade the cluster.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>application<wbr>Ports</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodetypeapplicationports">Cluster<wbr>Node<wbr>Type<wbr>Application<wbr>Ports?</a></span>
    </dt>
    <dd>{{% md %}}A `application_ports` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>capacities</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}The capacity tags applied to the nodes in the node type, the cluster resource manager uses these tags to understand how much resource a node has.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>client<wbr>Endpoint<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The Port used for the Client Endpoint for this Node Type. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>durability<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Durability Level for this Node Type. Possible values include `Bronze`, `Gold` and `Silver`. Defaults to `Bronze`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ephemeral<wbr>Ports</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodetypeephemeralports">Cluster<wbr>Node<wbr>Type<wbr>Ephemeral<wbr>Ports?</a></span>
    </dt>
    <dd>{{% md %}}A `ephemeral_ports` block as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>http<wbr>Endpoint<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The Port used for the HTTP Endpoint for this Node Type. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>instance<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The number of nodes for this Node Type.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>is<wbr>Primary</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Is this the Primary Node Type? Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Node Type. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>placement<wbr>Properties</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}The placement tags applied to nodes in the node type, which can be used to indicate where certain services (workload) should run.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>reverse<wbr>Proxy<wbr>Endpoint<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The Port used for the Reverse Proxy Endpoint  for this Node Type. Changing this will upgrade the cluster.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>application<wbr>Ports</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodetypeapplicationports">Dict[Cluster<wbr>Node<wbr>Type<wbr>Application<wbr>Ports]</a></span>
    </dt>
    <dd>{{% md %}}A `application_ports` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>capacities</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}The capacity tags applied to the nodes in the node type, the cluster resource manager uses these tags to understand how much resource a node has.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>client<wbr>Endpoint<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The Port used for the Client Endpoint for this Node Type. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>durability<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Durability Level for this Node Type. Possible values include `Bronze`, `Gold` and `Silver`. Defaults to `Bronze`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ephemeral<wbr>Ports</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodetypeephemeralports">Dict[Cluster<wbr>Node<wbr>Type<wbr>Ephemeral<wbr>Ports]</a></span>
    </dt>
    <dd>{{% md %}}A `ephemeral_ports` block as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>http<wbr>Endpoint<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The Port used for the HTTP Endpoint for this Node Type. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>instance<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The number of nodes for this Node Type.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>is<wbr>Primary</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Is this the Primary Node Type? Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the Node Type. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>placement<wbr>Properties</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}The placement tags applied to nodes in the node type, which can be used to indicate where certain services (workload) should run.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>reverse<wbr>Proxy<wbr>Endpoint<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The Port used for the Reverse Proxy Endpoint  for this Node Type. Changing this will upgrade the cluster.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Node<wbr>Type<wbr>Application<wbr>Ports</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#ClusterNodeTypeApplicationPorts">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#ClusterNodeTypeApplicationPorts">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/servicefabric?tab=doc#ClusterNodeTypeApplicationPortsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/servicefabric?tab=doc#ClusterNodeTypeApplicationPortsOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>End<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The end of the Application Port Range on this Node Type.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Start<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The start of the Application Port Range on this Node Type.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>End<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The end of the Application Port Range on this Node Type.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Start<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The start of the Application Port Range on this Node Type.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>end<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The end of the Application Port Range on this Node Type.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>start<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The start of the Application Port Range on this Node Type.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>end<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The end of the Application Port Range on this Node Type.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>start<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The start of the Application Port Range on this Node Type.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Node<wbr>Type<wbr>Ephemeral<wbr>Ports</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#ClusterNodeTypeEphemeralPorts">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#ClusterNodeTypeEphemeralPorts">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/servicefabric?tab=doc#ClusterNodeTypeEphemeralPortsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/servicefabric?tab=doc#ClusterNodeTypeEphemeralPortsOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>End<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The end of the Ephemeral Port Range on this Node Type.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Start<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The start of the Ephemeral Port Range on this Node Type.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>End<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The end of the Ephemeral Port Range on this Node Type.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Start<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The start of the Ephemeral Port Range on this Node Type.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>end<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The end of the Ephemeral Port Range on this Node Type.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>start<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The start of the Ephemeral Port Range on this Node Type.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>end<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The end of the Ephemeral Port Range on this Node Type.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>start<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The start of the Ephemeral Port Range on this Node Type.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Reverse<wbr>Proxy<wbr>Certificate</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#ClusterReverseProxyCertificate">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#ClusterReverseProxyCertificate">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/servicefabric?tab=doc#ClusterReverseProxyCertificateArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/servicefabric?tab=doc#ClusterReverseProxyCertificateOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Thumbprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Thumbprint of the Certificate.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Thumbprint<wbr>Secondary</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Secondary Thumbprint of the Certificate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>X509Store<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The X509 Store where the Certificate Exists, such as `My`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Thumbprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Thumbprint of the Certificate.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Thumbprint<wbr>Secondary</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Secondary Thumbprint of the Certificate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>X509Store<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The X509 Store where the Certificate Exists, such as `My`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>thumbprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Thumbprint of the Certificate.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>thumbprint<wbr>Secondary</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Secondary Thumbprint of the Certificate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>x509Store<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The X509 Store where the Certificate Exists, such as `My`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>thumbprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Thumbprint of the Certificate.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>thumbprint<wbr>Secondary</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Secondary Thumbprint of the Certificate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>x509Store<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The X509 Store where the Certificate Exists, such as `My`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-azure">https://github.com/pulumi/pulumi-azure</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd></dl>
