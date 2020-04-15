
---
title: "Domain"
block_external_search_index: true
---






## Create a Domain Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/cdn/#Domain">Domain</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/cdn/#DomainArgs">DomainArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Domain</span><span class="p">(resource_name, opts=None, </span>auth_config=None<span class="p">, </span>block_ips=None<span class="p">, </span>cache_configs=None<span class="p">, </span>cdn_type=None<span class="p">, </span>certificate_config=None<span class="p">, </span>domain_name=None<span class="p">, </span>http_header_configs=None<span class="p">, </span>optimize_enable=None<span class="p">, </span>page404_config=None<span class="p">, </span>page_compress_enable=None<span class="p">, </span>parameter_filter_config=None<span class="p">, </span>range_enable=None<span class="p">, </span>refer_config=None<span class="p">, </span>scope=None<span class="p">, </span>source_port=None<span class="p">, </span>source_type=None<span class="p">, </span>sources=None<span class="p">, </span>video_seek_enable=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewDomain<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/cdn?tab=doc#DomainArgs">DomainArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/cdn?tab=doc#Domain">Domain</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Cdn.Domain.html">Domain</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.AliCloud.Cdn.DomainArgs.html">DomainArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
    <dd>{{% md %}}Cdn type of the accelerated domain. Valid values are `web`, `download`, `video`, `liveStream`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Domain<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the accelerated domain. This name without suffix can have a string of 1 to 63 characters, must contain only alphanumeric characters or "-", and must not begin or end with "-", and "-" must not in the 3th and 4th character positions at the same time. Suffix `.sh` and `.tel` are not supported.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Auth<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainauthconfig">Pulumi.<wbr>Ali<wbr>Cloud.<wbr>Cdn.<wbr>Inputs.<wbr>Domain<wbr>Auth<wbr>Config<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}The auth config of the accelerated domain.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Block<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type">List&lt;string&gt;</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Cache<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domaincacheconfig">List&lt;Pulumi.<wbr>Ali<wbr>Cloud.<wbr>Cdn.<wbr>Inputs.<wbr>Domain<wbr>Cache<wbr>Config<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}The cache configs of the accelerated domain.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Certificate<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domaincertificateconfig">Pulumi.<wbr>Ali<wbr>Cloud.<wbr>Cdn.<wbr>Inputs.<wbr>Domain<wbr>Certificate<wbr>Config<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Http<wbr>Header<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainhttpheaderconfig">List&lt;Pulumi.<wbr>Ali<wbr>Cloud.<wbr>Cdn.<wbr>Inputs.<wbr>Domain<wbr>Http<wbr>Header<wbr>Config<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}The http header configs of the accelerated domain.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Optimize<wbr>Enable</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Page Optimize config of the accelerated domain. Valid values are `on` and `off`. Default value is `off`. It can effectively remove the page redundant content, reduce the file size and improve the speed of distribution when this parameter value is `on`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Page404Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainpage404config">Pulumi.<wbr>Ali<wbr>Cloud.<wbr>Cdn.<wbr>Inputs.<wbr>Domain<wbr>Page404Config<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}The error page config of the accelerated domain.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Page<wbr>Compress<wbr>Enable</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Page Compress config of the accelerated domain. Valid values are `on` and `off`. Default value is `off`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Parameter<wbr>Filter<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainparameterfilterconfig">Pulumi.<wbr>Ali<wbr>Cloud.<wbr>Cdn.<wbr>Inputs.<wbr>Domain<wbr>Parameter<wbr>Filter<wbr>Config<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}The parameter filter config of the accelerated domain.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Range<wbr>Enable</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Range Source config of the accelerated domain. Valid values are `on` and `off`. Default value is `off`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Refer<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainreferconfig">Pulumi.<wbr>Ali<wbr>Cloud.<wbr>Cdn.<wbr>Inputs.<wbr>Domain<wbr>Refer<wbr>Config<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}The refer config of the accelerated domain.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scope</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Scope of the accelerated domain. Valid values are `domestic`, `overseas`, `global`. Default value is `domestic`. This parameter's setting is valid Only for the international users and domestic L3 and above users .
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Source<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Source port of the accelerated domain. Valid values are `80` and `443`. Default value is `80`. You must use `80` when the `source_type` is `oss`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_new` configuration `sources` block `port` argument instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Source<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Source type of the accelerated domain. Valid values are `ipaddr`, `domain`, `oss`. You must set this parameter when `cdn_type` value is not `liveStream`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_new` configuration `sources` block `type` argument instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Sources</span>
        <span class="property-indicator"></span>
        <span class="property-type">List&lt;string&gt;</span>
    </dt>
    <dd>{{% md %}}Sources of the accelerated domain. It's a list of domain names or IP address and consists of at most 20 items. You must set this parameter when `cdn_type` value is not `liveStream`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_new` configuration `sources` argument instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Video<wbr>Seek<wbr>Enable</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Video Seek config of the accelerated domain. Valid values are `on` and `off`. Default value is `off`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

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
    <dd>{{% md %}}Cdn type of the accelerated domain. Valid values are `web`, `download`, `video`, `liveStream`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Domain<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the accelerated domain. This name without suffix can have a string of 1 to 63 characters, must contain only alphanumeric characters or "-", and must not begin or end with "-", and "-" must not in the 3th and 4th character positions at the same time. Suffix `.sh` and `.tel` are not supported.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Auth<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainauthconfig">Domain<wbr>Auth<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}The auth config of the accelerated domain.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Block<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Cache<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domaincacheconfig">[]Domain<wbr>Cache<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}The cache configs of the accelerated domain.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Certificate<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domaincertificateconfig">Domain<wbr>Certificate<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Http<wbr>Header<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainhttpheaderconfig">[]Domain<wbr>Http<wbr>Header<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}The http header configs of the accelerated domain.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Optimize<wbr>Enable</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Page Optimize config of the accelerated domain. Valid values are `on` and `off`. Default value is `off`. It can effectively remove the page redundant content, reduce the file size and improve the speed of distribution when this parameter value is `on`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Page404Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainpage404config">Domain<wbr>Page404Config</a></span>
    </dt>
    <dd>{{% md %}}The error page config of the accelerated domain.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Page<wbr>Compress<wbr>Enable</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Page Compress config of the accelerated domain. Valid values are `on` and `off`. Default value is `off`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Parameter<wbr>Filter<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainparameterfilterconfig">Domain<wbr>Parameter<wbr>Filter<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}The parameter filter config of the accelerated domain.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Range<wbr>Enable</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Range Source config of the accelerated domain. Valid values are `on` and `off`. Default value is `off`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Refer<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainreferconfig">Domain<wbr>Refer<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}The refer config of the accelerated domain.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scope</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Scope of the accelerated domain. Valid values are `domestic`, `overseas`, `global`. Default value is `domestic`. This parameter's setting is valid Only for the international users and domestic L3 and above users .
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Source<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Source port of the accelerated domain. Valid values are `80` and `443`. Default value is `80`. You must use `80` when the `source_type` is `oss`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_new` configuration `sources` block `port` argument instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Source<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Source type of the accelerated domain. Valid values are `ipaddr`, `domain`, `oss`. You must set this parameter when `cdn_type` value is not `liveStream`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_new` configuration `sources` block `type` argument instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Sources</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Sources of the accelerated domain. It's a list of domain names or IP address and consists of at most 20 items. You must set this parameter when `cdn_type` value is not `liveStream`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_new` configuration `sources` argument instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Video<wbr>Seek<wbr>Enable</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Video Seek config of the accelerated domain. Valid values are `on` and `off`. Default value is `off`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

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
    <dd>{{% md %}}Cdn type of the accelerated domain. Valid values are `web`, `download`, `video`, `liveStream`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>domain<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the accelerated domain. This name without suffix can have a string of 1 to 63 characters, must contain only alphanumeric characters or "-", and must not begin or end with "-", and "-" must not in the 3th and 4th character positions at the same time. Suffix `.sh` and `.tel` are not supported.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>auth<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainauthconfig">Domain<wbr>Auth<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}The auth config of the accelerated domain.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>block<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>cache<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domaincacheconfig">Domain<wbr>Cache<wbr>Config[]</a></span>
    </dt>
    <dd>{{% md %}}The cache configs of the accelerated domain.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>certificate<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domaincertificateconfig">Domain<wbr>Certificate<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>http<wbr>Header<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainhttpheaderconfig">Domain<wbr>Http<wbr>Header<wbr>Config[]</a></span>
    </dt>
    <dd>{{% md %}}The http header configs of the accelerated domain.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>optimize<wbr>Enable</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Page Optimize config of the accelerated domain. Valid values are `on` and `off`. Default value is `off`. It can effectively remove the page redundant content, reduce the file size and improve the speed of distribution when this parameter value is `on`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>page404Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainpage404config">Domain<wbr>Page404Config</a></span>
    </dt>
    <dd>{{% md %}}The error page config of the accelerated domain.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>page<wbr>Compress<wbr>Enable</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Page Compress config of the accelerated domain. Valid values are `on` and `off`. Default value is `off`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>parameter<wbr>Filter<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainparameterfilterconfig">Domain<wbr>Parameter<wbr>Filter<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}The parameter filter config of the accelerated domain.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>range<wbr>Enable</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Range Source config of the accelerated domain. Valid values are `on` and `off`. Default value is `off`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>refer<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainreferconfig">Domain<wbr>Refer<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}The refer config of the accelerated domain.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>scope</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Scope of the accelerated domain. Valid values are `domestic`, `overseas`, `global`. Default value is `domestic`. This parameter's setting is valid Only for the international users and domestic L3 and above users .
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>source<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Source port of the accelerated domain. Valid values are `80` and `443`. Default value is `80`. You must use `80` when the `source_type` is `oss`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_new` configuration `sources` block `port` argument instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>source<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Source type of the accelerated domain. Valid values are `ipaddr`, `domain`, `oss`. You must set this parameter when `cdn_type` value is not `liveStream`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_new` configuration `sources` block `type` argument instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>sources</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}Sources of the accelerated domain. It's a list of domain names or IP address and consists of at most 20 items. You must set this parameter when `cdn_type` value is not `liveStream`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_new` configuration `sources` argument instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>video<wbr>Seek<wbr>Enable</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Video Seek config of the accelerated domain. Valid values are `on` and `off`. Default value is `off`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

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
    <dd>{{% md %}}Cdn type of the accelerated domain. Valid values are `web`, `download`, `video`, `liveStream`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>domain_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the accelerated domain. This name without suffix can have a string of 1 to 63 characters, must contain only alphanumeric characters or "-", and must not begin or end with "-", and "-" must not in the 3th and 4th character positions at the same time. Suffix `.sh` and `.tel` are not supported.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>auth_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainauthconfig">Dict[Domain<wbr>Auth<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}The auth config of the accelerated domain.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>block_<wbr>ips</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>cache_<wbr>configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domaincacheconfig">List[Domain<wbr>Cache<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}The cache configs of the accelerated domain.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>certificate_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domaincertificateconfig">Dict[Domain<wbr>Certificate<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>http_<wbr>header_<wbr>configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainhttpheaderconfig">List[Domain<wbr>Http<wbr>Header<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}The http header configs of the accelerated domain.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>optimize_<wbr>enable</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Page Optimize config of the accelerated domain. Valid values are `on` and `off`. Default value is `off`. It can effectively remove the page redundant content, reduce the file size and improve the speed of distribution when this parameter value is `on`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>page404_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainpage404config">Dict[Domain<wbr>Page404Config]</a></span>
    </dt>
    <dd>{{% md %}}The error page config of the accelerated domain.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>page_<wbr>compress_<wbr>enable</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Page Compress config of the accelerated domain. Valid values are `on` and `off`. Default value is `off`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>parameter_<wbr>filter_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainparameterfilterconfig">Dict[Domain<wbr>Parameter<wbr>Filter<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}The parameter filter config of the accelerated domain.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>range_<wbr>enable</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Range Source config of the accelerated domain. Valid values are `on` and `off`. Default value is `off`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>refer_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainreferconfig">Dict[Domain<wbr>Refer<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}The refer config of the accelerated domain.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>scope</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Scope of the accelerated domain. Valid values are `domestic`, `overseas`, `global`. Default value is `domestic`. This parameter's setting is valid Only for the international users and domestic L3 and above users .
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>source_<wbr>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Source port of the accelerated domain. Valid values are `80` and `443`. Default value is `80`. You must use `80` when the `source_type` is `oss`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_new` configuration `sources` block `port` argument instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>source_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Source type of the accelerated domain. Valid values are `ipaddr`, `domain`, `oss`. You must set this parameter when `cdn_type` value is not `liveStream`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_new` configuration `sources` block `type` argument instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>sources</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Sources of the accelerated domain. It's a list of domain names or IP address and consists of at most 20 items. You must set this parameter when `cdn_type` value is not `liveStream`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_new` configuration `sources` argument instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>video_<wbr>seek_<wbr>enable</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Video Seek config of the accelerated domain. Valid values are `on` and `off`. Default value is `off`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

