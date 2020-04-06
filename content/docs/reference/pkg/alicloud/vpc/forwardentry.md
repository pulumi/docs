
---
title: "ForwardEntry"
block_external_search_index: true
---



Provides a forward resource.

> This content is derived from https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/forward_entry.html.markdown.



## Create a ForwardEntry Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/vpc/#ForwardEntry">ForwardEntry</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/vpc/#ForwardEntryArgs">ForwardEntryArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">ForwardEntry</span><span class="p">(resource_name, opts=None, </span>external_ip=None<span class="p">, </span>external_port=None<span class="p">, </span>forward_table_id=None<span class="p">, </span>internal_ip=None<span class="p">, </span>internal_port=None<span class="p">, </span>ip_protocol=None<span class="p">, </span>name=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewForwardEntry<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/vpc?tab=doc#ForwardEntryArgs">ForwardEntryArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/vpc?tab=doc#ForwardEntry">ForwardEntry</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Vpc.ForwardEntry.html">ForwardEntry</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Vpc.ForwardEntryArgs.html">ForwardEntryArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>External<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The external ip address, the ip must along bandwidth package public ip which `alicloud.vpc.NatGateway` argument `bandwidth_packages`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>External<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The external port, valid value is 1~65535|any.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Forward<wbr>Table<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The value can get from `alicloud.vpc.NatGateway` Attributes "forward_table_ids".
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Internal<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The internal ip, must a private ip.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Internal<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The internal port, valid value is 1~65535|any.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Ip<wbr>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ip protocal, valid value is tcp|udp|any.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of forward entry.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>External<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The external ip address, the ip must along bandwidth package public ip which `alicloud.vpc.NatGateway` argument `bandwidth_packages`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>External<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The external port, valid value is 1~65535|any.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Forward<wbr>Table<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The value can get from `alicloud.vpc.NatGateway` Attributes "forward_table_ids".
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Internal<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The internal ip, must a private ip.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Internal<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The internal port, valid value is 1~65535|any.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Ip<wbr>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ip protocal, valid value is tcp|udp|any.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of forward entry.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>external<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The external ip address, the ip must along bandwidth package public ip which `alicloud.vpc.NatGateway` argument `bandwidth_packages`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>external<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The external port, valid value is 1~65535|any.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>forward<wbr>Table<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The value can get from `alicloud.vpc.NatGateway` Attributes "forward_table_ids".
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>internal<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The internal ip, must a private ip.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>internal<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The internal port, valid value is 1~65535|any.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>ip<wbr>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ip protocal, valid value is tcp|udp|any.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of forward entry.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>external_<wbr>ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The external ip address, the ip must along bandwidth package public ip which `alicloud.vpc.NatGateway` argument `bandwidth_packages`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>external_<wbr>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The external port, valid value is 1~65535|any.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>forward_<wbr>table_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The value can get from `alicloud.vpc.NatGateway` Attributes "forward_table_ids".
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>internal_<wbr>ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The internal ip, must a private ip.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>internal_<wbr>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The internal port, valid value is 1~65535|any.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>ip_<wbr>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ip protocal, valid value is tcp|udp|any.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of forward entry.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## ForwardEntry Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>External<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The external ip address, the ip must along bandwidth package public ip which `alicloud.vpc.NatGateway` argument `bandwidth_packages`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>External<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The external port, valid value is 1~65535|any.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Forward<wbr>Entry<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The id of the forward entry on the server.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Forward<wbr>Table<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The value can get from `alicloud.vpc.NatGateway` Attributes "forward_table_ids".
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Internal<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The internal ip, must a private ip.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Internal<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The internal port, valid value is 1~65535|any.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ip<wbr>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ip protocal, valid value is tcp|udp|any.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of forward entry.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>External<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The external ip address, the ip must along bandwidth package public ip which `alicloud.vpc.NatGateway` argument `bandwidth_packages`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>External<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The external port, valid value is 1~65535|any.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Forward<wbr>Entry<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The id of the forward entry on the server.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Forward<wbr>Table<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The value can get from `alicloud.vpc.NatGateway` Attributes "forward_table_ids".
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Internal<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The internal ip, must a private ip.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Internal<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The internal port, valid value is 1~65535|any.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ip<wbr>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ip protocal, valid value is tcp|udp|any.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of forward entry.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>external<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The external ip address, the ip must along bandwidth package public ip which `alicloud.vpc.NatGateway` argument `bandwidth_packages`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>external<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The external port, valid value is 1~65535|any.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>forward<wbr>Entry<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The id of the forward entry on the server.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>forward<wbr>Table<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The value can get from `alicloud.vpc.NatGateway` Attributes "forward_table_ids".
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>internal<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The internal ip, must a private ip.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>internal<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The internal port, valid value is 1~65535|any.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ip<wbr>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ip protocal, valid value is tcp|udp|any.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of forward entry.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>external_<wbr>ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The external ip address, the ip must along bandwidth package public ip which `alicloud.vpc.NatGateway` argument `bandwidth_packages`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>external_<wbr>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The external port, valid value is 1~65535|any.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>forward_<wbr>entry_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The id of the forward entry on the server.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>forward_<wbr>table_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The value can get from `alicloud.vpc.NatGateway` Attributes "forward_table_ids".
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>internal_<wbr>ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The internal ip, must a private ip.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>internal_<wbr>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The internal port, valid value is 1~65535|any.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ip_<wbr>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ip protocal, valid value is tcp|udp|any.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of forward entry.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing ForwardEntry Resource

