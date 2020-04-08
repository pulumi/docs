
---
title: "GetRouterInterfaces"
block_external_search_index: true
---



This data source provides information about [router interfaces](https://www.alibabacloud.com/help/doc-detail/52412.htm)
that connect VPCs together.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as alicloud from "@pulumi/alicloud";

const routerInterfacesDs = pulumi.output(alicloud.vpc.getRouterInterfaces({
    nameRegex: "^testenv",
    status: "Active",
}, { async: true }));

export const firstRouterInterfaceId = routerInterfacesDs.interfaces[0].id;
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/router_interfaces.html.markdown.





## Using GetRouterInterfaces

{{< chooser language "javascript,typescript,python,go,csharp" / >}}


{{% choosable language typescript %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getRouterInterfaces<span class="p">(</span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/vpc/#GetRouterInterfacesArgs">GetRouterInterfacesArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#InvokeOptions">InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/vpc/#GetRouterInterfacesResult">GetRouterInterfacesResult</a></span>></span></code></pre></div>
{{% /choosable %}}


{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_router_interfaces(</span>ids=None<span class="p">, </span>name_regex=None<span class="p">, </span>opposite_interface_id=None<span class="p">, </span>opposite_interface_owner_id=None<span class="p">, </span>output_file=None<span class="p">, </span>role=None<span class="p">, </span>router_id=None<span class="p">, </span>router_type=None<span class="p">, </span>specification=None<span class="p">, </span>status=None<span class="p">, </span>opts=None<span class="p">)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupRouterInterfaces<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/vpc?tab=doc#LookupRouterInterfacesArgs">LookupRouterInterfacesArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#InvokeOption">InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/vpc?tab=doc#LookupRouterInterfacesResult">LookupRouterInterfacesResult</a></span>, error)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static class </span><span class="nx">GetRouterInterfaces </span><span class="p">{</span><span class="k">
    public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Vpc.GetRouterInterfacesResult.html">GetRouterInterfacesResult</a></span>> <span class="p">InvokeAsync(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Vpc.GetRouterInterfacesArgs.html">GetRouterInterfacesArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.InvokeOptions.html">InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span><span class="p">
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
    <dd>{{% md %}}A list of router interface IDs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A regex string used to filter by router interface name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Opposite<wbr>Interface<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}ID of the peer router interface.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Opposite<wbr>Interface<wbr>Owner<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Account ID of the owner of the peer router interface.
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
        <span>Role</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Role of the router interface. Valid values are `InitiatingSide` (connection initiator) and 
`AcceptingSide` (connection receiver). The value of this parameter must be `InitiatingSide` if the `router_type` is set to `VBR`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Router<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}ID of the VRouter located in the local region.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Router<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Router type in the local region. Valid values are `VRouter` and `VBR` (physical connection).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Specification</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specification of the link, such as `Small.1` (10Mb), `Middle.1` (100Mb), `Large.2` (2Gb), ...etc.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Expected status. Valid values are `Active`, `Inactive` and `Idle`.
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
    <dd>{{% md %}}A list of router interface IDs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A regex string used to filter by router interface name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Opposite<wbr>Interface<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}ID of the peer router interface.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Opposite<wbr>Interface<wbr>Owner<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Account ID of the owner of the peer router interface.
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
        <span>Role</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Role of the router interface. Valid values are `InitiatingSide` (connection initiator) and 
`AcceptingSide` (connection receiver). The value of this parameter must be `InitiatingSide` if the `router_type` is set to `VBR`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Router<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}ID of the VRouter located in the local region.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Router<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Router type in the local region. Valid values are `VRouter` and `VBR` (physical connection).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Specification</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specification of the link, such as `Small.1` (10Mb), `Middle.1` (100Mb), `Large.2` (2Gb), ...etc.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Expected status. Valid values are `Active`, `Inactive` and `Idle`.
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
    <dd>{{% md %}}A list of router interface IDs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A regex string used to filter by router interface name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>opposite<wbr>Interface<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}ID of the peer router interface.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>opposite<wbr>Interface<wbr>Owner<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Account ID of the owner of the peer router interface.
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
        <span>role</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Role of the router interface. Valid values are `InitiatingSide` (connection initiator) and 
`AcceptingSide` (connection receiver). The value of this parameter must be `InitiatingSide` if the `router_type` is set to `VBR`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>router<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}ID of the VRouter located in the local region.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>router<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Router type in the local region. Valid values are `VRouter` and `VBR` (physical connection).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>specification</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specification of the link, such as `Small.1` (10Mb), `Middle.1` (100Mb), `Large.2` (2Gb), ...etc.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Expected status. Valid values are `Active`, `Inactive` and `Idle`.
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
    <dd>{{% md %}}A list of router interface IDs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name_<wbr>regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A regex string used to filter by router interface name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>opposite_<wbr>interface_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}ID of the peer router interface.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>opposite_<wbr>interface_<wbr>owner_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Account ID of the owner of the peer router interface.
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
        <span>role</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Role of the router interface. Valid values are `InitiatingSide` (connection initiator) and 