</dl>
{{% /choosable %}}










## Look up an Existing Domain Resource

Get an existing Domain resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/cdn/#DomainState">DomainState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/cdn/#Domain">Domain</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>auth_config=None<span class="p">, </span>block_ips=None<span class="p">, </span>cache_configs=None<span class="p">, </span>cdn_type=None<span class="p">, </span>certificate_config=None<span class="p">, </span>domain_name=None<span class="p">, </span>http_header_configs=None<span class="p">, </span>optimize_enable=None<span class="p">, </span>page404_config=None<span class="p">, </span>page_compress_enable=None<span class="p">, </span>parameter_filter_config=None<span class="p">, </span>range_enable=None<span class="p">, </span>refer_config=None<span class="p">, </span>scope=None<span class="p">, </span>source_port=None<span class="p">, </span>source_type=None<span class="p">, </span>sources=None<span class="p">, </span>video_seek_enable=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetDomain<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/cdn?tab=doc#DomainState">DomainState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/cdn?tab=doc#Domain">Domain</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Cdn.Domain.html">Domain</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Cdn.DomainState.html">DomainState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Auth<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainauthconfig">Pulumi.<wbr>Ali<wbr>Cloud.<wbr>Cdn.<wbr>Inputs.<wbr>Domain<wbr>Auth<wbr>Config<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}The auth config of the accelerated domain.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Block<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type">List&lt;string&gt;</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Cache<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domaincacheconfig">List&lt;Pulumi.<wbr>Ali<wbr>Cloud.<wbr>Cdn.<wbr>Inputs.<wbr>Domain<wbr>Cache<wbr>Config<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}The cache configs of the accelerated domain.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cdn<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Cdn type of the accelerated domain. Valid values are `web`, `download`, `video`, `liveStream`.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Certificate<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domaincertificateconfig">Pulumi.<wbr>Ali<wbr>Cloud.<wbr>Cdn.<wbr>Inputs.<wbr>Domain<wbr>Certificate<wbr>Config<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Domain<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the accelerated domain. This name without suffix can have a string of 1 to 63 characters, must contain only alphanumeric characters or "-", and must not begin or end with "-", and "-" must not in the 3th and 4th character positions at the same time. Suffix `.sh` and `.tel` are not supported.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Http<wbr>Header<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainhttpheaderconfig">List&lt;Pulumi.<wbr>Ali<wbr>Cloud.<wbr>Cdn.<wbr>Inputs.<wbr>Domain<wbr>Http<wbr>Header<wbr>Config<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}The http header configs of the accelerated domain.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Optimize<wbr>Enable</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Page Optimize config of the accelerated domain. Valid values are `on` and `off`. Default value is `off`. It can effectively remove the page redundant content, reduce the file size and improve the speed of distribution when this parameter value is `on`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Page404Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainpage404config">Pulumi.<wbr>Ali<wbr>Cloud.<wbr>Cdn.<wbr>Inputs.<wbr>Domain<wbr>Page404Config<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}The error page config of the accelerated domain.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Page<wbr>Compress<wbr>Enable</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Page Compress config of the accelerated domain. Valid values are `on` and `off`. Default value is `off`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Parameter<wbr>Filter<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainparameterfilterconfig">Pulumi.<wbr>Ali<wbr>Cloud.<wbr>Cdn.<wbr>Inputs.<wbr>Domain<wbr>Parameter<wbr>Filter<wbr>Config<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}The parameter filter config of the accelerated domain.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Range<wbr>Enable</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Range Source config of the accelerated domain. Valid values are `on` and `off`. Default value is `off`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Refer<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainreferconfig">Pulumi.<wbr>Ali<wbr>Cloud.<wbr>Cdn.<wbr>Inputs.<wbr>Domain<wbr>Refer<wbr>Config<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}The refer config of the accelerated domain.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scope</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Scope of the accelerated domain. Valid values are `domestic`, `overseas`, `global`. Default value is `domestic`. This parameter's setting is valid Only for the international users and domestic L3 and above users .
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Source<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Source port of the accelerated domain. Valid values are `80` and `443`. Default value is `80`. You must use `80` when the `source_type` is `oss`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_new` configuration `sources` block `port` argument instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Source<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Source type of the accelerated domain. Valid values are `ipaddr`, `domain`, `oss`. You must set this parameter when `cdn_type` value is not `liveStream`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_new` configuration `sources` block `type` argument instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Sources</span>
        <span class="property-indicator"></span>
        <span class="property-type">List&lt;string&gt;</span>
    </dt>
    <dd>{{% md %}}Sources of the accelerated domain. It's a list of domain names or IP address and consists of at most 20 items. You must set this parameter when `cdn_type` value is not `liveStream`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_new` configuration `sources` argument instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Video<wbr>Seek<wbr>Enable</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Video Seek config of the accelerated domain. Valid values are `on` and `off`. Default value is `off`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Auth<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainauthconfig">Domain<wbr>Auth<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}The auth config of the accelerated domain.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Block<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Cache<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domaincacheconfig">[]Domain<wbr>Cache<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}The cache configs of the accelerated domain.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cdn<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Cdn type of the accelerated domain. Valid values are `web`, `download`, `video`, `liveStream`.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Certificate<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domaincertificateconfig">Domain<wbr>Certificate<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Domain<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the accelerated domain. This name without suffix can have a string of 1 to 63 characters, must contain only alphanumeric characters or "-", and must not begin or end with "-", and "-" must not in the 3th and 4th character positions at the same time. Suffix `.sh` and `.tel` are not supported.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Http<wbr>Header<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainhttpheaderconfig">[]Domain<wbr>Http<wbr>Header<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}The http header configs of the accelerated domain.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Optimize<wbr>Enable</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Page Optimize config of the accelerated domain. Valid values are `on` and `off`. Default value is `off`. It can effectively remove the page redundant content, reduce the file size and improve the speed of distribution when this parameter value is `on`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Page404Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainpage404config">Domain<wbr>Page404Config</a></span>
    </dt>
    <dd>{{% md %}}The error page config of the accelerated domain.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Page<wbr>Compress<wbr>Enable</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Page Compress config of the accelerated domain. Valid values are `on` and `off`. Default value is `off`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Parameter<wbr>Filter<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainparameterfilterconfig">Domain<wbr>Parameter<wbr>Filter<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}The parameter filter config of the accelerated domain.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Range<wbr>Enable</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Range Source config of the accelerated domain. Valid values are `on` and `off`. Default value is `off`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Refer<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainreferconfig">Domain<wbr>Refer<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}The refer config of the accelerated domain.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scope</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Scope of the accelerated domain. Valid values are `domestic`, `overseas`, `global`. Default value is `domestic`. This parameter's setting is valid Only for the international users and domestic L3 and above users .
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Source<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Source port of the accelerated domain. Valid values are `80` and `443`. Default value is `80`. You must use `80` when the `source_type` is `oss`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_new` configuration `sources` block `port` argument instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Source<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Source type of the accelerated domain. Valid values are `ipaddr`, `domain`, `oss`. You must set this parameter when `cdn_type` value is not `liveStream`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_new` configuration `sources` block `type` argument instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Sources</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Sources of the accelerated domain. It's a list of domain names or IP address and consists of at most 20 items. You must set this parameter when `cdn_type` value is not `liveStream`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_new` configuration `sources` argument instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Video<wbr>Seek<wbr>Enable</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Video Seek config of the accelerated domain. Valid values are `on` and `off`. Default value is `off`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>auth<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainauthconfig">Domain<wbr>Auth<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}The auth config of the accelerated domain.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>block<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>cache<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domaincacheconfig">Domain<wbr>Cache<wbr>Config[]</a></span>
    </dt>
    <dd>{{% md %}}The cache configs of the accelerated domain.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>cdn<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Cdn type of the accelerated domain. Valid values are `web`, `download`, `video`, `liveStream`.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>certificate<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domaincertificateconfig">Domain<wbr>Certificate<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>domain<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the accelerated domain. This name without suffix can have a string of 1 to 63 characters, must contain only alphanumeric characters or "-", and must not begin or end with "-", and "-" must not in the 3th and 4th character positions at the same time. Suffix `.sh` and `.tel` are not supported.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>http<wbr>Header<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainhttpheaderconfig">Domain<wbr>Http<wbr>Header<wbr>Config[]</a></span>
    </dt>
    <dd>{{% md %}}The http header configs of the accelerated domain.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>optimize<wbr>Enable</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Page Optimize config of the accelerated domain. Valid values are `on` and `off`. Default value is `off`. It can effectively remove the page redundant content, reduce the file size and improve the speed of distribution when this parameter value is `on`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>page404Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainpage404config">Domain<wbr>Page404Config</a></span>
    </dt>
    <dd>{{% md %}}The error page config of the accelerated domain.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>page<wbr>Compress<wbr>Enable</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Page Compress config of the accelerated domain. Valid values are `on` and `off`. Default value is `off`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>parameter<wbr>Filter<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainparameterfilterconfig">Domain<wbr>Parameter<wbr>Filter<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}The parameter filter config of the accelerated domain.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>range<wbr>Enable</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Range Source config of the accelerated domain. Valid values are `on` and `off`. Default value is `off`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>refer<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainreferconfig">Domain<wbr>Refer<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}The refer config of the accelerated domain.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>scope</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Scope of the accelerated domain. Valid values are `domestic`, `overseas`, `global`. Default value is `domestic`. This parameter's setting is valid Only for the international users and domestic L3 and above users .
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>source<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Source port of the accelerated domain. Valid values are `80` and `443`. Default value is `80`. You must use `80` when the `source_type` is `oss`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_new` configuration `sources` block `port` argument instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>source<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Source type of the accelerated domain. Valid values are `ipaddr`, `domain`, `oss`. You must set this parameter when `cdn_type` value is not `liveStream`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_new` configuration `sources` block `type` argument instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>sources</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}Sources of the accelerated domain. It's a list of domain names or IP address and consists of at most 20 items. You must set this parameter when `cdn_type` value is not `liveStream`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_new` configuration `sources` argument instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>video<wbr>Seek<wbr>Enable</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Video Seek config of the accelerated domain. Valid values are `on` and `off`. Default value is `off`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>auth_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainauthconfig">Dict[Domain<wbr>Auth<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}The auth config of the accelerated domain.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>block_<wbr>ips</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>cache_<wbr>configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domaincacheconfig">List[Domain<wbr>Cache<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}The cache configs of the accelerated domain.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>cdn_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Cdn type of the accelerated domain. Valid values are `web`, `download`, `video`, `liveStream`.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>certificate_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domaincertificateconfig">Dict[Domain<wbr>Certificate<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>domain_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the accelerated domain. This name without suffix can have a string of 1 to 63 characters, must contain only alphanumeric characters or "-", and must not begin or end with "-", and "-" must not in the 3th and 4th character positions at the same time. Suffix `.sh` and `.tel` are not supported.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>http_<wbr>header_<wbr>configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainhttpheaderconfig">List[Domain<wbr>Http<wbr>Header<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}The http header configs of the accelerated domain.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>optimize_<wbr>enable</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Page Optimize config of the accelerated domain. Valid values are `on` and `off`. Default value is `off`. It can effectively remove the page redundant content, reduce the file size and improve the speed of distribution when this parameter value is `on`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>page404_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainpage404config">Dict[Domain<wbr>Page404Config]</a></span>
    </dt>
    <dd>{{% md %}}The error page config of the accelerated domain.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>page_<wbr>compress_<wbr>enable</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Page Compress config of the accelerated domain. Valid values are `on` and `off`. Default value is `off`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>parameter_<wbr>filter_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainparameterfilterconfig">Dict[Domain<wbr>Parameter<wbr>Filter<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}The parameter filter config of the accelerated domain.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>range_<wbr>enable</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Range Source config of the accelerated domain. Valid values are `on` and `off`. Default value is `off`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>refer_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#domainreferconfig">Dict[Domain<wbr>Refer<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}The refer config of the accelerated domain.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>scope</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Scope of the accelerated domain. Valid values are `domestic`, `overseas`, `global`. Default value is `domestic`. This parameter's setting is valid Only for the international users and domestic L3 and above users .
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>source_<wbr>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Source port of the accelerated domain. Valid values are `80` and `443`. Default value is `80`. You must use `80` when the `source_type` is `oss`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_new` configuration `sources` block `port` argument instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>source_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Source type of the accelerated domain. Valid values are `ipaddr`, `domain`, `oss`. You must set this parameter when `cdn_type` value is not `liveStream`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_new` configuration `sources` block `type` argument instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>sources</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Sources of the accelerated domain. It's a list of domain names or IP address and consists of at most 20 items. You must set this parameter when `cdn_type` value is not `liveStream`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_new` configuration `sources` argument instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>video_<wbr>seek_<wbr>enable</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Video Seek config of the accelerated domain. Valid values are `on` and `off`. Default value is `off`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.{{% /md %}}</p></dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Domain<wbr>Auth<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/input/#DomainAuthConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/output/#DomainAuthConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/cdn?tab=doc#DomainAuthConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/cdn?tab=doc#DomainAuthConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Auth<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Auth type of the auth config. Valid values are  `no_auth`, `type_a`, `type_b` and `type_c`. Default value is `no_auth`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Master<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Master authentication key of the auth config. This parameter can have a string of 6 to 32 characters and must contain only alphanumeric characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Slave<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Slave authentication key of the auth config. This parameter can have a string of 6 to 32 characters and must contain only alphanumeric characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Authentication cache time of the auth config. Default value is `1800`. It's value is valid only when the `auth_type` is `type_b` or `type_c`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Auth<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Auth type of the auth config. Valid values are  `no_auth`, `type_a`, `type_b` and `type_c`. Default value is `no_auth`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Master<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Master authentication key of the auth config. This parameter can have a string of 6 to 32 characters and must contain only alphanumeric characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Slave<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Slave authentication key of the auth config. This parameter can have a string of 6 to 32 characters and must contain only alphanumeric characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Authentication cache time of the auth config. Default value is `1800`. It's value is valid only when the `auth_type` is `type_b` or `type_c`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>auth<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Auth type of the auth config. Valid values are  `no_auth`, `type_a`, `type_b` and `type_c`. Default value is `no_auth`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>master<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Master authentication key of the auth config. This parameter can have a string of 6 to 32 characters and must contain only alphanumeric characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>slave<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Slave authentication key of the auth config. This parameter can have a string of 6 to 32 characters and must contain only alphanumeric characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Authentication cache time of the auth config. Default value is `1800`. It's value is valid only when the `auth_type` is `type_b` or `type_c`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>auth_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Auth type of the auth config. Valid values are  `no_auth`, `type_a`, `type_b` and `type_c`. Default value is `no_auth`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>master<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Master authentication key of the auth config. This parameter can have a string of 6 to 32 characters and must contain only alphanumeric characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>slave<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Slave authentication key of the auth config. This parameter can have a string of 6 to 32 characters and must contain only alphanumeric characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Authentication cache time of the auth config. Default value is `1800`. It's value is valid only when the `auth_type` is `type_b` or `type_c`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Domain<wbr>Cache<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/input/#DomainCacheConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/output/#DomainCacheConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/cdn?tab=doc#DomainCacheConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/cdn?tab=doc#DomainCacheConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Cache<wbr>Content</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Cache content of the cache config. It's value is a path string when the `cache_type` is `path`. When the `cache_type` is `suffix`, it's value is a string which contains multiple file suffixes separated by commas.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Cache<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Cache type of the cache config. Valid values are `suffix` and `path`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Cache time of the cache config.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cache<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Weight</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Weight of the cache config. This parameter's value is between 1 and 99. Default value is `1`. The higher the value, the higher the priority.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Cache<wbr>Content</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Cache content of the cache config. It's value is a path string when the `cache_type` is `path`. When the `cache_type` is `suffix`, it's value is a string which contains multiple file suffixes separated by commas.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Cache<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Cache type of the cache config. Valid values are `suffix` and `path`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Cache time of the cache config.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cache<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Weight</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Weight of the cache config. This parameter's value is between 1 and 99. Default value is `1`. The higher the value, the higher the priority.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>cache<wbr>Content</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Cache content of the cache config. It's value is a path string when the `cache_type` is `path`. When the `cache_type` is `suffix`, it's value is a string which contains multiple file suffixes separated by commas.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>cache<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Cache type of the cache config. Valid values are `suffix` and `path`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Cache time of the cache config.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cache<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>weight</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Weight of the cache config. This parameter's value is between 1 and 99. Default value is `1`. The higher the value, the higher the priority.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>cache<wbr>Content</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Cache content of the cache config. It's value is a path string when the `cache_type` is `path`. When the `cache_type` is `suffix`, it's value is a string which contains multiple file suffixes separated by commas.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>cache<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Cache type of the cache config. Valid values are `suffix` and `path`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Cache time of the cache config.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cache<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>weight</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Weight of the cache config. This parameter's value is between 1 and 99. Default value is `1`. The higher the value, the higher the priority.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Domain<wbr>Certificate<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/input/#DomainCertificateConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/output/#DomainCertificateConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/cdn?tab=doc#DomainCertificateConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/cdn?tab=doc#DomainCertificateConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Private<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The SSL private key. This is required if `server_certificate_status` is `on`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Server<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The SSL server certificate string. This is required if `server_certificate_status` is `on`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Server<wbr>Certificate<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}This parameter indicates whether or not enable https. Valid values are `on` and `off`. Default value is `on`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Private<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The SSL private key. This is required if `server_certificate_status` is `on`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Server<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The SSL server certificate string. This is required if `server_certificate_status` is `on`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Server<wbr>Certificate<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}This parameter indicates whether or not enable https. Valid values are `on` and `off`. Default value is `on`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>private<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The SSL private key. This is required if `server_certificate_status` is `on`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>server<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The SSL server certificate string. This is required if `server_certificate_status` is `on`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>server<wbr>Certificate<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}This parameter indicates whether or not enable https. Valid values are `on` and `off`. Default value is `on`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

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





