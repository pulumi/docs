
---
title: "LoadBalancerMonitor"
block_external_search_index: true
---



If you're using Cloudflare's Load Balancing to load-balance across multiple origin servers or data centers, you configure one of these Monitors to actively check the availability of those servers over HTTP(S) or TCP.

> This content is derived from https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/load_balancer_monitor.html.markdown.



## Create a LoadBalancerMonitor Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/cloudflare/#LoadBalancerMonitor">LoadBalancerMonitor</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/cloudflare/#LoadBalancerMonitorArgs">LoadBalancerMonitorArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">LoadBalancerMonitor</span><span class="p">(resource_name, opts=None, </span>allow_insecure=None<span class="p">, </span>description=None<span class="p">, </span>expected_body=None<span class="p">, </span>expected_codes=None<span class="p">, </span>follow_redirects=None<span class="p">, </span>headers=None<span class="p">, </span>interval=None<span class="p">, </span>method=None<span class="p">, </span>path=None<span class="p">, </span>port=None<span class="p">, </span>retries=None<span class="p">, </span>timeout=None<span class="p">, </span>type=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewLoadBalancerMonitor<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-cloudflare/sdk/go/cloudflare/?tab=doc#LoadBalancerMonitorArgs">LoadBalancerMonitorArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-cloudflare/sdk/go/cloudflare/?tab=doc#LoadBalancerMonitor">LoadBalancerMonitor</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Cloudflare/Pulumi.Cloudflare..LoadBalancerMonitor.html">LoadBalancerMonitor</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Cloudflare/Pulumi.Cloudflare.LoadBalancerMonitorArgs.html">LoadBalancerMonitorArgs</a></span>? <span class="nx">args = null<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Allow<wbr>Insecure</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Do not validate the certificate when monitor use HTTPS. Only valid if `type` is "http" or "https".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Free text description.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Expected<wbr>Body</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A case-insensitive sub-string to look for in the response body. If this string is not found, the origin will be marked as unhealthy. Only valid if `type` is "http" or "https". Default: "".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Expected<wbr>Codes</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The expected HTTP response code or code range of the health check. Eg `2xx`. Only valid and required if `type` is "http" or "https".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Follow<wbr>Redirects</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Follow redirects if returned by the origin. Only valid if `type` is "http" or "https".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#loadbalancermonitorheader">List&lt;Load<wbr>Balancer<wbr>Monitor<wbr>Header<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}The header name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Interval</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The interval between each health check. Shorter intervals may improve failover time, but will increase load on the origins as we check from multiple locations. Default: 60.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Method</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The method to use for the health check. Valid values are any valid HTTP verb if `type` is "http" or "https", or `connection_established` if `type` is "tcp". Default: "GET" if `type` is "http" or "https", or "connection_established" if `type` is "tcp" .
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The endpoint path to health check against. Default: "/". Only valid if `type` is "http" or "https".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Retries</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The number of retries to attempt in case of a timeout before marking the origin as unhealthy. Retries are attempted immediately. Default: 2.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The timeout (in seconds) before marking the health check as failed. Default: 5.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The protocol to use for the healthcheck. Currently supported protocols are 'HTTP', 'HTTPS' and 'TCP'. Default: "http".
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Insecure</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Do not validate the certificate when monitor use HTTPS. Only valid if `type` is "http" or "https".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Free text description.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Expected<wbr>Body</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A case-insensitive sub-string to look for in the response body. If this string is not found, the origin will be marked as unhealthy. Only valid if `type` is "http" or "https". Default: "".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Expected<wbr>Codes</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The expected HTTP response code or code range of the health check. Eg `2xx`. Only valid and required if `type` is "http" or "https".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Follow<wbr>Redirects</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Follow redirects if returned by the origin. Only valid if `type` is "http" or "https".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#loadbalancermonitorheader">[]Load<wbr>Balancer<wbr>Monitor<wbr>Header</a></span>
    </dt>
    <dd>{{% md %}}The header name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Interval</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The interval between each health check. Shorter intervals may improve failover time, but will increase load on the origins as we check from multiple locations. Default: 60.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Method</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The method to use for the health check. Valid values are any valid HTTP verb if `type` is "http" or "https", or `connection_established` if `type` is "tcp". Default: "GET" if `type` is "http" or "https", or "connection_established" if `type` is "tcp" .
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The endpoint path to health check against. Default: "/". Only valid if `type` is "http" or "https".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Retries</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The number of retries to attempt in case of a timeout before marking the origin as unhealthy. Retries are attempted immediately. Default: 2.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The timeout (in seconds) before marking the health check as failed. Default: 5.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The protocol to use for the healthcheck. Currently supported protocols are 'HTTP', 'HTTPS' and 'TCP'. Default: "http".
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Insecure</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Do not validate the certificate when monitor use HTTPS. Only valid if `type` is "http" or "https".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Free text description.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>expected<wbr>Body</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A case-insensitive sub-string to look for in the response body. If this string is not found, the origin will be marked as unhealthy. Only valid if `type` is "http" or "https". Default: "".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>expected<wbr>Codes</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The expected HTTP response code or code range of the health check. Eg `2xx`. Only valid and required if `type` is "http" or "https".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>follow<wbr>Redirects</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Follow redirects if returned by the origin. Only valid if `type` is "http" or "https".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>headers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#loadbalancermonitorheader">Load<wbr>Balancer<wbr>Monitor<wbr>Header[]?</a></span>
    </dt>
    <dd>{{% md %}}The header name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>interval</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The interval between each health check. Shorter intervals may improve failover time, but will increase load on the origins as we check from multiple locations. Default: 60.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>method</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The method to use for the health check. Valid values are any valid HTTP verb if `type` is "http" or "https", or `connection_established` if `type` is "tcp". Default: "GET" if `type` is "http" or "https", or "connection_established" if `type` is "tcp" .
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The endpoint path to health check against. Default: "/". Only valid if `type` is "http" or "https".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>retries</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The number of retries to attempt in case of a timeout before marking the origin as unhealthy. Retries are attempted immediately. Default: 2.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The timeout (in seconds) before marking the health check as failed. Default: 5.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The protocol to use for the healthcheck. Currently supported protocols are 'HTTP', 'HTTPS' and 'TCP'. Default: "http".
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>allow_<wbr>insecure</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Do not validate the certificate when monitor use HTTPS. Only valid if `type` is "http" or "https".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Free text description.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>expected_<wbr>body</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A case-insensitive sub-string to look for in the response body. If this string is not found, the origin will be marked as unhealthy. Only valid if `type` is "http" or "https". Default: "".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>expected_<wbr>codes</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The expected HTTP response code or code range of the health check. Eg `2xx`. Only valid and required if `type` is "http" or "https".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>follow_<wbr>redirects</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Follow redirects if returned by the origin. Only valid if `type` is "http" or "https".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>headers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#loadbalancermonitorheader">List[Load<wbr>Balancer<wbr>Monitor<wbr>Header]</a></span>
    </dt>
    <dd>{{% md %}}The header name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>interval</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The interval between each health check. Shorter intervals may improve failover time, but will increase load on the origins as we check from multiple locations. Default: 60.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>method</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The method to use for the health check. Valid values are any valid HTTP verb if `type` is "http" or "https", or `connection_established` if `type` is "tcp". Default: "GET" if `type` is "http" or "https", or "connection_established" if `type` is "tcp" .
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>path</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The endpoint path to health check against. Default: "/". Only valid if `type` is "http" or "https".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>retries</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The number of retries to attempt in case of a timeout before marking the origin as unhealthy. Retries are attempted immediately. Default: 2.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The timeout (in seconds) before marking the health check as failed. Default: 5.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The protocol to use for the healthcheck. Currently supported protocols are 'HTTP', 'HTTPS' and 'TCP'. Default: "http".
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## LoadBalancerMonitor Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Allow<wbr>Insecure</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Do not validate the certificate when monitor use HTTPS. Only valid if `type` is "http" or "https".
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Created<wbr>On</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The RFC3339 timestamp of when the load balancer monitor was created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Free text description.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Expected<wbr>Body</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A case-insensitive sub-string to look for in the response body. If this string is not found, the origin will be marked as unhealthy. Only valid if `type` is "http" or "https". Default: "".
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Expected<wbr>Codes</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The expected HTTP response code or code range of the health check. Eg `2xx`. Only valid and required if `type` is "http" or "https".
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Follow<wbr>Redirects</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Follow redirects if returned by the origin. Only valid if `type` is "http" or "https".
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#loadbalancermonitorheader">List&lt;Load<wbr>Balancer<wbr>Monitor<wbr>Header&gt;?</a></span>
    </dt>
    <dd>{{% md %}}The header name.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Interval</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The interval between each health check. Shorter intervals may improve failover time, but will increase load on the origins as we check from multiple locations. Default: 60.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Method</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The method to use for the health check. Valid values are any valid HTTP verb if `type` is "http" or "https", or `connection_established` if `type` is "tcp". Default: "GET" if `type` is "http" or "https", or "connection_established" if `type` is "tcp" .
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Modified<wbr>On</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The RFC3339 timestamp of when the load balancer monitor was last modified.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The endpoint path to health check against. Default: "/". Only valid if `type` is "http" or "https".
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Retries</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The number of retries to attempt in case of a timeout before marking the origin as unhealthy. Retries are attempted immediately. Default: 2.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The timeout (in seconds) before marking the health check as failed. Default: 5.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The protocol to use for the healthcheck. Currently supported protocols are 'HTTP', 'HTTPS' and 'TCP'. Default: "http".
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Allow<wbr>Insecure</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Do not validate the certificate when monitor use HTTPS. Only valid if `type` is "http" or "https".
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Created<wbr>On</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The RFC3339 timestamp of when the load balancer monitor was created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Free text description.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Expected<wbr>Body</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A case-insensitive sub-string to look for in the response body. If this string is not found, the origin will be marked as unhealthy. Only valid if `type` is "http" or "https". Default: "".
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Expected<wbr>Codes</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The expected HTTP response code or code range of the health check. Eg `2xx`. Only valid and required if `type` is "http" or "https".
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Follow<wbr>Redirects</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Follow redirects if returned by the origin. Only valid if `type` is "http" or "https".
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#loadbalancermonitorheader">[]Load<wbr>Balancer<wbr>Monitor<wbr>Header</a></span>
    </dt>
    <dd>{{% md %}}The header name.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Interval</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The interval between each health check. Shorter intervals may improve failover time, but will increase load on the origins as we check from multiple locations. Default: 60.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Method</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The method to use for the health check. Valid values are any valid HTTP verb if `type` is "http" or "https", or `connection_established` if `type` is "tcp". Default: "GET" if `type` is "http" or "https", or "connection_established" if `type` is "tcp" .
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Modified<wbr>On</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The RFC3339 timestamp of when the load balancer monitor was last modified.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The endpoint path to health check against. Default: "/". Only valid if `type` is "http" or "https".
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Retries</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The number of retries to attempt in case of a timeout before marking the origin as unhealthy. Retries are attempted immediately. Default: 2.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The timeout (in seconds) before marking the health check as failed. Default: 5.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The protocol to use for the healthcheck. Currently supported protocols are 'HTTP', 'HTTPS' and 'TCP'. Default: "http".
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>allow<wbr>Insecure</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Do not validate the certificate when monitor use HTTPS. Only valid if `type` is "http" or "https".
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>created<wbr>On</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The RFC3339 timestamp of when the load balancer monitor was created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Free text description.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>expected<wbr>Body</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A case-insensitive sub-string to look for in the response body. If this string is not found, the origin will be marked as unhealthy. Only valid if `type` is "http" or "https". Default: "".
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>expected<wbr>Codes</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The expected HTTP response code or code range of the health check. Eg `2xx`. Only valid and required if `type` is "http" or "https".
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>follow<wbr>Redirects</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Follow redirects if returned by the origin. Only valid if `type` is "http" or "https".
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>headers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#loadbalancermonitorheader">Load<wbr>Balancer<wbr>Monitor<wbr>Header[]?</a></span>
    </dt>
    <dd>{{% md %}}The header name.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>interval</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The interval between each health check. Shorter intervals may improve failover time, but will increase load on the origins as we check from multiple locations. Default: 60.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>method</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The method to use for the health check. Valid values are any valid HTTP verb if `type` is "http" or "https", or `connection_established` if `type` is "tcp". Default: "GET" if `type` is "http" or "https", or "connection_established" if `type` is "tcp" .
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>modified<wbr>On</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The RFC3339 timestamp of when the load balancer monitor was last modified.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The endpoint path to health check against. Default: "/". Only valid if `type` is "http" or "https".
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>retries</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The number of retries to attempt in case of a timeout before marking the origin as unhealthy. Retries are attempted immediately. Default: 2.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The timeout (in seconds) before marking the health check as failed. Default: 5.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The protocol to use for the healthcheck. Currently supported protocols are 'HTTP', 'HTTPS' and 'TCP'. Default: "http".
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>allow_<wbr>insecure</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Do not validate the certificate when monitor use HTTPS. Only valid if `type` is "http" or "https".
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>created_<wbr>on</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The RFC3339 timestamp of when the load balancer monitor was created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Free text description.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>expected_<wbr>body</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A case-insensitive sub-string to look for in the response body. If this string is not found, the origin will be marked as unhealthy. Only valid if `type` is "http" or "https". Default: "".
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>expected_<wbr>codes</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The expected HTTP response code or code range of the health check. Eg `2xx`. Only valid and required if `type` is "http" or "https".
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>follow_<wbr>redirects</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Follow redirects if returned by the origin. Only valid if `type` is "http" or "https".
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>headers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#loadbalancermonitorheader">List[Load<wbr>Balancer<wbr>Monitor<wbr>Header]</a></span>
    </dt>
    <dd>{{% md %}}The header name.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>interval</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The interval between each health check. Shorter intervals may improve failover time, but will increase load on the origins as we check from multiple locations. Default: 60.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>method</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The method to use for the health check. Valid values are any valid HTTP verb if `type` is "http" or "https", or `connection_established` if `type` is "tcp". Default: "GET" if `type` is "http" or "https", or "connection_established" if `type` is "tcp" .
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>modified_<wbr>on</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The RFC3339 timestamp of when the load balancer monitor was last modified.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>path</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The endpoint path to health check against. Default: "/". Only valid if `type` is "http" or "https".
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>retries</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The number of retries to attempt in case of a timeout before marking the origin as unhealthy. Retries are attempted immediately. Default: 2.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The timeout (in seconds) before marking the health check as failed. Default: 5.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The protocol to use for the healthcheck. Currently supported protocols are 'HTTP', 'HTTPS' and 'TCP'. Default: "http".
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing LoadBalancerMonitor Resource

