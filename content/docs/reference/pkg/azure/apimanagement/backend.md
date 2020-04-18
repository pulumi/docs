
---
title: "Backend"
block_external_search_index: true
---



Manages a backend within an API Management Service.

> This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/api_management_backend.html.markdown.



## Create a Backend Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/apimanagement/#Backend">Backend</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/apimanagement/#BackendArgs">BackendArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Backend</span><span class="p">(resource_name, opts=None, </span>api_management_name=None<span class="p">, </span>credentials=None<span class="p">, </span>description=None<span class="p">, </span>name=None<span class="p">, </span>protocol=None<span class="p">, </span>proxy=None<span class="p">, </span>resource_group_name=None<span class="p">, </span>resource_id=None<span class="p">, </span>service_fabric_cluster=None<span class="p">, </span>title=None<span class="p">, </span>tls=None<span class="p">, </span>url=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewBackend<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/apimanagement?tab=doc#BackendArgs">BackendArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/apimanagement?tab=doc#Backend">Backend</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Apimanagement.Backend.html">Backend</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.ApiManagement.BackendArgs.html">BackendArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Api<wbr>Management<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Name of the API Management Service where this backend should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Credentials</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendcredentials">Backend<wbr>Credentials<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `credentials` block as documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The description of the backend.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the API Management backend. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The protocol used by the backend host. Possible values are `http` or `soap`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Proxy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendproxy">Backend<wbr>Proxy<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `proxy` block as documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The management URI of the backend host in an external system. This URI can be the ARM Resource ID of Logic Apps, Function Apps or API Apps, or the management endpoint of a Service Fabric cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Service<wbr>Fabric<wbr>Cluster</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicefabriccluster">Backend<wbr>Service<wbr>Fabric<wbr>Cluster<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `service_fabric_cluster` block as documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Title</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The title of the backend.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tls</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendtls">Backend<wbr>Tls<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `tls` block as documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The URL of the backend host.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Api<wbr>Management<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Name of the API Management Service where this backend should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Credentials</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendcredentials">*Backend<wbr>Credentials</a></span>
    </dt>
    <dd>{{% md %}}A `credentials` block as documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The description of the backend.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the API Management backend. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The protocol used by the backend host. Possible values are `http` or `soap`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Proxy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendproxy">*Backend<wbr>Proxy</a></span>
    </dt>
    <dd>{{% md %}}A `proxy` block as documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The management URI of the backend host in an external system. This URI can be the ARM Resource ID of Logic Apps, Function Apps or API Apps, or the management endpoint of a Service Fabric cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Service<wbr>Fabric<wbr>Cluster</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicefabriccluster">*Backend<wbr>Service<wbr>Fabric<wbr>Cluster</a></span>
    </dt>
    <dd>{{% md %}}A `service_fabric_cluster` block as documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Title</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The title of the backend.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tls</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendtls">*Backend<wbr>Tls</a></span>
    </dt>
    <dd>{{% md %}}A `tls` block as documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The URL of the backend host.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>api<wbr>Management<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Name of the API Management Service where this backend should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>credentials</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendcredentials">Backend<wbr>Credentials?</a></span>
    </dt>
    <dd>{{% md %}}A `credentials` block as documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The description of the backend.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the API Management backend. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The protocol used by the backend host. Possible values are `http` or `soap`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>proxy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendproxy">Backend<wbr>Proxy?</a></span>
    </dt>
    <dd>{{% md %}}A `proxy` block as documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The management URI of the backend host in an external system. This URI can be the ARM Resource ID of Logic Apps, Function Apps or API Apps, or the management endpoint of a Service Fabric cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>service<wbr>Fabric<wbr>Cluster</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicefabriccluster">Backend<wbr>Service<wbr>Fabric<wbr>Cluster?</a></span>
    </dt>
    <dd>{{% md %}}A `service_fabric_cluster` block as documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>title</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The title of the backend.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tls</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendtls">Backend<wbr>Tls?</a></span>
    </dt>
    <dd>{{% md %}}A `tls` block as documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The URL of the backend host.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>api_<wbr>management_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Name of the API Management Service where this backend should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>credentials</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendcredentials">Dict[Backend<wbr>Credentials]</a></span>
    </dt>
    <dd>{{% md %}}A `credentials` block as documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The description of the backend.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the API Management backend. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The protocol used by the backend host. Possible values are `http` or `soap`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>proxy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendproxy">Dict[Backend<wbr>Proxy]</a></span>
    </dt>
    <dd>{{% md %}}A `proxy` block as documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>resource_<wbr>group_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The management URI of the backend host in an external system. This URI can be the ARM Resource ID of Logic Apps, Function Apps or API Apps, or the management endpoint of a Service Fabric cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>service_<wbr>fabric_<wbr>cluster</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicefabriccluster">Dict[Backend<wbr>Service<wbr>Fabric<wbr>Cluster]</a></span>
    </dt>
    <dd>{{% md %}}A `service_fabric_cluster` block as documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>title</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The title of the backend.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tls</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendtls">Dict[Backend<wbr>Tls]</a></span>
    </dt>
    <dd>{{% md %}}A `tls` block as documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>url</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The URL of the backend host.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## Backend Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Api<wbr>Management<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Name of the API Management Service where this backend should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Credentials</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendcredentials">Backend<wbr>Credentials?</a></span>
    </dt>
    <dd>{{% md %}}A `credentials` block as documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The description of the backend.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the API Management backend. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The protocol used by the backend host. Possible values are `http` or `soap`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Proxy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendproxy">Backend<wbr>Proxy?</a></span>
    </dt>
    <dd>{{% md %}}A `proxy` block as documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Resource<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The management URI of the backend host in an external system. This URI can be the ARM Resource ID of Logic Apps, Function Apps or API Apps, or the management endpoint of a Service Fabric cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Service<wbr>Fabric<wbr>Cluster</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicefabriccluster">Backend<wbr>Service<wbr>Fabric<wbr>Cluster?</a></span>
    </dt>
    <dd>{{% md %}}A `service_fabric_cluster` block as documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Title</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The title of the backend.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tls</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendtls">Backend<wbr>Tls?</a></span>
    </dt>
    <dd>{{% md %}}A `tls` block as documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The URL of the backend host.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Api<wbr>Management<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Name of the API Management Service where this backend should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Credentials</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendcredentials">*Backend<wbr>Credentials</a></span>
    </dt>
    <dd>{{% md %}}A `credentials` block as documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The description of the backend.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the API Management backend. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The protocol used by the backend host. Possible values are `http` or `soap`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Proxy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendproxy">*Backend<wbr>Proxy</a></span>
    </dt>
    <dd>{{% md %}}A `proxy` block as documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Resource<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The management URI of the backend host in an external system. This URI can be the ARM Resource ID of Logic Apps, Function Apps or API Apps, or the management endpoint of a Service Fabric cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Service<wbr>Fabric<wbr>Cluster</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicefabriccluster">*Backend<wbr>Service<wbr>Fabric<wbr>Cluster</a></span>
    </dt>
    <dd>{{% md %}}A `service_fabric_cluster` block as documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Title</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The title of the backend.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tls</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendtls">*Backend<wbr>Tls</a></span>
    </dt>
    <dd>{{% md %}}A `tls` block as documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The URL of the backend host.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>api<wbr>Management<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Name of the API Management Service where this backend should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>credentials</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendcredentials">Backend<wbr>Credentials?</a></span>
    </dt>
    <dd>{{% md %}}A `credentials` block as documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The description of the backend.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the API Management backend. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The protocol used by the backend host. Possible values are `http` or `soap`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>proxy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendproxy">Backend<wbr>Proxy?</a></span>
    </dt>
    <dd>{{% md %}}A `proxy` block as documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>resource<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The management URI of the backend host in an external system. This URI can be the ARM Resource ID of Logic Apps, Function Apps or API Apps, or the management endpoint of a Service Fabric cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>service<wbr>Fabric<wbr>Cluster</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicefabriccluster">Backend<wbr>Service<wbr>Fabric<wbr>Cluster?</a></span>
    </dt>
    <dd>{{% md %}}A `service_fabric_cluster` block as documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>title</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The title of the backend.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tls</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendtls">Backend<wbr>Tls?</a></span>
    </dt>
    <dd>{{% md %}}A `tls` block as documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The URL of the backend host.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>api_<wbr>management_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Name of the API Management Service where this backend should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>credentials</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendcredentials">Dict[Backend<wbr>Credentials]</a></span>
    </dt>
    <dd>{{% md %}}A `credentials` block as documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The description of the backend.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the API Management backend. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The protocol used by the backend host. Possible values are `http` or `soap`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>proxy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendproxy">Dict[Backend<wbr>Proxy]</a></span>
    </dt>
    <dd>{{% md %}}A `proxy` block as documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>resource_<wbr>group_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>resource_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The management URI of the backend host in an external system. This URI can be the ARM Resource ID of Logic Apps, Function Apps or API Apps, or the management endpoint of a Service Fabric cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>service_<wbr>fabric_<wbr>cluster</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicefabriccluster">Dict[Backend<wbr>Service<wbr>Fabric<wbr>Cluster]</a></span>
    </dt>
    <dd>{{% md %}}A `service_fabric_cluster` block as documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>title</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The title of the backend.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tls</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendtls">Dict[Backend<wbr>Tls]</a></span>
    </dt>
    <dd>{{% md %}}A `tls` block as documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>url</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The URL of the backend host.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing Backend Resource