<h4>Domain<wbr>Http<wbr>Header<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/input/#DomainHttpHeaderConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/output/#DomainHttpHeaderConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/cdn?tab=doc#DomainHttpHeaderConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/cdn?tab=doc#DomainHttpHeaderConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Header<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Header key of the http header. Valid values are `Content-Type`, `Cache-Control`, `Content-Disposition`, `Content-Language`，`Expires`, `Access-Control-Allow-Origin`, `Access-Control-Allow-Methods` and `Access-Control-Max-Age`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Header<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Header value of the http header.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Header<wbr>Id</span>
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
        <span>Header<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Header key of the http header. Valid values are `Content-Type`, `Cache-Control`, `Content-Disposition`, `Content-Language`，`Expires`, `Access-Control-Allow-Origin`, `Access-Control-Allow-Methods` and `Access-Control-Max-Age`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Header<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Header value of the http header.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Header<wbr>Id</span>
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
        <span>header<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Header key of the http header. Valid values are `Content-Type`, `Cache-Control`, `Content-Disposition`, `Content-Language`，`Expires`, `Access-Control-Allow-Origin`, `Access-Control-Allow-Methods` and `Access-Control-Max-Age`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>header<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Header value of the http header.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>header<wbr>Id</span>
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
        <span>header<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Header key of the http header. Valid values are `Content-Type`, `Cache-Control`, `Content-Disposition`, `Content-Language`，`Expires`, `Access-Control-Allow-Origin`, `Access-Control-Allow-Methods` and `Access-Control-Max-Age`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>header<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Header value of the http header.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>header<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Domain<wbr>Page404Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/input/#DomainPage404Config">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/output/#DomainPage404Config">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/cdn?tab=doc#DomainPage404ConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/cdn?tab=doc#DomainPage404ConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Custom<wbr>Page<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Custom page url of the error page. It must be the full path under the accelerated domain name. It's value must be `http://promotion.alicdn.com/help/oss/error.html` when `page_type` value is `charity` and It can not be set when `page_type` value is `default`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Error<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Page<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Page type of the error page. Valid values are `default`, `charity`, `other`. Default value is `default`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Custom<wbr>Page<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Custom page url of the error page. It must be the full path under the accelerated domain name. It's value must be `http://promotion.alicdn.com/help/oss/error.html` when `page_type` value is `charity` and It can not be set when `page_type` value is `default`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Error<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Page<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Page type of the error page. Valid values are `default`, `charity`, `other`. Default value is `default`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>custom<wbr>Page<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Custom page url of the error page. It must be the full path under the accelerated domain name. It's value must be `http://promotion.alicdn.com/help/oss/error.html` when `page_type` value is `charity` and It can not be set when `page_type` value is `default`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>error<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>page<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Page type of the error page. Valid values are `default`, `charity`, `other`. Default value is `default`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>custom<wbr>Page<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Custom page url of the error page. It must be the full path under the accelerated domain name. It's value must be `http://promotion.alicdn.com/help/oss/error.html` when `page_type` value is `charity` and It can not be set when `page_type` value is `default`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>error<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>page<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Page type of the error page. Valid values are `default`, `charity`, `other`. Default value is `default`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Domain<wbr>Parameter<wbr>Filter<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/input/#DomainParameterFilterConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/output/#DomainParameterFilterConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/cdn?tab=doc#DomainParameterFilterConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/cdn?tab=doc#DomainParameterFilterConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Enable</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}This parameter indicates whether or not the `parameter_filter_config` is enable. Valid values are `on` and `off`. Default value is `off`.  
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hash<wbr>Key<wbr>Args</span>
        <span class="property-indicator"></span>
        <span class="property-type">List&lt;string&gt;</span>
    </dt>
    <dd>{{% md %}}Reserved parameters of `parameter_filter_config`. It's a list of string and consists of at most 10 items.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Enable</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}This parameter indicates whether or not the `parameter_filter_config` is enable. Valid values are `on` and `off`. Default value is `off`.  
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hash<wbr>Key<wbr>Args</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Reserved parameters of `parameter_filter_config`. It's a list of string and consists of at most 10 items.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>enable</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}This parameter indicates whether or not the `parameter_filter_config` is enable. Valid values are `on` and `off`. Default value is `off`.  
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hash<wbr>Key<wbr>Args</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}Reserved parameters of `parameter_filter_config`. It's a list of string and consists of at most 10 items.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>enable</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}This parameter indicates whether or not the `parameter_filter_config` is enable. Valid values are `on` and `off`. Default value is `off`.  
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hash<wbr>Key<wbr>Args</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Reserved parameters of `parameter_filter_config`. It's a list of string and consists of at most 10 items.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Domain<wbr>Refer<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/input/#DomainReferConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/output/#DomainReferConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/cdn?tab=doc#DomainReferConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/cdn?tab=doc#DomainReferConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Refer<wbr>Lists</span>
        <span class="property-indicator"></span>
        <span class="property-type">List&lt;string&gt;</span>
    </dt>
    <dd>{{% md %}}A list of domain names of the refer config.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Empty</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}This parameter indicates whether or not to allow empty refer access. Valid values are `on` and `off`. Default value is `on`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Refer<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Refer type of the refer config. Valid values are `block` and `allow`. Default value is `block`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Refer<wbr>Lists</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of domain names of the refer config.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Empty</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}This parameter indicates whether or not to allow empty refer access. Valid values are `on` and `off`. Default value is `on`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Refer<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Refer type of the refer config. Valid values are `block` and `allow`. Default value is `block`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>refer<wbr>Lists</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}A list of domain names of the refer config.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Empty</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}This parameter indicates whether or not to allow empty refer access. Valid values are `on` and `off`. Default value is `on`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>refer<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Refer type of the refer config. Valid values are `block` and `allow`. Default value is `block`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>refer<wbr>Lists</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of domain names of the refer config.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Empty</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}This parameter indicates whether or not to allow empty refer access. Valid values are `on` and `off`. Default value is `on`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>refer<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Refer type of the refer config. Valid values are `block` and `allow`. Default value is `block`.
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