Get an existing LoadBalancerMonitor resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/cloudflare/#LoadBalancerMonitorState">LoadBalancerMonitorState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/cloudflare/#LoadBalancerMonitor">LoadBalancerMonitor</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>allow_insecure=None<span class="p">, </span>created_on=None<span class="p">, </span>description=None<span class="p">, </span>expected_body=None<span class="p">, </span>expected_codes=None<span class="p">, </span>follow_redirects=None<span class="p">, </span>headers=None<span class="p">, </span>interval=None<span class="p">, </span>method=None<span class="p">, </span>modified_on=None<span class="p">, </span>path=None<span class="p">, </span>port=None<span class="p">, </span>retries=None<span class="p">, </span>timeout=None<span class="p">, </span>type=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetLoadBalancerMonitor<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-cloudflare/sdk/go/cloudflare/?tab=doc#LoadBalancerMonitorState">LoadBalancerMonitorState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-cloudflare/sdk/go/cloudflare/?tab=doc#LoadBalancerMonitor">LoadBalancerMonitor</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Cloudflare/Pulumi.Cloudflare..LoadBalancerMonitor.html">LoadBalancerMonitor</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Cloudflare/Pulumi.Cloudflare..LoadBalancerMonitorState.html">LoadBalancerMonitorState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Allow<wbr>Insecure</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Do not validate the certificate when monitor use HTTPS. Only valid if `type` is "http" or "https".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Created<wbr>On</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The RFC3339 timestamp of when the load balancer monitor was created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Free text description.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Expected<wbr>Body</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A case-insensitive sub-string to look for in the response body. If this string is not found, the origin will be marked as unhealthy. Only valid if `type` is "http" or "https". Default: "".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Expected<wbr>Codes</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The expected HTTP response code or code range of the health check. Eg `2xx`. Only valid and required if `type` is "http" or "https".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Follow<wbr>Redirects</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Follow redirects if returned by the origin. Only valid if `type` is "http" or "https".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#loadbalancermonitorheader">List&lt;Load<wbr>Balancer<wbr>Monitor<wbr>Header<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}The header name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Interval</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The interval between each health check. Shorter intervals may improve failover time, but will increase load on the origins as we check from multiple locations. Default: 60.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Method</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The method to use for the health check. Valid values are any valid HTTP verb if `type` is "http" or "https", or `connection_established` if `type` is "tcp". Default: "GET" if `type` is "http" or "https", or "connection_established" if `type` is "tcp" .
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Modified<wbr>On</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The RFC3339 timestamp of when the load balancer monitor was last modified.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The endpoint path to health check against. Default: "/". Only valid if `type` is "http" or "https".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Retries</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The number of retries to attempt in case of a timeout before marking the origin as unhealthy. Retries are attempted immediately. Default: 2.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The timeout (in seconds) before marking the health check as failed. Default: 5.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The protocol to use for the healthcheck. Currently supported protocols are 'HTTP', 'HTTPS' and 'TCP'. Default: "http".
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Insecure</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Do not validate the certificate when monitor use HTTPS. Only valid if `type` is "http" or "https".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Created<wbr>On</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The RFC3339 timestamp of when the load balancer monitor was created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Free text description.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Expected<wbr>Body</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A case-insensitive sub-string to look for in the response body. If this string is not found, the origin will be marked as unhealthy. Only valid if `type` is "http" or "https". Default: "".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Expected<wbr>Codes</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The expected HTTP response code or code range of the health check. Eg `2xx`. Only valid and required if `type` is "http" or "https".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Follow<wbr>Redirects</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Follow redirects if returned by the origin. Only valid if `type` is "http" or "https".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#loadbalancermonitorheader">[]Load<wbr>Balancer<wbr>Monitor<wbr>Header</a></span>
    </dt>
    <dd>{{% md %}}The header name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Interval</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The interval between each health check. Shorter intervals may improve failover time, but will increase load on the origins as we check from multiple locations. Default: 60.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Method</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The method to use for the health check. Valid values are any valid HTTP verb if `type` is "http" or "https", or `connection_established` if `type` is "tcp". Default: "GET" if `type` is "http" or "https", or "connection_established" if `type` is "tcp" .
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Modified<wbr>On</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The RFC3339 timestamp of when the load balancer monitor was last modified.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The endpoint path to health check against. Default: "/". Only valid if `type` is "http" or "https".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Retries</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The number of retries to attempt in case of a timeout before marking the origin as unhealthy. Retries are attempted immediately. Default: 2.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The timeout (in seconds) before marking the health check as failed. Default: 5.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The protocol to use for the healthcheck. Currently supported protocols are 'HTTP', 'HTTPS' and 'TCP'. Default: "http".
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Insecure</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Do not validate the certificate when monitor use HTTPS. Only valid if `type` is "http" or "https".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>created<wbr>On</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The RFC3339 timestamp of when the load balancer monitor was created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Free text description.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>expected<wbr>Body</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A case-insensitive sub-string to look for in the response body. If this string is not found, the origin will be marked as unhealthy. Only valid if `type` is "http" or "https". Default: "".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>expected<wbr>Codes</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The expected HTTP response code or code range of the health check. Eg `2xx`. Only valid and required if `type` is "http" or "https".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>follow<wbr>Redirects</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Follow redirects if returned by the origin. Only valid if `type` is "http" or "https".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>headers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#loadbalancermonitorheader">Load<wbr>Balancer<wbr>Monitor<wbr>Header[]?</a></span>
    </dt>
    <dd>{{% md %}}The header name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>interval</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The interval between each health check. Shorter intervals may improve failover time, but will increase load on the origins as we check from multiple locations. Default: 60.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>method</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The method to use for the health check. Valid values are any valid HTTP verb if `type` is "http" or "https", or `connection_established` if `type` is "tcp". Default: "GET" if `type` is "http" or "https", or "connection_established" if `type` is "tcp" .
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>modified<wbr>On</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The RFC3339 timestamp of when the load balancer monitor was last modified.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The endpoint path to health check against. Default: "/". Only valid if `type` is "http" or "https".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>retries</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The number of retries to attempt in case of a timeout before marking the origin as unhealthy. Retries are attempted immediately. Default: 2.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The timeout (in seconds) before marking the health check as failed. Default: 5.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The protocol to use for the healthcheck. Currently supported protocols are 'HTTP', 'HTTPS' and 'TCP'. Default: "http".
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>allow_<wbr>insecure</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Do not validate the certificate when monitor use HTTPS. Only valid if `type` is "http" or "https".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>created_<wbr>on</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The RFC3339 timestamp of when the load balancer monitor was created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Free text description.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>expected_<wbr>body</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A case-insensitive sub-string to look for in the response body. If this string is not found, the origin will be marked as unhealthy. Only valid if `type` is "http" or "https". Default: "".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>expected_<wbr>codes</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The expected HTTP response code or code range of the health check. Eg `2xx`. Only valid and required if `type` is "http" or "https".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>follow_<wbr>redirects</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Follow redirects if returned by the origin. Only valid if `type` is "http" or "https".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>headers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#loadbalancermonitorheader">List[Load<wbr>Balancer<wbr>Monitor<wbr>Header]</a></span>
    </dt>
    <dd>{{% md %}}The header name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>interval</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The interval between each health check. Shorter intervals may improve failover time, but will increase load on the origins as we check from multiple locations. Default: 60.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>method</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The method to use for the health check. Valid values are any valid HTTP verb if `type` is "http" or "https", or `connection_established` if `type` is "tcp". Default: "GET" if `type` is "http" or "https", or "connection_established" if `type` is "tcp" .
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>modified_<wbr>on</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The RFC3339 timestamp of when the load balancer monitor was last modified.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>path</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The endpoint path to health check against. Default: "/". Only valid if `type` is "http" or "https".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>retries</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The number of retries to attempt in case of a timeout before marking the origin as unhealthy. Retries are attempted immediately. Default: 2.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The timeout (in seconds) before marking the health check as failed. Default: 5.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The protocol to use for the healthcheck. Currently supported protocols are 'HTTP', 'HTTPS' and 'TCP'. Default: "http".
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Load<wbr>Balancer<wbr>Monitor<wbr>Header</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/cloudflare/types/input/#LoadBalancerMonitorHeader">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/cloudflare/types/output/#LoadBalancerMonitorHeader">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-cloudflare/sdk/go/cloudflare/?tab=doc#LoadBalancerMonitorHeaderArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-cloudflare/sdk/go/cloudflare/?tab=doc#LoadBalancerMonitorHeaderOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Header</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The header name.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Values</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}A list of string values for the header.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Header</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The header name.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Values</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of string values for the header.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>header</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The header name.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>values</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}A list of string values for the header.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>header</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The header name.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>values</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of string values for the header.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}









<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-cloudflare">https://github.com/pulumi/pulumi-cloudflare</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    
</dl>