Get an existing Backend resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/apimanagement/#BackendState">BackendState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/apimanagement/#Backend">Backend</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>api_management_name=None<span class="p">, </span>credentials=None<span class="p">, </span>description=None<span class="p">, </span>name=None<span class="p">, </span>protocol=None<span class="p">, </span>proxy=None<span class="p">, </span>resource_group_name=None<span class="p">, </span>resource_id=None<span class="p">, </span>service_fabric_cluster=None<span class="p">, </span>title=None<span class="p">, </span>tls=None<span class="p">, </span>url=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetBackend<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/apimanagement?tab=doc#BackendState">BackendState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/apimanagement?tab=doc#Backend">Backend</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Apimanagement.Backend.html">Backend</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Apimanagement.BackendState.html">BackendState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Api<wbr>Management<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Name of the API Management Service where this backend should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Credentials</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendcredentials">Backend<wbr>Credentials<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `credentials` block as documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The description of the backend.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the API Management backend. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The protocol used by the backend host. Possible values are `http` or `soap`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Proxy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendproxy">Backend<wbr>Proxy<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `proxy` block as documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The management URI of the backend host in an external system. This URI can be the ARM Resource ID of Logic Apps, Function Apps or API Apps, or the management endpoint of a Service Fabric cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Service<wbr>Fabric<wbr>Cluster</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicefabriccluster">Backend<wbr>Service<wbr>Fabric<wbr>Cluster<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `service_fabric_cluster` block as documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Title</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The title of the backend.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tls</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendtls">Backend<wbr>Tls<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `tls` block as documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The URL of the backend host.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Api<wbr>Management<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Name of the API Management Service where this backend should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Credentials</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendcredentials">*Backend<wbr>Credentials</a></span>
    </dt>
    <dd>{{% md %}}A `credentials` block as documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The description of the backend.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the API Management backend. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The protocol used by the backend host. Possible values are `http` or `soap`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Proxy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendproxy">*Backend<wbr>Proxy</a></span>
    </dt>
    <dd>{{% md %}}A `proxy` block as documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The management URI of the backend host in an external system. This URI can be the ARM Resource ID of Logic Apps, Function Apps or API Apps, or the management endpoint of a Service Fabric cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Service<wbr>Fabric<wbr>Cluster</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicefabriccluster">*Backend<wbr>Service<wbr>Fabric<wbr>Cluster</a></span>
    </dt>
    <dd>{{% md %}}A `service_fabric_cluster` block as documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Title</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The title of the backend.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tls</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendtls">*Backend<wbr>Tls</a></span>
    </dt>
    <dd>{{% md %}}A `tls` block as documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The URL of the backend host.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>api<wbr>Management<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Name of the API Management Service where this backend should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>credentials</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendcredentials">Backend<wbr>Credentials?</a></span>
    </dt>
    <dd>{{% md %}}A `credentials` block as documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The description of the backend.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the API Management backend. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The protocol used by the backend host. Possible values are `http` or `soap`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>proxy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendproxy">Backend<wbr>Proxy?</a></span>
    </dt>
    <dd>{{% md %}}A `proxy` block as documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The management URI of the backend host in an external system. This URI can be the ARM Resource ID of Logic Apps, Function Apps or API Apps, or the management endpoint of a Service Fabric cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>service<wbr>Fabric<wbr>Cluster</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicefabriccluster">Backend<wbr>Service<wbr>Fabric<wbr>Cluster?</a></span>
    </dt>
    <dd>{{% md %}}A `service_fabric_cluster` block as documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>title</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The title of the backend.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tls</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendtls">Backend<wbr>Tls?</a></span>
    </dt>
    <dd>{{% md %}}A `tls` block as documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The URL of the backend host.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>api_<wbr>management_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Name of the API Management Service where this backend should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>credentials</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendcredentials">Dict[Backend<wbr>Credentials]</a></span>
    </dt>
    <dd>{{% md %}}A `credentials` block as documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The description of the backend.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the API Management backend. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The protocol used by the backend host. Possible values are `http` or `soap`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>proxy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendproxy">Dict[Backend<wbr>Proxy]</a></span>
    </dt>
    <dd>{{% md %}}A `proxy` block as documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource_<wbr>group_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The management URI of the backend host in an external system. This URI can be the ARM Resource ID of Logic Apps, Function Apps or API Apps, or the management endpoint of a Service Fabric cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>service_<wbr>fabric_<wbr>cluster</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicefabriccluster">Dict[Backend<wbr>Service<wbr>Fabric<wbr>Cluster]</a></span>
    </dt>
    <dd>{{% md %}}A `service_fabric_cluster` block as documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>title</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The title of the backend.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tls</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendtls">Dict[Backend<wbr>Tls]</a></span>
    </dt>
    <dd>{{% md %}}A `tls` block as documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>url</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The URL of the backend host.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Backend<wbr>Credentials</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#BackendCredentials">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#BackendCredentials">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/apimanagement?tab=doc#BackendCredentialsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/apimanagement?tab=doc#BackendCredentialsOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Authorization</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendcredentialsauthorization">Backend<wbr>Credentials<wbr>Authorization<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}An `authorization` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Certificates</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of client certificate thumbprints to present to the backend host. The certificates must exist within the API Management Service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Header</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}A mapping of header parameters to pass to the backend host. The keys are the header names and the values are a comma separated string of header values. This is converted to a list before being passed to the API.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Query</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}A mapping of query parameters to pass to the backend host. The keys are the query names and the values are a comma separated string of query values. This is converted to a list before being passed to the API.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Authorization</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendcredentialsauthorization">*Backend<wbr>Credentials<wbr>Authorization</a></span>
    </dt>
    <dd>{{% md %}}An `authorization` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Certificates</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of client certificate thumbprints to present to the backend host. The certificates must exist within the API Management Service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Header</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A mapping of header parameters to pass to the backend host. The keys are the header names and the values are a comma separated string of header values. This is converted to a list before being passed to the API.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Query</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A mapping of query parameters to pass to the backend host. The keys are the query names and the values are a comma separated string of query values. This is converted to a list before being passed to the API.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>authorization</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendcredentialsauthorization">Backend<wbr>Credentials<wbr>Authorization?</a></span>
    </dt>
    <dd>{{% md %}}An `authorization` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>certificates</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of client certificate thumbprints to present to the backend host. The certificates must exist within the API Management Service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>header</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}A mapping of header parameters to pass to the backend host. The keys are the header names and the values are a comma separated string of header values. This is converted to a list before being passed to the API.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>query</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}A mapping of query parameters to pass to the backend host. The keys are the query names and the values are a comma separated string of query values. This is converted to a list before being passed to the API.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>authorization</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendcredentialsauthorization">Dict[Backend<wbr>Credentials<wbr>Authorization]</a></span>
    </dt>
    <dd>{{% md %}}An `authorization` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>certificates</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of client certificate thumbprints to present to the backend host. The certificates must exist within the API Management Service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>header</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A mapping of header parameters to pass to the backend host. The keys are the header names and the values are a comma separated string of header values. This is converted to a list before being passed to the API.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>query</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A mapping of query parameters to pass to the backend host. The keys are the query names and the values are a comma separated string of query values. This is converted to a list before being passed to the API.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Backend<wbr>Credentials<wbr>Authorization</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#BackendCredentialsAuthorization">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#BackendCredentialsAuthorization">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/apimanagement?tab=doc#BackendCredentialsAuthorizationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/apimanagement?tab=doc#BackendCredentialsAuthorizationOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Parameter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The authentication Parameter value.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scheme</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The authentication Scheme name.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Parameter</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The authentication Parameter value.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scheme</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The authentication Scheme name.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>parameter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The authentication Parameter value.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scheme</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The authentication Scheme name.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>parameter</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The authentication Parameter value.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scheme</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The authentication Scheme name.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Backend<wbr>Proxy</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#BackendProxy">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#BackendProxy">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/apimanagement?tab=doc#BackendProxyArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/apimanagement?tab=doc#BackendProxyOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The password to connect to the proxy server.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The URL of the proxy server.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The username to connect to the proxy server.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The password to connect to the proxy server.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The URL of the proxy server.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The username to connect to the proxy server.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The password to connect to the proxy server.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The URL of the proxy server.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The username to connect to the proxy server.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>password</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The password to connect to the proxy server.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>url</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The URL of the proxy server.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>username</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The username to connect to the proxy server.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Backend<wbr>Service<wbr>Fabric<wbr>Cluster</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#BackendServiceFabricCluster">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#BackendServiceFabricCluster">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/apimanagement?tab=doc#BackendServiceFabricClusterArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/apimanagement?tab=doc#BackendServiceFabricClusterOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Client<wbr>Certificate<wbr>Thumbprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The client certificate thumbprint for the management endpoint.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Management<wbr>Endpoints</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}A list of cluster management endpoints.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Max<wbr>Partition<wbr>Resolution<wbr>Retries</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The maximum number of retries when attempting resolve the partition.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Server<wbr>Certificate<wbr>Thumbprints</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of thumbprints of the server certificates of the Service Fabric cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Server<wbr>X509Names</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicefabricclusterserverx509name">List&lt;Backend<wbr>Service<wbr>Fabric<wbr>Cluster<wbr>Server<wbr>X509Name<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}One or more `server_x509_name` blocks as documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Client<wbr>Certificate<wbr>Thumbprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The client certificate thumbprint for the management endpoint.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Management<wbr>Endpoints</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of cluster management endpoints.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Max<wbr>Partition<wbr>Resolution<wbr>Retries</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The maximum number of retries when attempting resolve the partition.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Server<wbr>Certificate<wbr>Thumbprints</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of thumbprints of the server certificates of the Service Fabric cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Server<wbr>X509Names</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicefabricclusterserverx509name">[]Backend<wbr>Service<wbr>Fabric<wbr>Cluster<wbr>Server<wbr>X509Name</a></span>
    </dt>
    <dd>{{% md %}}One or more `server_x509_name` blocks as documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>client<wbr>Certificate<wbr>Thumbprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The client certificate thumbprint for the management endpoint.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>management<wbr>Endpoints</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}A list of cluster management endpoints.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>max<wbr>Partition<wbr>Resolution<wbr>Retries</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The maximum number of retries when attempting resolve the partition.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>server<wbr>Certificate<wbr>Thumbprints</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of thumbprints of the server certificates of the Service Fabric cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>server<wbr>X509Names</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicefabricclusterserverx509name">Backend<wbr>Service<wbr>Fabric<wbr>Cluster<wbr>Server<wbr>X509Name[]?</a></span>
    </dt>
    <dd>{{% md %}}One or more `server_x509_name` blocks as documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>client<wbr>Certificate<wbr>Thumbprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The client certificate thumbprint for the management endpoint.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>management<wbr>Endpoints</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of cluster management endpoints.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>max<wbr>Partition<wbr>Resolution<wbr>Retries</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum number of retries when attempting resolve the partition.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>server<wbr>Certificate<wbr>Thumbprints</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of thumbprints of the server certificates of the Service Fabric cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>server<wbr>X509Names</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendservicefabricclusterserverx509name">List[Backend<wbr>Service<wbr>Fabric<wbr>Cluster<wbr>Server<wbr>X509Name]</a></span>
    </dt>
    <dd>{{% md %}}One or more `server_x509_name` blocks as documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Backend<wbr>Service<wbr>Fabric<wbr>Cluster<wbr>Server<wbr>X509Name</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#BackendServiceFabricClusterServerX509Name">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#BackendServiceFabricClusterServerX509Name">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/apimanagement?tab=doc#BackendServiceFabricClusterServerX509NameArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/apimanagement?tab=doc#BackendServiceFabricClusterServerX509NameOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Issuer<wbr>Certificate<wbr>Thumbprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The thumbprint for the issuer of the certificate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the API Management backend. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Issuer<wbr>Certificate<wbr>Thumbprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The thumbprint for the issuer of the certificate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the API Management backend. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>issuer<wbr>Certificate<wbr>Thumbprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The thumbprint for the issuer of the certificate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the API Management backend. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>issuer<wbr>Certificate<wbr>Thumbprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The thumbprint for the issuer of the certificate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the API Management backend. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Backend<wbr>Tls</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#BackendTls">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#BackendTls">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/apimanagement?tab=doc#BackendTlsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/apimanagement?tab=doc#BackendTlsOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Validate<wbr>Certificate<wbr>Chain</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag indicating whether SSL certificate chain validation should be done when using self-signed certificates for the backend host.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Validate<wbr>Certificate<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag indicating whether SSL certificate name validation should be done when using self-signed certificates for the backend host.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Validate<wbr>Certificate<wbr>Chain</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag indicating whether SSL certificate chain validation should be done when using self-signed certificates for the backend host.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Validate<wbr>Certificate<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag indicating whether SSL certificate name validation should be done when using self-signed certificates for the backend host.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>validate<wbr>Certificate<wbr>Chain</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag indicating whether SSL certificate chain validation should be done when using self-signed certificates for the backend host.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>validate<wbr>Certificate<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag indicating whether SSL certificate name validation should be done when using self-signed certificates for the backend host.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>validate<wbr>Certificate<wbr>Chain</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag indicating whether SSL certificate chain validation should be done when using self-signed certificates for the backend host.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>validate<wbr>Certificate<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag indicating whether SSL certificate name validation should be done when using self-signed certificates for the backend host.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}









<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-azure">https://github.com/pulumi/pulumi-azure</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    
</dl>

