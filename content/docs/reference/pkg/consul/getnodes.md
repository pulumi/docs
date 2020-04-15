
---
title: "GetNodes"
block_external_search_index: true
---



The `consul..getNodes` data source returns a list of Consul nodes that have
been registered with the Consul cluster in a given datacenter.  By specifying a
different datacenter in the `query_options` it is possible to retrieve a list of
nodes from a different WAN-attached Consul datacenter.

> This content is derived from https://github.com/terraform-providers/terraform-provider-consul/blob/master/website/docs/d/nodes.html.markdown.





## Using GetNodes

{{< chooser language "javascript,typescript,python,go,csharp" / >}}


{{% choosable language typescript %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getNodes<span class="p">(</span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/consul/#GetNodesArgs">GetNodesArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#InvokeOptions">InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/consul/#GetNodesResult">GetNodesResult</a></span>></span></code></pre></div>
{{% /choosable %}}


{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_nodes(</span>query_options=None<span class="p">, </span>opts=None<span class="p">)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupNodes<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-consul/sdk/go/consul/?tab=doc#GetNodesArgs">GetNodesArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#InvokeOption">pulumi.InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-consul/sdk/go/consul/?tab=doc#LookupNodesResult">LookupNodesResult</a></span>, error)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static class </span><span class="nx">GetNodes </span><span class="p">{</span><span class="k">
    public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Consul/Pulumi.Consul.GetNodesResult.html">GetNodesResult</a></span>> <span class="p">InvokeAsync(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Consul/Pulumi.Consul.GetNodesArgs.html">GetNodesArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.InvokeOptions.html">InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span><span class="p">
}</span></code></pre></div>
{{% /choosable %}}



The following arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Query<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getnodesqueryoption">List&lt;Get<wbr>Nodes<wbr>Query<wbr>Option<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}See below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Query<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getnodesqueryoption">[]Get<wbr>Nodes<wbr>Query<wbr>Option</a></span>
    </dt>
    <dd>{{% md %}}See below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>query<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getnodesqueryoption">Get<wbr>Nodes<wbr>Query<wbr>Option[]</a></span>
    </dt>
    <dd>{{% md %}}See below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>query_<wbr>options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getnodesqueryoption">List[Get<wbr>Nodes<wbr>Query<wbr>Option]</a></span>
    </dt>
    <dd>{{% md %}}See below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## GetNodes Result

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Datacenter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The datacenter the keys are being read from to.
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
        <span>Node<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List&lt;string&gt;</span>
    </dt>
    <dd>{{% md %}}A list of the Consul node IDs.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Node<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type">List&lt;string&gt;</span>
    </dt>
    <dd>{{% md %}}A list of the Consul node names.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Nodes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getnodesnode">List&lt;Get<wbr>Nodes<wbr>Node&gt;</a></span>
    </dt>
    <dd>{{% md %}}A list of nodes and details about each Consul agent.  The list of
per-node attributes is detailed below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Query<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getnodesqueryoption">List&lt;Get<wbr>Nodes<wbr>Query<wbr>Option&gt;</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Datacenter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The datacenter the keys are being read from to.
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
        <span>Node<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of the Consul node IDs.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Node<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of the Consul node names.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Nodes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getnodesnode">[]Get<wbr>Nodes<wbr>Node</a></span>
    </dt>
    <dd>{{% md %}}A list of nodes and details about each Consul agent.  The list of
per-node attributes is detailed below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Query<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getnodesqueryoption">[]Get<wbr>Nodes<wbr>Query<wbr>Option</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>datacenter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The datacenter the keys are being read from to.
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
        <span>node<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}A list of the Consul node IDs.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>node<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}A list of the Consul node names.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>nodes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getnodesnode">Get<wbr>Nodes<wbr>Node[]</a></span>
    </dt>
    <dd>{{% md %}}A list of nodes and details about each Consul agent.  The list of
per-node attributes is detailed below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>query<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getnodesqueryoption">Get<wbr>Nodes<wbr>Query<wbr>Option[]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>datacenter</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The datacenter the keys are being read from to.
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
        <span>node_<wbr>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of the Consul node IDs.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>node_<wbr>names</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of the Consul node names.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>nodes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getnodesnode">List[Get<wbr>Nodes<wbr>Node]</a></span>
    </dt>
    <dd>{{% md %}}A list of nodes and details about each Consul agent.  The list of
per-node attributes is detailed below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>query_<wbr>options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getnodesqueryoption">List[Get<wbr>Nodes<wbr>Query<wbr>Option]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Supporting Types

<h4>Get<wbr>Nodes<wbr>Node</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/consul/types/output/#GetNodesNode">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-consul/sdk/go/consul/?tab=doc#GetNodesNode">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Node ID of the Consul agent.
* [`meta`](https://www.consul.io/docs/agent/http/catalog.html#Meta) - Node meta
data tag information, if any.
* [`name`](https://www.consul.io/docs/agent/http/catalog.html#Node) - The name
of the Consul node.
* [`address`](https://www.consul.io/docs/agent/http/catalog.html#Address) - The
IP address the node is advertising to the Consul cluster.
* [`tagged_addresses`](https://www.consul.io/docs/agent/http/catalog.html#TaggedAddresses) -
List of explicit LAN and WAN IP addresses for the agent.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Meta</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, string&gt;</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Tagged<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, string&gt;</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Node ID of the Consul agent.
* [`meta`](https://www.consul.io/docs/agent/http/catalog.html#Meta) - Node meta
data tag information, if any.
* [`name`](https://www.consul.io/docs/agent/http/catalog.html#Node) - The name
of the Consul node.
* [`address`](https://www.consul.io/docs/agent/http/catalog.html#Address) - The
IP address the node is advertising to the Consul cluster.
* [`tagged_addresses`](https://www.consul.io/docs/agent/http/catalog.html#TaggedAddresses) -
List of explicit LAN and WAN IP addresses for the agent.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Meta</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Tagged<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Node ID of the Consul agent.
* [`meta`](https://www.consul.io/docs/agent/http/catalog.html#Meta) - Node meta
data tag information, if any.
* [`name`](https://www.consul.io/docs/agent/http/catalog.html#Node) - The name
of the Consul node.
* [`address`](https://www.consul.io/docs/agent/http/catalog.html#Address) - The
IP address the node is advertising to the Consul cluster.
* [`tagged_addresses`](https://www.consul.io/docs/agent/http/catalog.html#TaggedAddresses) -
List of explicit LAN and WAN IP addresses for the agent.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>meta</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>tagged<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>address</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Node ID of the Consul agent.
* [`meta`](https://www.consul.io/docs/agent/http/catalog.html#Meta) - Node meta
data tag information, if any.
* [`name`](https://www.consul.io/docs/agent/http/catalog.html#Node) - The name
of the Consul node.
* [`address`](https://www.consul.io/docs/agent/http/catalog.html#Address) - The
IP address the node is advertising to the Consul cluster.
* [`tagged_addresses`](https://www.consul.io/docs/agent/http/catalog.html#TaggedAddresses) -
List of explicit LAN and WAN IP addresses for the agent.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>meta</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>tagged<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Get<wbr>Nodes<wbr>Query<wbr>Option</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/consul/types/input/#GetNodesQueryOption">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/consul/types/output/#GetNodesQueryOption">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-consul/sdk/go/consul/?tab=doc#GetNodesQueryOptionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-consul/sdk/go/consul/?tab=doc#GetNodesQueryOption">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Stale</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}When `true`, the default, allow responses from
Consul servers that are followers.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Datacenter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Consul datacenter to query.  Defaults to the
same value found in `query_options` parameter specified below, or if that is
empty, the `datacenter` value found in the Consul agent that this provider is
configured to talk to then the datacenter in the provider setup.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Near</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Meta</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, string&gt;</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Require<wbr>Consistent</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}When `true` force the client to perform a
read on at least quorum servers and verify the result is the same.  Defaults
to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specify the Consul ACL token to use when performing the
request.  This defaults to the same API token configured by the `consul`
provider but may be overriden if necessary.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Wait<wbr>Index</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Index number used to enable blocking quereis.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Wait<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Max time the client should wait for a blocking query
to return.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Stale</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}When `true`, the default, allow responses from
Consul servers that are followers.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Datacenter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Consul datacenter to query.  Defaults to the
same value found in `query_options` parameter specified below, or if that is
empty, the `datacenter` value found in the Consul agent that this provider is
configured to talk to then the datacenter in the provider setup.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Near</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Meta</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Require<wbr>Consistent</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}When `true` force the client to perform a
read on at least quorum servers and verify the result is the same.  Defaults
to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specify the Consul ACL token to use when performing the
request.  This defaults to the same API token configured by the `consul`
provider but may be overriden if necessary.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Wait<wbr>Index</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Index number used to enable blocking quereis.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Wait<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Max time the client should wait for a blocking query
to return.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Stale</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}When `true`, the default, allow responses from
Consul servers that are followers.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>datacenter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Consul datacenter to query.  Defaults to the
same value found in `query_options` parameter specified below, or if that is
empty, the `datacenter` value found in the Consul agent that this provider is
configured to talk to then the datacenter in the provider setup.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>near</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node<wbr>Meta</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>require<wbr>Consistent</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}When `true` force the client to perform a
read on at least quorum servers and verify the result is the same.  Defaults
to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specify the Consul ACL token to use when performing the
request.  This defaults to the same API token configured by the `consul`
provider but may be overriden if necessary.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>wait<wbr>Index</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Index number used to enable blocking quereis.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>wait<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Max time the client should wait for a blocking query
to return.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Stale</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}When `true`, the default, allow responses from
Consul servers that are followers.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>datacenter</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Consul datacenter to query.  Defaults to the
same value found in `query_options` parameter specified below, or if that is
empty, the `datacenter` value found in the Consul agent that this provider is
configured to talk to then the datacenter in the provider setup.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>near</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node<wbr>Meta</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>require<wbr>Consistent</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}When `true` force the client to perform a
read on at least quorum servers and verify the result is the same.  Defaults
to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specify the Consul ACL token to use when performing the
request.  This defaults to the same API token configured by the `consul`
provider but may be overriden if necessary.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>wait<wbr>Index</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Index number used to enable blocking quereis.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>wait<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Max time the client should wait for a blocking query
to return.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







