
---
title: "Policy"
block_external_search_index: true
---

A policy is a collection of DNS rules applied to one or more Virtual
Private Cloud resources.

To get more information about Policy, see:

* [API documentation](https://cloud.google.com/dns/docs/reference/v1beta2/policies)
* How-to Guides
    * [Using DNS server policies](https://cloud.google.com/dns/zones/#using-dns-server-policies)

> This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/dns_policy.html.markdown.



## Create a Policy Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/dns/#Policy">Policy</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/dns/#PolicyArgs">PolicyArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Policy</span><span class="p">(resource_name, opts=None, </span>alternative_name_server_config=None<span class="p">, </span>description=None<span class="p">, </span>enable_inbound_forwarding=None<span class="p">, </span>enable_logging=None<span class="p">, </span>name=None<span class="p">, </span>networks=None<span class="p">, </span>project=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewPolicy<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/dns?tab=doc#PolicyArgs">PolicyArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/dns?tab=doc#Policy">Policy</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Dns.Policy.html">Policy</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Dns.PolicyArgs.html">PolicyArgs</a></span>? <span class="nx">args = null<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Alternative<wbr>Name<wbr>Server<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyalternativenameserverconfig">Policy<wbr>Alternative<wbr>Name<wbr>Server<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Sets an alternative name server for the associated networks. When specified, all DNS queries are forwarded to a name
server that you choose. Names such as .internal are not available when an alternative name server is specified.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A textual description field. Defaults to 'Managed by Terraform'.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Inbound<wbr>Forwarding</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Allows networks bound to this policy to receive DNS queries sent by VMs or applications over VPN connections. When
enabled, a virtual IP address will be allocated from each of the sub-networks that are bound to this policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Logging</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Controls whether logging is enabled for the networks bound to this policy. Defaults to no logging if not set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}User assigned name for this policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Networks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policynetwork">List&lt;Policy<wbr>Network<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}List of network names specifying networks to which this policy is applied.
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

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Alternative<wbr>Name<wbr>Server<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyalternativenameserverconfig">*Policy<wbr>Alternative<wbr>Name<wbr>Server<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Sets an alternative name server for the associated networks. When specified, all DNS queries are forwarded to a name
server that you choose. Names such as .internal are not available when an alternative name server is specified.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A textual description field. Defaults to 'Managed by Terraform'.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Inbound<wbr>Forwarding</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Allows networks bound to this policy to receive DNS queries sent by VMs or applications over VPN connections. When
enabled, a virtual IP address will be allocated from each of the sub-networks that are bound to this policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Logging</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Controls whether logging is enabled for the networks bound to this policy. Defaults to no logging if not set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}User assigned name for this policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Networks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policynetwork">[]Policy<wbr>Network</a></span>
    </dt>
    <dd>{{% md %}}List of network names specifying networks to which this policy is applied.
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

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>alternative<wbr>Name<wbr>Server<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyalternativenameserverconfig">Policy<wbr>Alternative<wbr>Name<wbr>Server<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Sets an alternative name server for the associated networks. When specified, all DNS queries are forwarded to a name
server that you choose. Names such as .internal are not available when an alternative name server is specified.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A textual description field. Defaults to 'Managed by Terraform'.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Inbound<wbr>Forwarding</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Allows networks bound to this policy to receive DNS queries sent by VMs or applications over VPN connections. When
enabled, a virtual IP address will be allocated from each of the sub-networks that are bound to this policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Logging</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Controls whether logging is enabled for the networks bound to this policy. Defaults to no logging if not set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}User assigned name for this policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>networks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policynetwork">Policy<wbr>Network[]?</a></span>
    </dt>
    <dd>{{% md %}}List of network names specifying networks to which this policy is applied.
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

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>alternative_<wbr>name_<wbr>server_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyalternativenameserverconfig">Dict[Policy<wbr>Alternative<wbr>Name<wbr>Server<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Sets an alternative name server for the associated networks. When specified, all DNS queries are forwarded to a name
server that you choose. Names such as .internal are not available when an alternative name server is specified.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A textual description field. Defaults to 'Managed by Terraform'.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>inbound_<wbr>forwarding</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Allows networks bound to this policy to receive DNS queries sent by VMs or applications over VPN connections. When
enabled, a virtual IP address will be allocated from each of the sub-networks that are bound to this policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>logging</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Controls whether logging is enabled for the networks bound to this policy. Defaults to no logging if not set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}User assigned name for this policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>networks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policynetwork">List[Policy<wbr>Network]</a></span>
    </dt>
    <dd>{{% md %}}List of network names specifying networks to which this policy is applied.
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

</dl>
{{% /choosable %}}