`AcceptingSide` (connection receiver). The value of this parameter must be `InitiatingSide` if the `router_type` is set to `VBR`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>router_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}ID of the VRouter located in the local region.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>router_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Router type in the local region. Valid values are `VRouter` and `VBR` (physical connection).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>specification</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specification of the link, such as `Small.1` (10Mb), `Middle.1` (100Mb), `Large.2` (2Gb), ...etc.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Expected status. Valid values are `Active`, `Inactive` and `Idle`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## GetRouterInterfaces Result

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

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
    <dd>{{% md %}}A list of router interface IDs.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Interfaces</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getrouterinterfacesinterface">List&lt;Get<wbr>Router<wbr>Interfaces<wbr>Interface&gt;</a></span>
    </dt>
    <dd>{{% md %}}A list of router interfaces. Each element contains the following attributes:
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
    <dd>{{% md %}}A list of router interface names.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Opposite<wbr>Interface<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Peer router interface ID.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Opposite<wbr>Interface<wbr>Owner<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Account ID of the owner of the peer router interface.
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
        <span>Role</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Router interface role. Possible values: `InitiatingSide` and `AcceptingSide`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Router<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}ID of the VRouter located in the local region.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Router<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Router type in the local region. Possible values: `VRouter` and `VBR`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Specification</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Router interface specification. Possible values: `Small.1`, `Middle.1`, `Large.2`, ...etc.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Router interface status. Possible values: `Active`, `Inactive` and `Idle`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

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
    <dd>{{% md %}}A list of router interface IDs.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Interfaces</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getrouterinterfacesinterface">[]Get<wbr>Router<wbr>Interfaces<wbr>Interface</a></span>
    </dt>
    <dd>{{% md %}}A list of router interfaces. Each element contains the following attributes:
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
    <dd>{{% md %}}A list of router interface names.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Opposite<wbr>Interface<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Peer router interface ID.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Opposite<wbr>Interface<wbr>Owner<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Account ID of the owner of the peer router interface.
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
        <span>Role</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Router interface role. Possible values: `InitiatingSide` and `AcceptingSide`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Router<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}ID of the VRouter located in the local region.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Router<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Router type in the local region. Possible values: `VRouter` and `VBR`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Specification</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Router interface specification. Possible values: `Small.1`, `Middle.1`, `Large.2`, ...etc.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Router interface status. Possible values: `Active`, `Inactive` and `Idle`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

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
    <dd>{{% md %}}A list of router interface IDs.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>interfaces</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getrouterinterfacesinterface">Get<wbr>Router<wbr>Interfaces<wbr>Interface[]</a></span>
    </dt>
    <dd>{{% md %}}A list of router interfaces. Each element contains the following attributes:
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
    <dd>{{% md %}}A list of router interface names.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>opposite<wbr>Interface<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Peer router interface ID.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>opposite<wbr>Interface<wbr>Owner<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Account ID of the owner of the peer router interface.
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
        <span>role</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Router interface role. Possible values: `InitiatingSide` and `AcceptingSide`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>router<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}ID of the VRouter located in the local region.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>router<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Router type in the local region. Possible values: `VRouter` and `VBR`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>specification</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Router interface specification. Possible values: `Small.1`, `Middle.1`, `Large.2`, ...etc.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Router interface status. Possible values: `Active`, `Inactive` and `Idle`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

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
    <dd>{{% md %}}A list of router interface IDs.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>interfaces</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getrouterinterfacesinterface">List[Get<wbr>Router<wbr>Interfaces<wbr>Interface]</a></span>
    </dt>
    <dd>{{% md %}}A list of router interfaces. Each element contains the following attributes:
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
    <dd>{{% md %}}A list of router interface names.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>opposite_<wbr>interface_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Peer router interface ID.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>opposite_<wbr>interface_<wbr>owner_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Account ID of the owner of the peer router interface.
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
        <span>role</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Router interface role. Possible values: `InitiatingSide` and `AcceptingSide`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>router_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}ID of the VRouter located in the local region.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>router_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Router type in the local region. Possible values: `VRouter` and `VBR`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>specification</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Router interface specification. Possible values: `Small.1`, `Middle.1`, `Large.2`, ...etc.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Router interface status. Possible values: `Active`, `Inactive` and `Idle`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Supporting Types

