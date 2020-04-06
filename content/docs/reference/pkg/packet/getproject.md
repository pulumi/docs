
---
title: "GetProject"
block_external_search_index: true
---



Use this datasource to retrieve attributes of the Project API resource.

> This content is derived from https://github.com/terraform-providers/terraform-provider-packet/blob/master/website/docs/d/project.html.markdown.





## Using GetProject

{{< chooser language "javascript,typescript,python,go,csharp" / >}}


{{% choosable language typescript %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getProject<span class="p">(</span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/packet/#GetProjectArgs">GetProjectArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#InvokeOptions">InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/packet/#GetProjectResult">GetProjectResult</a></span>></span></code></pre></div>
{{% /choosable %}}


{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_project(</span>name=None<span class="p">, </span>project_id=None<span class="p">, </span>opts=None<span class="p">)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupProject<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-packet/sdk/go/packet/?tab=doc#GetProjectArgs">GetProjectArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#InvokeOption">InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-packet/sdk/go/packet/?tab=doc#LookupProjectResult">LookupProjectResult</a></span>, error)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static class </span><span class="nx">GetProject </span><span class="p">{</span><span class="k">
    public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Packet/Pulumi.Packet.GetProjectResult.html">GetProjectResult</a></span>> <span class="p">InvokeAsync(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Packet/Pulumi.Packet.GetProjectArgs.html">GetProjectArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.InvokeOptions.html">InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span><span class="p">
}</span></code></pre></div>
{{% /choosable %}}



The following arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name which is used to look up the project
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The UUID by which to look up the project
{{% /md %}}</dd>

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
    <dd>{{% md %}}The name which is used to look up the project
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The UUID by which to look up the project
{{% /md %}}</dd>

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
    <dd>{{% md %}}The name which is used to look up the project
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The UUID by which to look up the project
{{% /md %}}</dd>

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
    <dd>{{% md %}}The name which is used to look up the project
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The UUID by which to look up the project
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## GetProject Result

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Backend<wbr>Transfer</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether Backend Transfer is enabled for this project
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Bgp<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getprojectbgpconfig">Get<wbr>Project<wbr>Bgp<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Optional BGP settings. Refer to [Packet guide for BGP](https://www.packet.com/developers/docs/network/advanced/local-and-global-bgp/).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Created</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The timestamp for when the project was created
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
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Organization<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The UUID of this project's parent organization
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Payment<wbr>Method<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The UUID of payment method for this project
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Project<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Updated</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The timestamp for the last time the project was updated
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>User<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}List of UUIDs of user accounts which beling to this project
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Backend<wbr>Transfer</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether Backend Transfer is enabled for this project
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Bgp<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getprojectbgpconfig">Get<wbr>Project<wbr>Bgp<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Optional BGP settings. Refer to [Packet guide for BGP](https://www.packet.com/developers/docs/network/advanced/local-and-global-bgp/).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Created</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The timestamp for when the project was created
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
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Organization<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The UUID of this project's parent organization
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Payment<wbr>Method<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The UUID of payment method for this project
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Project<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Updated</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The timestamp for the last time the project was updated
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>User<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of UUIDs of user accounts which beling to this project
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>backend<wbr>Transfer</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Whether Backend Transfer is enabled for this project
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>bgp<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getprojectbgpconfig">Get<wbr>Project<wbr>Bgp<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Optional BGP settings. Refer to [Packet guide for BGP](https://www.packet.com/developers/docs/network/advanced/local-and-global-bgp/).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>created</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The timestamp for when the project was created
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
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>organization<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The UUID of this project's parent organization
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>payment<wbr>Method<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The UUID of payment method for this project
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>project<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>updated</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The timestamp for the last time the project was updated
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>user<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}List of UUIDs of user accounts which beling to this project
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>backend_<wbr>transfer</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether Backend Transfer is enabled for this project
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>bgp_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getprojectbgpconfig">Dict[Get<wbr>Project<wbr>Bgp<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Optional BGP settings. Refer to [Packet guide for BGP](https://www.packet.com/developers/docs/network/advanced/local-and-global-bgp/).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>created</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The timestamp for when the project was created
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
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>organization_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The UUID of this project's parent organization
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>payment_<wbr>method_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The UUID of payment method for this project
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>project_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>updated</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The timestamp for the last time the project was updated
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>user_<wbr>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of UUIDs of user accounts which beling to this project
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Supporting Types

<h4>Get<wbr>Project<wbr>Bgp<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/packet/types/output/#GetProjectBgpConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-packet/sdk/go/packet/?tab=doc#GetProjectBgpConfig">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Asn</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Autonomous System Numer for local BGP deployment
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Deployment<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}`private` or `public`, the `private` is likely to be usable immediately, the `public` will need to be review by Packet engineers
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Max<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The maximum number of route filters allowed per server
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Md5</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Password for BGP session in plaintext (not a checksum)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}status of BGP configuration in the project
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Asn</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Autonomous System Numer for local BGP deployment
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Deployment<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}`private` or `public`, the `private` is likely to be usable immediately, the `public` will need to be review by Packet engineers
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Max<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The maximum number of route filters allowed per server
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Md5</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Password for BGP session in plaintext (not a checksum)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}status of BGP configuration in the project
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>asn</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Autonomous System Numer for local BGP deployment
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>deployment<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}`private` or `public`, the `private` is likely to be usable immediately, the `public` will need to be review by Packet engineers
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>max<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The maximum number of route filters allowed per server
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>md5</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Password for BGP session in plaintext (not a checksum)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}status of BGP configuration in the project
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>asn</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Autonomous System Numer for local BGP deployment
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>deployment<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}`private` or `public`, the `private` is likely to be usable immediately, the `public` will need to be review by Packet engineers
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>max<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum number of route filters allowed per server
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>md5</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Password for BGP session in plaintext (not a checksum)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}status of BGP configuration in the project
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