## Policy Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Alternative<wbr>Name<wbr>Server<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyalternativenameserverconfig">Policy<wbr>Alternative<wbr>Name<wbr>Server<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Sets an alternative name server for the associated networks. When specified, all DNS queries are forwarded to a name
server that you choose. Names such as .internal are not available when an alternative name server is specified.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A textual description field. Defaults to 'Managed by Terraform'.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enable<wbr>Inbound<wbr>Forwarding</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Allows networks bound to this policy to receive DNS queries sent by VMs or applications over VPN connections. When
enabled, a virtual IP address will be allocated from each of the sub-networks that are bound to this policy.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enable<wbr>Logging</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Controls whether logging is enabled for the networks bound to this policy. Defaults to no logging if not set.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}User assigned name for this policy.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Networks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policynetwork">List&lt;Policy<wbr>Network&gt;?</a></span>
    </dt>
    <dd>{{% md %}}List of network names specifying networks to which this policy is applied.
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

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Alternative<wbr>Name<wbr>Server<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyalternativenameserverconfig">*Policy<wbr>Alternative<wbr>Name<wbr>Server<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Sets an alternative name server for the associated networks. When specified, all DNS queries are forwarded to a name
server that you choose. Names such as .internal are not available when an alternative name server is specified.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A textual description field. Defaults to 'Managed by Terraform'.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enable<wbr>Inbound<wbr>Forwarding</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Allows networks bound to this policy to receive DNS queries sent by VMs or applications over VPN connections. When
enabled, a virtual IP address will be allocated from each of the sub-networks that are bound to this policy.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enable<wbr>Logging</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Controls whether logging is enabled for the networks bound to this policy. Defaults to no logging if not set.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}User assigned name for this policy.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Networks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policynetwork">[]Policy<wbr>Network</a></span>
    </dt>
    <dd>{{% md %}}List of network names specifying networks to which this policy is applied.
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

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>alternative<wbr>Name<wbr>Server<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyalternativenameserverconfig">Policy<wbr>Alternative<wbr>Name<wbr>Server<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Sets an alternative name server for the associated networks. When specified, all DNS queries are forwarded to a name
server that you choose. Names such as .internal are not available when an alternative name server is specified.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A textual description field. Defaults to 'Managed by Terraform'.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enable<wbr>Inbound<wbr>Forwarding</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Allows networks bound to this policy to receive DNS queries sent by VMs or applications over VPN connections. When
enabled, a virtual IP address will be allocated from each of the sub-networks that are bound to this policy.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enable<wbr>Logging</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Controls whether logging is enabled for the networks bound to this policy. Defaults to no logging if not set.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}User assigned name for this policy.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>networks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policynetwork">Policy<wbr>Network[]?</a></span>
    </dt>
    <dd>{{% md %}}List of network names specifying networks to which this policy is applied.
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

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>alternative_<wbr>name_<wbr>server_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyalternativenameserverconfig">Dict[Policy<wbr>Alternative<wbr>Name<wbr>Server<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Sets an alternative name server for the associated networks. When specified, all DNS queries are forwarded to a name
server that you choose. Names such as .internal are not available when an alternative name server is specified.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A textual description field. Defaults to 'Managed by Terraform'.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enable_<wbr>inbound_<wbr>forwarding</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Allows networks bound to this policy to receive DNS queries sent by VMs or applications over VPN connections. When
enabled, a virtual IP address will be allocated from each of the sub-networks that are bound to this policy.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enable_<wbr>logging</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Controls whether logging is enabled for the networks bound to this policy. Defaults to no logging if not set.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}User assigned name for this policy.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>networks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policynetwork">List[Policy<wbr>Network]</a></span>
    </dt>
    <dd>{{% md %}}List of network names specifying networks to which this policy is applied.
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

</dl>
{{% /choosable %}}








## Look up an Existing Policy Resource

