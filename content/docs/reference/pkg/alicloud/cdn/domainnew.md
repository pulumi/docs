
---
title: "DomainNew"
block_external_search_index: true
---



Provides a CDN Accelerated Domain resource. This resource is based on CDN's new version OpenAPI.

For information about Cdn Domain New and how to use it, see [Add a domain](https://www.alibabacloud.com/help/doc-detail/91176.html).

> **NOTE:** Available in v1.34.0+.

> This content is derived from https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/cdn_domain_new.html.markdown.



## Create a DomainNew Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/cdn/#DomainNew">DomainNew</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/cdn/#DomainNewArgs">DomainNewArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">DomainNew</span><span class="p">(resource_name, opts=None, </span>cdn_type=None<span class="p">, </span>certificate_config=None<span class="p">, </span>domain_name=None<span class="p">, </span>resource_group_id=None<span class="p">, </span>scope=None<span class="p">, </span>sources=None<span class="p">, </span>tags=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewDomainNew<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/cdn?tab=doc#DomainNewArgs">DomainNewArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/cdn?tab=doc#DomainNew">DomainNew</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Cdn.DomainNew.html">DomainNew</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Cdn.DomainNewArgs.html">DomainNewArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Cdn<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Cdn type of the accelerated domain. Valid values are `web`, `download`, `video`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Certificate<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainnewcertificateconfig">Domain<wbr>New<wbr>Certificate<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Certificate config of the accelerated domain. It's a list and consist of at most 1 item.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Domain<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the accelerated domain. This name without suffix can have a string of 1 to 63 characters, must contain only alphanumeric characters or "-", and must not begin or end with "-", and "-" must not in the 3th and 4th character positions at the same time. Suffix `.sh` and `.tel` are not supported.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Resource group ID.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scope</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Scope of the accelerated domain. Valid values are `domestic`, `overseas`, `global`. Default value is `domestic`. This parameter's setting is valid Only for the international users and domestic L3 and above users .
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Sources</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainnewsources">Domain<wbr>New<wbr>Sources<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}The source address list of the accelerated domain. Defaults to null. See Block Sources.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Cdn<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Cdn type of the accelerated domain. Valid values are `web`, `download`, `video`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Certificate<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainnewcertificateconfig">*Domain<wbr>New<wbr>Certificate<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Certificate config of the accelerated domain. It's a list and consist of at most 1 item.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Domain<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the accelerated domain. This name without suffix can have a string of 1 to 63 characters, must contain only alphanumeric characters or "-", and must not begin or end with "-", and "-" must not in the 3th and 4th character positions at the same time. Suffix `.sh` and `.tel` are not supported.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Resource group ID.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scope</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Scope of the accelerated domain. Valid values are `domestic`, `overseas`, `global`. Default value is `domestic`. This parameter's setting is valid Only for the international users and domestic L3 and above users .
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Sources</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainnewsources">Domain<wbr>New<wbr>Sources</a></span>
    </dt>
    <dd>{{% md %}}The source address list of the accelerated domain. Defaults to null. See Block Sources.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>cdn<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Cdn type of the accelerated domain. Valid values are `web`, `download`, `video`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>certificate<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainnewcertificateconfig">Domain<wbr>New<wbr>Certificate<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Certificate config of the accelerated domain. It's a list and consist of at most 1 item.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>domain<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the accelerated domain. This name without suffix can have a string of 1 to 63 characters, must contain only alphanumeric characters or "-", and must not begin or end with "-", and "-" must not in the 3th and 4th character positions at the same time. Suffix `.sh` and `.tel` are not supported.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Resource group ID.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scope</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Scope of the accelerated domain. Valid values are `domestic`, `overseas`, `global`. Default value is `domestic`. This parameter's setting is valid Only for the international users and domestic L3 and above users .
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>sources</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainnewsources">Domain<wbr>New<wbr>Sources</a></span>
    </dt>
    <dd>{{% md %}}The source address list of the accelerated domain. Defaults to null. See Block Sources.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>cdn_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Cdn type of the accelerated domain. Valid values are `web`, `download`, `video`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>certificate_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainnewcertificateconfig">Dict[Domain<wbr>New<wbr>Certificate<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Certificate config of the accelerated domain. It's a list and consist of at most 1 item.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>domain_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the accelerated domain. This name without suffix can have a string of 1 to 63 characters, must contain only alphanumeric characters or "-", and must not begin or end with "-", and "-" must not in the 3th and 4th character positions at the same time. Suffix `.sh` and `.tel` are not supported.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource_<wbr>group_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Resource group ID.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scope</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Scope of the accelerated domain. Valid values are `domestic`, `overseas`, `global`. Default value is `domestic`. This parameter's setting is valid Only for the international users and domestic L3 and above users .
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>sources</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainnewsources">Dict[Domain<wbr>New<wbr>Sources]</a></span>
    </dt>
    <dd>{{% md %}}The source address list of the accelerated domain. Defaults to null. See Block Sources.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## DomainNew Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Cdn<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Cdn type of the accelerated domain. Valid values are `web`, `download`, `video`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Certificate<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainnewcertificateconfig">Domain<wbr>New<wbr>Certificate<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Certificate config of the accelerated domain. It's a list and consist of at most 1 item.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Domain<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the accelerated domain. This name without suffix can have a string of 1 to 63 characters, must contain only alphanumeric characters or "-", and must not begin or end with "-", and "-" must not in the 3th and 4th character positions at the same time. Suffix `.sh` and `.tel` are not supported.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Resource<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Resource group ID.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Scope</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Scope of the accelerated domain. Valid values are `domestic`, `overseas`, `global`. Default value is `domestic`. This parameter's setting is valid Only for the international users and domestic L3 and above users .
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Sources</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainnewsources">Domain<wbr>New<wbr>Sources</a></span>
    </dt>
    <dd>{{% md %}}The source address list of the accelerated domain. Defaults to null. See Block Sources.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Cdn<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Cdn type of the accelerated domain. Valid values are `web`, `download`, `video`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Certificate<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainnewcertificateconfig">Domain<wbr>New<wbr>Certificate<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Certificate config of the accelerated domain. It's a list and consist of at most 1 item.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Domain<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the accelerated domain. This name without suffix can have a string of 1 to 63 characters, must contain only alphanumeric characters or "-", and must not begin or end with "-", and "-" must not in the 3th and 4th character positions at the same time. Suffix `.sh` and `.tel` are not supported.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Resource<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Resource group ID.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Scope</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Scope of the accelerated domain. Valid values are `domestic`, `overseas`, `global`. Default value is `domestic`. This parameter's setting is valid Only for the international users and domestic L3 and above users .
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Sources</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainnewsources">Domain<wbr>New<wbr>Sources</a></span>
    </dt>
    <dd>{{% md %}}The source address list of the accelerated domain. Defaults to null. See Block Sources.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>cdn<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Cdn type of the accelerated domain. Valid values are `web`, `download`, `video`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>certificate<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainnewcertificateconfig">Domain<wbr>New<wbr>Certificate<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Certificate config of the accelerated domain. It's a list and consist of at most 1 item.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>domain<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the accelerated domain. This name without suffix can have a string of 1 to 63 characters, must contain only alphanumeric characters or "-", and must not begin or end with "-", and "-" must not in the 3th and 4th character positions at the same time. Suffix `.sh` and `.tel` are not supported.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>resource<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Resource group ID.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>scope</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Scope of the accelerated domain. Valid values are `domestic`, `overseas`, `global`. Default value is `domestic`. This parameter's setting is valid Only for the international users and domestic L3 and above users .
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>sources</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainnewsources">Domain<wbr>New<wbr>Sources</a></span>
    </dt>
    <dd>{{% md %}}The source address list of the accelerated domain. Defaults to null. See Block Sources.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>cdn_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Cdn type of the accelerated domain. Valid values are `web`, `download`, `video`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>certificate_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainnewcertificateconfig">Dict[Domain<wbr>New<wbr>Certificate<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Certificate config of the accelerated domain. It's a list and consist of at most 1 item.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>domain_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the accelerated domain. This name without suffix can have a string of 1 to 63 characters, must contain only alphanumeric characters or "-", and must not begin or end with "-", and "-" must not in the 3th and 4th character positions at the same time. Suffix `.sh` and `.tel` are not supported.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>resource_<wbr>group_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Resource group ID.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>scope</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Scope of the accelerated domain. Valid values are `domestic`, `overseas`, `global`. Default value is `domestic`. This parameter's setting is valid Only for the international users and domestic L3 and above users .
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>sources</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainnewsources">Dict[Domain<wbr>New<wbr>Sources]</a></span>
    </dt>
    <dd>{{% md %}}The source address list of the accelerated domain. Defaults to null. See Block Sources.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing DomainNew Resource

Get an existing DomainNew resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/cdn/#DomainNewState">DomainNewState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/cdn/#DomainNew">DomainNew</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>cdn_type=None<span class="p">, </span>certificate_config=None<span class="p">, </span>domain_name=None<span class="p">, </span>resource_group_id=None<span class="p">, </span>scope=None<span class="p">, </span>sources=None<span class="p">, </span>tags=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetDomainNew<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/cdn?tab=doc#DomainNewState">DomainNewState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/cdn?tab=doc#DomainNew">DomainNew</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Cdn.DomainNew.html">DomainNew</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Cdn.DomainNewState.html">DomainNewState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Cdn<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Cdn type of the accelerated domain. Valid values are `web`, `download`, `video`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Certificate<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainnewcertificateconfig">Domain<wbr>New<wbr>Certificate<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Certificate config of the accelerated domain. It's a list and consist of at most 1 item.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Domain<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the accelerated domain. This name without suffix can have a string of 1 to 63 characters, must contain only alphanumeric characters or "-", and must not begin or end with "-", and "-" must not in the 3th and 4th character positions at the same time. Suffix `.sh` and `.tel` are not supported.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Resource group ID.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scope</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Scope of the accelerated domain. Valid values are `domestic`, `overseas`, `global`. Default value is `domestic`. This parameter's setting is valid Only for the international users and domestic L3 and above users .
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sources</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainnewsources">Domain<wbr>New<wbr>Sources<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The source address list of the accelerated domain. Defaults to null. See Block Sources.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Cdn<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Cdn type of the accelerated domain. Valid values are `web`, `download`, `video`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Certificate<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainnewcertificateconfig">*Domain<wbr>New<wbr>Certificate<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Certificate config of the accelerated domain. It's a list and consist of at most 1 item.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Domain<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of the accelerated domain. This name without suffix can have a string of 1 to 63 characters, must contain only alphanumeric characters or "-", and must not begin or end with "-", and "-" must not in the 3th and 4th character positions at the same time. Suffix `.sh` and `.tel` are not supported.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Resource group ID.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scope</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Scope of the accelerated domain. Valid values are `domestic`, `overseas`, `global`. Default value is `domestic`. This parameter's setting is valid Only for the international users and domestic L3 and above users .
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sources</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainnewsources">*Domain<wbr>New<wbr>Sources</a></span>
    </dt>
    <dd>{{% md %}}The source address list of the accelerated domain. Defaults to null. See Block Sources.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>cdn<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Cdn type of the accelerated domain. Valid values are `web`, `download`, `video`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>certificate<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainnewcertificateconfig">Domain<wbr>New<wbr>Certificate<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Certificate config of the accelerated domain. It's a list and consist of at most 1 item.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>domain<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the accelerated domain. This name without suffix can have a string of 1 to 63 characters, must contain only alphanumeric characters or "-", and must not begin or end with "-", and "-" must not in the 3th and 4th character positions at the same time. Suffix `.sh` and `.tel` are not supported.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Resource group ID.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scope</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Scope of the accelerated domain. Valid values are `domestic`, `overseas`, `global`. Default value is `domestic`. This parameter's setting is valid Only for the international users and domestic L3 and above users .
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sources</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainnewsources">Domain<wbr>New<wbr>Sources?</a></span>
    </dt>
    <dd>{{% md %}}The source address list of the accelerated domain. Defaults to null. See Block Sources.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>cdn_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Cdn type of the accelerated domain. Valid values are `web`, `download`, `video`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>certificate_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainnewcertificateconfig">Dict[Domain<wbr>New<wbr>Certificate<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Certificate config of the accelerated domain. It's a list and consist of at most 1 item.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>domain_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the accelerated domain. This name without suffix can have a string of 1 to 63 characters, must contain only alphanumeric characters or "-", and must not begin or end with "-", and "-" must not in the 3th and 4th character positions at the same time. Suffix `.sh` and `.tel` are not supported.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource_<wbr>group_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Resource group ID.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scope</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Scope of the accelerated domain. Valid values are `domestic`, `overseas`, `global`. Default value is `domestic`. This parameter's setting is valid Only for the international users and domestic L3 and above users .
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sources</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainnewsources">Dict[Domain<wbr>New<wbr>Sources]</a></span>
    </dt>
    <dd>{{% md %}}The source address list of the accelerated domain. Defaults to null. See Block Sources.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Domain<wbr>New<wbr>Certificate<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/input/#DomainNewCertificateConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/output/#DomainNewCertificateConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/cdn?tab=doc#DomainNewCertificateConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/cdn?tab=doc#DomainNewCertificateConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Cert<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The SSL certificate name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cert<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The SSL certificate type, can be "upload", "cas" and "free".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Force<wbr>Set</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Set `1` to ignore the repeated verification for certificate name, and cover the information of the origin certificate (with the same name). Set `0` to work the verification.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Private<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The SSL private key. This is required if `server_certificate_status` is `on`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Server<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The SSL server certificate string. This is required if `server_certificate_status` is `on`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Server<wbr>Certificate<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}This parameter indicates whether or not enable https. Valid values are `on` and `off`. Default value is `on`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Cert<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The SSL certificate name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cert<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The SSL certificate type, can be "upload", "cas" and "free".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Force<wbr>Set</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Set `1` to ignore the repeated verification for certificate name, and cover the information of the origin certificate (with the same name). Set `0` to work the verification.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Private<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The SSL private key. This is required if `server_certificate_status` is `on`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Server<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The SSL server certificate string. This is required if `server_certificate_status` is `on`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Server<wbr>Certificate<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}This parameter indicates whether or not enable https. Valid values are `on` and `off`. Default value is `on`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>cert<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The SSL certificate name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cert<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The SSL certificate type, can be "upload", "cas" and "free".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>force<wbr>Set</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Set `1` to ignore the repeated verification for certificate name, and cover the information of the origin certificate (with the same name). Set `0` to work the verification.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>private<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The SSL private key. This is required if `server_certificate_status` is `on`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>server<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The SSL server certificate string. This is required if `server_certificate_status` is `on`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>server<wbr>Certificate<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}This parameter indicates whether or not enable https. Valid values are `on` and `off`. Default value is `on`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>cert<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The SSL certificate name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cert<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The SSL certificate type, can be "upload", "cas" and "free".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>force<wbr>Set</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Set `1` to ignore the repeated verification for certificate name, and cover the information of the origin certificate (with the same name). Set `0` to work the verification.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>private_<wbr>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The SSL private key. This is required if `server_certificate_status` is `on`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>server_<wbr>certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The SSL server certificate string. This is required if `server_certificate_status` is `on`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>server<wbr>Certificate<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}This parameter indicates whether or not enable https. Valid values are `on` and `off`. Default value is `on`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Domain<wbr>New<wbr>Sources</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/input/#DomainNewSources">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/output/#DomainNewSources">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/cdn?tab=doc#DomainNewSourcesArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/cdn?tab=doc#DomainNewSourcesOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Content</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The adress of source. Valid values can be ip or doaminName. Each item's `content` can not be repeated.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The port of source. Valid values are `443` and `80`. Default value is `80`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Priority of the source. Valid values are `0` and `100`. Default value is `20`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of the source. Valid values are `ipaddr`, `domain` and `oss`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Weight</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Weight of the source. Valid values are from `0` to `100`. Default value is `10`, but if type is `ipaddr`, the value can only be `10`. 
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Content</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The adress of source. Valid values can be ip or doaminName. Each item's `content` can not be repeated.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The port of source. Valid values are `443` and `80`. Default value is `80`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Priority of the source. Valid values are `0` and `100`. Default value is `20`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of the source. Valid values are `ipaddr`, `domain` and `oss`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Weight</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Weight of the source. Valid values are from `0` to `100`. Default value is `10`, but if type is `ipaddr`, the value can only be `10`. 
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>content</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The adress of source. Valid values can be ip or doaminName. Each item's `content` can not be repeated.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The port of source. Valid values are `443` and `80`. Default value is `80`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Priority of the source. Valid values are `0` and `100`. Default value is `20`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of the source. Valid values are `ipaddr`, `domain` and `oss`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>weight</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Weight of the source. Valid values are from `0` to `100`. Default value is `10`, but if type is `ipaddr`, the value can only be `10`. 
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>content</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The adress of source. Valid values can be ip or doaminName. Each item's `content` can not be repeated.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The port of source. Valid values are `443` and `80`. Default value is `80`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Priority of the source. Valid values are `0` and `100`. Default value is `20`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The type of the source. Valid values are `ipaddr`, `domain` and `oss`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>weight</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Weight of the source. Valid values are from `0` to `100`. Default value is `10`, but if type is `ipaddr`, the value can only be `10`. 
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