<h4>Get<wbr>Router<wbr>Interfaces<wbr>Interface</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/output/#GetRouterInterfacesInterface">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/vpc?tab=doc#GetRouterInterfacesInterface">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Access<wbr>Point<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the access point used by the VBR.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Creation<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Router interface creation time.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Router interface description.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Health<wbr>Check<wbr>Source<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Source IP address used to perform health check on the physical connection.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Health<wbr>Check<wbr>Target<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Destination IP address used to perform health check on the physical connection.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Router interface ID.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Router interface name.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Opposite<wbr>Interface<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the peer router interface.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Opposite<wbr>Interface<wbr>Owner<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Account ID of the owner of the peer router interface.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Opposite<wbr>Region<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Peer router region ID.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Opposite<wbr>Router<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Peer router ID.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Opposite<wbr>Router<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Router type in the peer region. Possible values: `VRouter` and `VBR`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Role</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Role of the router interface. Valid values are `InitiatingSide` (connection initiator) and 
`AcceptingSide` (connection receiver). The value of this parameter must be `InitiatingSide` if the `router_type` is set to `VBR`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Router<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the VRouter located in the local region.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Router<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Router type in the local region. Valid values are `VRouter` and `VBR` (physical connection).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Specification</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specification of the link, such as `Small.1` (10Mb), `Middle.1` (100Mb), `Large.2` (2Gb), ...etc.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Expected status. Valid values are `Active`, `Inactive` and `Idle`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Vpc<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the VPC that owns the router in the local region.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Access<wbr>Point<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the access point used by the VBR.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Creation<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Router interface creation time.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Router interface description.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Health<wbr>Check<wbr>Source<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Source IP address used to perform health check on the physical connection.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Health<wbr>Check<wbr>Target<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Destination IP address used to perform health check on the physical connection.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Router interface ID.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Router interface name.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Opposite<wbr>Interface<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the peer router interface.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Opposite<wbr>Interface<wbr>Owner<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Account ID of the owner of the peer router interface.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Opposite<wbr>Region<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Peer router region ID.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Opposite<wbr>Router<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Peer router ID.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Opposite<wbr>Router<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Router type in the peer region. Possible values: `VRouter` and `VBR`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Role</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Role of the router interface. Valid values are `InitiatingSide` (connection initiator) and 
`AcceptingSide` (connection receiver). The value of this parameter must be `InitiatingSide` if the `router_type` is set to `VBR`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Router<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the VRouter located in the local region.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Router<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Router type in the local region. Valid values are `VRouter` and `VBR` (physical connection).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Specification</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specification of the link, such as `Small.1` (10Mb), `Middle.1` (100Mb), `Large.2` (2Gb), ...etc.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Expected status. Valid values are `Active`, `Inactive` and `Idle`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Vpc<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the VPC that owns the router in the local region.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>access<wbr>Point<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the access point used by the VBR.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>creation<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Router interface creation time.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Router interface description.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>health<wbr>Check<wbr>Source<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Source IP address used to perform health check on the physical connection.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>health<wbr>Check<wbr>Target<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Destination IP address used to perform health check on the physical connection.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Router interface ID.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Router interface name.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>opposite<wbr>Interface<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the peer router interface.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>opposite<wbr>Interface<wbr>Owner<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Account ID of the owner of the peer router interface.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>opposite<wbr>Region<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Peer router region ID.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>opposite<wbr>Router<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Peer router ID.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>opposite<wbr>Router<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Router type in the peer region. Possible values: `VRouter` and `VBR`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>role</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Role of the router interface. Valid values are `InitiatingSide` (connection initiator) and 
`AcceptingSide` (connection receiver). The value of this parameter must be `InitiatingSide` if the `router_type` is set to `VBR`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>router<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the VRouter located in the local region.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>router<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Router type in the local region. Valid values are `VRouter` and `VBR` (physical connection).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>specification</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specification of the link, such as `Small.1` (10Mb), `Middle.1` (100Mb), `Large.2` (2Gb), ...etc.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Expected status. Valid values are `Active`, `Inactive` and `Idle`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>vpc<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the VPC that owns the router in the local region.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>access_<wbr>point_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}ID of the access point used by the VBR.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>creation_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Router interface creation time.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Router interface description.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>health_<wbr>check_<wbr>source_<wbr>ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Source IP address used to perform health check on the physical connection.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>health_<wbr>check_<wbr>target_<wbr>ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Destination IP address used to perform health check on the physical connection.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Router interface ID.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Router interface name.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>opposite_<wbr>interface_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}ID of the peer router interface.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>opposite_<wbr>interface_<wbr>owner_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Account ID of the owner of the peer router interface.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>opposite<wbr>Region<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Peer router region ID.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>opposite_<wbr>router_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Peer router ID.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>opposite_<wbr>router_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Router type in the peer region. Possible values: `VRouter` and `VBR`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>role</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Role of the router interface. Valid values are `InitiatingSide` (connection initiator) and 
`AcceptingSide` (connection receiver). The value of this parameter must be `InitiatingSide` if the `router_type` is set to `VBR`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>router_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}ID of the VRouter located in the local region.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>router_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Router type in the local region. Valid values are `VRouter` and `VBR` (physical connection).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>specification</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specification of the link, such as `Small.1` (10Mb), `Middle.1` (100Mb), `Large.2` (2Gb), ...etc.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Expected status. Valid values are `Active`, `Inactive` and `Idle`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>vpc_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}ID of the VPC that owns the router in the local region.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