Get an existing Policy resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/dns/#PolicyState">PolicyState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/dns/#Policy">Policy</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>alternative_name_server_config=None<span class="p">, </span>description=None<span class="p">, </span>enable_inbound_forwarding=None<span class="p">, </span>enable_logging=None<span class="p">, </span>name=None<span class="p">, </span>networks=None<span class="p">, </span>project=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetPolicy<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/dns?tab=doc#PolicyState">PolicyState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/dns?tab=doc#Policy">Policy</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Dns.Policy.html">Policy</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Dns.PolicyState.html">PolicyState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Alternative<wbr>Name<wbr>Server<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyalternativenameserverconfig">Policy<wbr>Alternative<wbr>Name<wbr>Server<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Sets an alternative name server for the associated networks. When specified, all DNS queries are forwarded to a name
server that you choose. Names such as .internal are not available when an alternative name server is specified.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A textual description field. Defaults to 'Managed by Terraform'.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Inbound<wbr>Forwarding</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Allows networks bound to this policy to receive DNS queries sent by VMs or applications over VPN connections. When
enabled, a virtual IP address will be allocated from each of the sub-networks that are bound to this policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Logging</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Controls whether logging is enabled for the networks bound to this policy. Defaults to no logging if not set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}User assigned name for this policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Networks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policynetwork">List&lt;Policy<wbr>Network<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}List of network names specifying networks to which this policy is applied.
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

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Alternative<wbr>Name<wbr>Server<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyalternativenameserverconfig">*Policy<wbr>Alternative<wbr>Name<wbr>Server<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Sets an alternative name server for the associated networks. When specified, all DNS queries are forwarded to a name
server that you choose. Names such as .internal are not available when an alternative name server is specified.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A textual description field. Defaults to 'Managed by Terraform'.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Inbound<wbr>Forwarding</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Allows networks bound to this policy to receive DNS queries sent by VMs or applications over VPN connections. When
enabled, a virtual IP address will be allocated from each of the sub-networks that are bound to this policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Logging</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Controls whether logging is enabled for the networks bound to this policy. Defaults to no logging if not set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}User assigned name for this policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Networks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policynetwork">[]Policy<wbr>Network</a></span>
    </dt>
    <dd>{{% md %}}List of network names specifying networks to which this policy is applied.
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

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>alternative<wbr>Name<wbr>Server<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyalternativenameserverconfig">Policy<wbr>Alternative<wbr>Name<wbr>Server<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Sets an alternative name server for the associated networks. When specified, all DNS queries are forwarded to a name
server that you choose. Names such as .internal are not available when an alternative name server is specified.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A textual description field. Defaults to 'Managed by Terraform'.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Inbound<wbr>Forwarding</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Allows networks bound to this policy to receive DNS queries sent by VMs or applications over VPN connections. When
enabled, a virtual IP address will be allocated from each of the sub-networks that are bound to this policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Logging</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Controls whether logging is enabled for the networks bound to this policy. Defaults to no logging if not set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}User assigned name for this policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>networks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policynetwork">Policy<wbr>Network[]?</a></span>
    </dt>
    <dd>{{% md %}}List of network names specifying networks to which this policy is applied.
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

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>alternative_<wbr>name_<wbr>server_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyalternativenameserverconfig">Dict[Policy<wbr>Alternative<wbr>Name<wbr>Server<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Sets an alternative name server for the associated networks. When specified, all DNS queries are forwarded to a name
server that you choose. Names such as .internal are not available when an alternative name server is specified.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A textual description field. Defaults to 'Managed by Terraform'.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>inbound_<wbr>forwarding</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Allows networks bound to this policy to receive DNS queries sent by VMs or applications over VPN connections. When
enabled, a virtual IP address will be allocated from each of the sub-networks that are bound to this policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>logging</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Controls whether logging is enabled for the networks bound to this policy. Defaults to no logging if not set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}User assigned name for this policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>networks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policynetwork">List[Policy<wbr>Network]</a></span>
    </dt>
    <dd>{{% md %}}List of network names specifying networks to which this policy is applied.
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

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Policy<wbr>Alternative<wbr>Name<wbr>Server<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#PolicyAlternativeNameServerConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#PolicyAlternativeNameServerConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/dns?tab=doc#PolicyAlternativeNameServerConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/dns?tab=doc#PolicyAlternativeNameServerConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Target<wbr>Name<wbr>Servers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyalternativenameserverconfigtargetnameserver">List&lt;Policy<wbr>Alternative<wbr>Name<wbr>Server<wbr>Config<wbr>Target<wbr>Name<wbr>Server<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Target<wbr>Name<wbr>Servers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyalternativenameserverconfigtargetnameserver">[]Policy<wbr>Alternative<wbr>Name<wbr>Server<wbr>Config<wbr>Target<wbr>Name<wbr>Server</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>target<wbr>Name<wbr>Servers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyalternativenameserverconfigtargetnameserver">Policy<wbr>Alternative<wbr>Name<wbr>Server<wbr>Config<wbr>Target<wbr>Name<wbr>Server[]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>target<wbr>Name<wbr>Servers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyalternativenameserverconfigtargetnameserver">List[Policy<wbr>Alternative<wbr>Name<wbr>Server<wbr>Config<wbr>Target<wbr>Name<wbr>Server]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Policy<wbr>Alternative<wbr>Name<wbr>Server<wbr>Config<wbr>Target<wbr>Name<wbr>Server</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#PolicyAlternativeNameServerConfigTargetNameServer">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#PolicyAlternativeNameServerConfigTargetNameServer">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/dns?tab=doc#PolicyAlternativeNameServerConfigTargetNameServerArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/dns?tab=doc#PolicyAlternativeNameServerConfigTargetNameServerOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Ipv4Address</span>
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
        <span>Ipv4Address</span>
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
        <span>ipv4Address</span>
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
        <span>ipv4Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Policy<wbr>Network</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#PolicyNetwork">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#PolicyNetwork">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/dns?tab=doc#PolicyNetworkArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/dns?tab=doc#PolicyNetworkOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Network<wbr>Url</span>
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
        <span>Network<wbr>Url</span>
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
        <span>network<wbr>Url</span>
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
        <span>network<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}








<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-gcp">https://github.com/pulumi/pulumi-gcp</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd></dl>
