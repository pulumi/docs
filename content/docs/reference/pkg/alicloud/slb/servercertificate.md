
---
title: "ServerCertificate"
block_external_search_index: true
---



A Load Balancer Server Certificate is an ssl Certificate used by the listener of the protocol https.

For information about slb and how to use it, see [What is Server Load Balancer](https://www.alibabacloud.com/help/doc-detail/27539.htm).

For information about Server Certificate and how to use it, see [Configure Server Certificate](https://www.alibabacloud.com/help/doc-detail/85968.htm).

> This content is derived from https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/slb_server_certificate.html.markdown.



## Create a ServerCertificate Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/slb/#ServerCertificate">ServerCertificate</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/slb/#ServerCertificateArgs">ServerCertificateArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">ServerCertificate</span><span class="p">(resource_name, opts=None, </span>alicloud_certifacte_id=None<span class="p">, </span>alicloud_certifacte_name=None<span class="p">, </span>alicloud_certificate_id=None<span class="p">, </span>alicloud_certificate_name=None<span class="p">, </span>alicloud_certificate_region_id=None<span class="p">, </span>name=None<span class="p">, </span>private_key=None<span class="p">, </span>resource_group_id=None<span class="p">, </span>server_certificate=None<span class="p">, </span>tags=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewServerCertificate<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/slb?tab=doc#ServerCertificateArgs">ServerCertificateArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/slb?tab=doc#ServerCertificate">ServerCertificate</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Slb.ServerCertificate.html">ServerCertificate</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Slb.ServerCertificateArgs.html">ServerCertificateArgs</a></span>? <span class="nx">args = null<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Alicloud<wbr>Certifacte<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Field &#39;alicloud_certifacte_id&#39; has been deprecated from provider version 1.68.0. Use &#39;alicloud_certificate_id&#39; replaces it.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Alicloud<wbr>Certifacte<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Field &#39;alicloud_certifacte_name&#39; has been deprecated from provider version 1.68.0. Use &#39;alicloud_certificate_name&#39; replaces it.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Alicloud<wbr>Certificate<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}an id of server certificate ssued/proxied by alibaba cloud. but it is not supported on the international site of alibaba cloud now.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Alicloud<wbr>Certificate<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}the name of the certificate specified by `alicloud_certificate_id`.but it is not supported on the international site of alibaba cloud now.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Alicloud<wbr>Certificate<wbr>Region<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}the region of the certificate specified by `alicloud_certificate_id`. but it is not supported on the international site of alibaba cloud now.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the Server Certificate.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Private<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}the content of privat key of the ssl certificate specified by `server_certificate`. where `alicloud_certificate_id` is null, it is required, otherwise it is ignored.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Id of resource group which the slb server certificate belongs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}the content of the ssl certificate. where `alicloud_certificate_id` is null, it is required, otherwise it is ignored.
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

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Alicloud<wbr>Certifacte<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Field &#39;alicloud_certifacte_id&#39; has been deprecated from provider version 1.68.0. Use &#39;alicloud_certificate_id&#39; replaces it.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Alicloud<wbr>Certifacte<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Field &#39;alicloud_certifacte_name&#39; has been deprecated from provider version 1.68.0. Use &#39;alicloud_certificate_name&#39; replaces it.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Alicloud<wbr>Certificate<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}an id of server certificate ssued/proxied by alibaba cloud. but it is not supported on the international site of alibaba cloud now.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Alicloud<wbr>Certificate<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}the name of the certificate specified by `alicloud_certificate_id`.but it is not supported on the international site of alibaba cloud now.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Alicloud<wbr>Certificate<wbr>Region<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}the region of the certificate specified by `alicloud_certificate_id`. but it is not supported on the international site of alibaba cloud now.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of the Server Certificate.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Private<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}the content of privat key of the ssl certificate specified by `server_certificate`. where `alicloud_certificate_id` is null, it is required, otherwise it is ignored.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Id of resource group which the slb server certificate belongs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Server<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}the content of the ssl certificate. where `alicloud_certificate_id` is null, it is required, otherwise it is ignored.
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

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>alicloud<wbr>Certifacte<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Field &#39;alicloud_certifacte_id&#39; has been deprecated from provider version 1.68.0. Use &#39;alicloud_certificate_id&#39; replaces it.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>alicloud<wbr>Certifacte<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Field &#39;alicloud_certifacte_name&#39; has been deprecated from provider version 1.68.0. Use &#39;alicloud_certificate_name&#39; replaces it.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>alicloud<wbr>Certificate<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}an id of server certificate ssued/proxied by alibaba cloud. but it is not supported on the international site of alibaba cloud now.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>alicloud<wbr>Certificate<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}the name of the certificate specified by `alicloud_certificate_id`.but it is not supported on the international site of alibaba cloud now.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>alicloud<wbr>Certificate<wbr>Region<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}the region of the certificate specified by `alicloud_certificate_id`. but it is not supported on the international site of alibaba cloud now.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the Server Certificate.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>private<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}the content of privat key of the ssl certificate specified by `server_certificate`. where `alicloud_certificate_id` is null, it is required, otherwise it is ignored.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Id of resource group which the slb server certificate belongs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>server<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}the content of the ssl certificate. where `alicloud_certificate_id` is null, it is required, otherwise it is ignored.
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

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>alicloud_<wbr>certifacte_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Field &#39;alicloud_certifacte_id&#39; has been deprecated from provider version 1.68.0. Use &#39;alicloud_certificate_id&#39; replaces it.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>alicloud_<wbr>certifacte_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Field &#39;alicloud_certifacte_name&#39; has been deprecated from provider version 1.68.0. Use &#39;alicloud_certificate_name&#39; replaces it.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>alicloud_<wbr>certificate_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}an id of server certificate ssued/proxied by alibaba cloud. but it is not supported on the international site of alibaba cloud now.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>alicloud_<wbr>certificate_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}the name of the certificate specified by `alicloud_certificate_id`.but it is not supported on the international site of alibaba cloud now.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>alicloud_<wbr>certificate_<wbr>region_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}the region of the certificate specified by `alicloud_certificate_id`. but it is not supported on the international site of alibaba cloud now.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the Server Certificate.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>private_<wbr>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}the content of privat key of the ssl certificate specified by `server_certificate`. where `alicloud_certificate_id` is null, it is required, otherwise it is ignored.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource_<wbr>group_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Id of resource group which the slb server certificate belongs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>server_<wbr>certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}the content of the ssl certificate. where `alicloud_certificate_id` is null, it is required, otherwise it is ignored.
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







## ServerCertificate Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Alicloud<wbr>Certifacte<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Field &#39;alicloud_certifacte_id&#39; has been deprecated from provider version 1.68.0. Use &#39;alicloud_certificate_id&#39; replaces it.{{% /md %}}</p></dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Alicloud<wbr>Certifacte<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Field &#39;alicloud_certifacte_name&#39; has been deprecated from provider version 1.68.0. Use &#39;alicloud_certificate_name&#39; replaces it.{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>Alicloud<wbr>Certificate<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}an id of server certificate ssued/proxied by alibaba cloud. but it is not supported on the international site of alibaba cloud now.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Alicloud<wbr>Certificate<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}the name of the certificate specified by `alicloud_certificate_id`.but it is not supported on the international site of alibaba cloud now.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Alicloud<wbr>Certificate<wbr>Region<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}the region of the certificate specified by `alicloud_certificate_id`. but it is not supported on the international site of alibaba cloud now.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the Server Certificate.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Private<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}the content of privat key of the ssl certificate specified by `server_certificate`. where `alicloud_certificate_id` is null, it is required, otherwise it is ignored.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Resource<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Id of resource group which the slb server certificate belongs.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}the content of the ssl certificate. where `alicloud_certificate_id` is null, it is required, otherwise it is ignored.
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

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Alicloud<wbr>Certifacte<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Field &#39;alicloud_certifacte_id&#39; has been deprecated from provider version 1.68.0. Use &#39;alicloud_certificate_id&#39; replaces it.{{% /md %}}</p></dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Alicloud<wbr>Certifacte<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Field &#39;alicloud_certifacte_name&#39; has been deprecated from provider version 1.68.0. Use &#39;alicloud_certificate_name&#39; replaces it.{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>Alicloud<wbr>Certificate<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}an id of server certificate ssued/proxied by alibaba cloud. but it is not supported on the international site of alibaba cloud now.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Alicloud<wbr>Certificate<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}the name of the certificate specified by `alicloud_certificate_id`.but it is not supported on the international site of alibaba cloud now.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Alicloud<wbr>Certificate<wbr>Region<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}the region of the certificate specified by `alicloud_certificate_id`. but it is not supported on the international site of alibaba cloud now.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the Server Certificate.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Private<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}the content of privat key of the ssl certificate specified by `server_certificate`. where `alicloud_certificate_id` is null, it is required, otherwise it is ignored.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Resource<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Id of resource group which the slb server certificate belongs.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Server<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}the content of the ssl certificate. where `alicloud_certificate_id` is null, it is required, otherwise it is ignored.
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

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>alicloud<wbr>Certifacte<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Field &#39;alicloud_certifacte_id&#39; has been deprecated from provider version 1.68.0. Use &#39;alicloud_certificate_id&#39; replaces it.{{% /md %}}</p></dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>alicloud<wbr>Certifacte<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Field &#39;alicloud_certifacte_name&#39; has been deprecated from provider version 1.68.0. Use &#39;alicloud_certificate_name&#39; replaces it.{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>alicloud<wbr>Certificate<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}an id of server certificate ssued/proxied by alibaba cloud. but it is not supported on the international site of alibaba cloud now.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>alicloud<wbr>Certificate<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}the name of the certificate specified by `alicloud_certificate_id`.but it is not supported on the international site of alibaba cloud now.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>alicloud<wbr>Certificate<wbr>Region<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}the region of the certificate specified by `alicloud_certificate_id`. but it is not supported on the international site of alibaba cloud now.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the Server Certificate.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>private<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}the content of privat key of the ssl certificate specified by `server_certificate`. where `alicloud_certificate_id` is null, it is required, otherwise it is ignored.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>resource<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Id of resource group which the slb server certificate belongs.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>server<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}the content of the ssl certificate. where `alicloud_certificate_id` is null, it is required, otherwise it is ignored.
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

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>alicloud_<wbr>certifacte_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Field &#39;alicloud_certifacte_id&#39; has been deprecated from provider version 1.68.0. Use &#39;alicloud_certificate_id&#39; replaces it.{{% /md %}}</p></dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>alicloud_<wbr>certifacte_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Field &#39;alicloud_certifacte_name&#39; has been deprecated from provider version 1.68.0. Use &#39;alicloud_certificate_name&#39; replaces it.{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>alicloud_<wbr>certificate_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}an id of server certificate ssued/proxied by alibaba cloud. but it is not supported on the international site of alibaba cloud now.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>alicloud_<wbr>certificate_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}the name of the certificate specified by `alicloud_certificate_id`.but it is not supported on the international site of alibaba cloud now.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>alicloud_<wbr>certificate_<wbr>region_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}the region of the certificate specified by `alicloud_certificate_id`. but it is not supported on the international site of alibaba cloud now.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the Server Certificate.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>private_<wbr>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}the content of privat key of the ssl certificate specified by `server_certificate`. where `alicloud_certificate_id` is null, it is required, otherwise it is ignored.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>resource_<wbr>group_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Id of resource group which the slb server certificate belongs.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>server_<wbr>certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}the content of the ssl certificate. where `alicloud_certificate_id` is null, it is required, otherwise it is ignored.
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








## Look up an Existing ServerCertificate Resource

Get an existing ServerCertificate resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/slb/#ServerCertificateState">ServerCertificateState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/slb/#ServerCertificate">ServerCertificate</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>alicloud_certifacte_id=None<span class="p">, </span>alicloud_certifacte_name=None<span class="p">, </span>alicloud_certificate_id=None<span class="p">, </span>alicloud_certificate_name=None<span class="p">, </span>alicloud_certificate_region_id=None<span class="p">, </span>name=None<span class="p">, </span>private_key=None<span class="p">, </span>resource_group_id=None<span class="p">, </span>server_certificate=None<span class="p">, </span>tags=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetServerCertificate<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/slb?tab=doc#ServerCertificateState">ServerCertificateState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/slb?tab=doc#ServerCertificate">ServerCertificate</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Slb.ServerCertificate.html">ServerCertificate</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Slb.ServerCertificateState.html">ServerCertificateState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Alicloud<wbr>Certifacte<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Field &#39;alicloud_certifacte_id&#39; has been deprecated from provider version 1.68.0. Use &#39;alicloud_certificate_id&#39; replaces it.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Alicloud<wbr>Certifacte<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Field &#39;alicloud_certifacte_name&#39; has been deprecated from provider version 1.68.0. Use &#39;alicloud_certificate_name&#39; replaces it.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Alicloud<wbr>Certificate<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}an id of server certificate ssued/proxied by alibaba cloud. but it is not supported on the international site of alibaba cloud now.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Alicloud<wbr>Certificate<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}the name of the certificate specified by `alicloud_certificate_id`.but it is not supported on the international site of alibaba cloud now.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Alicloud<wbr>Certificate<wbr>Region<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}the region of the certificate specified by `alicloud_certificate_id`. but it is not supported on the international site of alibaba cloud now.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the Server Certificate.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Private<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}the content of privat key of the ssl certificate specified by `server_certificate`. where `alicloud_certificate_id` is null, it is required, otherwise it is ignored.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Id of resource group which the slb server certificate belongs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}the content of the ssl certificate. where `alicloud_certificate_id` is null, it is required, otherwise it is ignored.
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

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Alicloud<wbr>Certifacte<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Field &#39;alicloud_certifacte_id&#39; has been deprecated from provider version 1.68.0. Use &#39;alicloud_certificate_id&#39; replaces it.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Alicloud<wbr>Certifacte<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Field &#39;alicloud_certifacte_name&#39; has been deprecated from provider version 1.68.0. Use &#39;alicloud_certificate_name&#39; replaces it.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Alicloud<wbr>Certificate<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}an id of server certificate ssued/proxied by alibaba cloud. but it is not supported on the international site of alibaba cloud now.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Alicloud<wbr>Certificate<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}the name of the certificate specified by `alicloud_certificate_id`.but it is not supported on the international site of alibaba cloud now.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Alicloud<wbr>Certificate<wbr>Region<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}the region of the certificate specified by `alicloud_certificate_id`. but it is not supported on the international site of alibaba cloud now.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of the Server Certificate.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Private<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}the content of privat key of the ssl certificate specified by `server_certificate`. where `alicloud_certificate_id` is null, it is required, otherwise it is ignored.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Id of resource group which the slb server certificate belongs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Server<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}the content of the ssl certificate. where `alicloud_certificate_id` is null, it is required, otherwise it is ignored.
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

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>alicloud<wbr>Certifacte<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Field &#39;alicloud_certifacte_id&#39; has been deprecated from provider version 1.68.0. Use &#39;alicloud_certificate_id&#39; replaces it.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>alicloud<wbr>Certifacte<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Field &#39;alicloud_certifacte_name&#39; has been deprecated from provider version 1.68.0. Use &#39;alicloud_certificate_name&#39; replaces it.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>alicloud<wbr>Certificate<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}an id of server certificate ssued/proxied by alibaba cloud. but it is not supported on the international site of alibaba cloud now.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>alicloud<wbr>Certificate<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}the name of the certificate specified by `alicloud_certificate_id`.but it is not supported on the international site of alibaba cloud now.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>alicloud<wbr>Certificate<wbr>Region<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}the region of the certificate specified by `alicloud_certificate_id`. but it is not supported on the international site of alibaba cloud now.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the Server Certificate.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>private<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}the content of privat key of the ssl certificate specified by `server_certificate`. where `alicloud_certificate_id` is null, it is required, otherwise it is ignored.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Id of resource group which the slb server certificate belongs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>server<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}the content of the ssl certificate. where `alicloud_certificate_id` is null, it is required, otherwise it is ignored.
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

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>alicloud_<wbr>certifacte_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Field &#39;alicloud_certifacte_id&#39; has been deprecated from provider version 1.68.0. Use &#39;alicloud_certificate_id&#39; replaces it.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>alicloud_<wbr>certifacte_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Field &#39;alicloud_certifacte_name&#39; has been deprecated from provider version 1.68.0. Use &#39;alicloud_certificate_name&#39; replaces it.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>alicloud_<wbr>certificate_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}an id of server certificate ssued/proxied by alibaba cloud. but it is not supported on the international site of alibaba cloud now.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>alicloud_<wbr>certificate_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}the name of the certificate specified by `alicloud_certificate_id`.but it is not supported on the international site of alibaba cloud now.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>alicloud_<wbr>certificate_<wbr>region_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}the region of the certificate specified by `alicloud_certificate_id`. but it is not supported on the international site of alibaba cloud now.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the Server Certificate.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>private_<wbr>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}the content of privat key of the ssl certificate specified by `server_certificate`. where `alicloud_certificate_id` is null, it is required, otherwise it is ignored.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource_<wbr>group_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Id of resource group which the slb server certificate belongs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>server_<wbr>certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}the content of the ssl certificate. where `alicloud_certificate_id` is null, it is required, otherwise it is ignored.
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











<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-alicloud">https://github.com/pulumi/pulumi-alicloud</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    
</dl>