Get an existing ForwardEntry resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/vpc/#ForwardEntryState">ForwardEntryState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/vpc/#ForwardEntry">ForwardEntry</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>external_ip=None<span class="p">, </span>external_port=None<span class="p">, </span>forward_entry_id=None<span class="p">, </span>forward_table_id=None<span class="p">, </span>internal_ip=None<span class="p">, </span>internal_port=None<span class="p">, </span>ip_protocol=None<span class="p">, </span>name=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetForwardEntry<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/vpc?tab=doc#ForwardEntryState">ForwardEntryState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/vpc?tab=doc#ForwardEntry">ForwardEntry</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Vpc.ForwardEntry.html">ForwardEntry</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Vpc.ForwardEntryState.html">ForwardEntryState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>External<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The external ip address, the ip must along bandwidth package public ip which `alicloud.vpc.NatGateway` argument `bandwidth_packages`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>External<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The external port, valid value is 1~65535|any.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Forward<wbr>Entry<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The id of the forward entry on the server.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Forward<wbr>Table<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The value can get from `alicloud.vpc.NatGateway` Attributes "forward_table_ids".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Internal<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The internal ip, must a private ip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Internal<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The internal port, valid value is 1~65535|any.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ip<wbr>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ip protocal, valid value is tcp|udp|any.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of forward entry.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>External<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The external ip address, the ip must along bandwidth package public ip which `alicloud.vpc.NatGateway` argument `bandwidth_packages`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>External<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The external port, valid value is 1~65535|any.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Forward<wbr>Entry<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The id of the forward entry on the server.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Forward<wbr>Table<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The value can get from `alicloud.vpc.NatGateway` Attributes "forward_table_ids".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Internal<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The internal ip, must a private ip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Internal<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The internal port, valid value is 1~65535|any.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ip<wbr>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ip protocal, valid value is tcp|udp|any.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of forward entry.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>external<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The external ip address, the ip must along bandwidth package public ip which `alicloud.vpc.NatGateway` argument `bandwidth_packages`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>external<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The external port, valid value is 1~65535|any.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>forward<wbr>Entry<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The id of the forward entry on the server.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>forward<wbr>Table<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The value can get from `alicloud.vpc.NatGateway` Attributes "forward_table_ids".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>internal<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The internal ip, must a private ip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>internal<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The internal port, valid value is 1~65535|any.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ip<wbr>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ip protocal, valid value is tcp|udp|any.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of forward entry.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>external_<wbr>ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The external ip address, the ip must along bandwidth package public ip which `alicloud.vpc.NatGateway` argument `bandwidth_packages`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>external_<wbr>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The external port, valid value is 1~65535|any.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>forward_<wbr>entry_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The id of the forward entry on the server.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>forward_<wbr>table_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The value can get from `alicloud.vpc.NatGateway` Attributes "forward_table_ids".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>internal_<wbr>ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The internal ip, must a private ip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>internal_<wbr>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The internal port, valid value is 1~65535|any.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ip_<wbr>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ip protocal, valid value is tcp|udp|any.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of forward entry.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}











<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-alicloud">https://github.com/pulumi/pulumi-alicloud</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    
</dl>

