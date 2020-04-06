
---
title: "ProfileHttp"
block_external_search_index: true
---



`f5bigip.ltm.ProfileHttp` Configures a custom profile_http for use by health checks.

For resources should be named with their "full path". The full path is the combination of the partition + name of the resource. For example /Common/my-pool.

> This content is derived from https://github.com/terraform-providers/terraform-provider-bigip/blob/master/website/docs/r/bigip_ltm_profile_http.html.markdown.



## Create a ProfileHttp Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/f5bigip/ltm/#ProfileHttp">ProfileHttp</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/f5bigip/ltm/#ProfileHttpArgs">ProfileHttpArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">ProfileHttp</span><span class="p">(resource_name, opts=None, </span>accept_xff=None<span class="p">, </span>app_service=None<span class="p">, </span>basic_auth_realm=None<span class="p">, </span>defaults_from=None<span class="p">, </span>description=None<span class="p">, </span>encrypt_cookie_secret=None<span class="p">, </span>encrypt_cookies=None<span class="p">, </span>fallback_host=None<span class="p">, </span>fallback_status_codes=None<span class="p">, </span>head_erase=None<span class="p">, </span>head_insert=None<span class="p">, </span>insert_xforwarded_for=None<span class="p">, </span>lws_separator=None<span class="p">, </span>name=None<span class="p">, </span>oneconnect_transformations=None<span class="p">, </span>proxy_type=None<span class="p">, </span>redirect_rewrite=None<span class="p">, </span>request_chunking=None<span class="p">, </span>response_chunking=None<span class="p">, </span>response_headers_permitteds=None<span class="p">, </span>server_agent_name=None<span class="p">, </span>tm_partition=None<span class="p">, </span>via_host_name=None<span class="p">, </span>via_request=None<span class="p">, </span>via_response=None<span class="p">, </span>xff_alternative_names=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewProfileHttp<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-f5bigip/sdk/go/f5bigip/ltm?tab=doc#ProfileHttpArgs">ProfileHttpArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-f5bigip/sdk/go/f5bigip/ltm?tab=doc#ProfileHttp">ProfileHttp</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.F5bigip/Pulumi.F5bigip.Ltm.ProfileHttp.html">ProfileHttp</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.F5bigip/Pulumi.F5bigip.Ltm.ProfileHttpArgs.html">ProfileHttpArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Accept<wbr>Xff</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Enables or disables trusting the client IP address, and statistics from the client IP address, based on the request's
XFF (X-forwarded-for) headers, if they exist.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>App<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The application service to which the object belongs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Basic<wbr>Auth<wbr>Realm</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies a quoted string for the basic authentication realm. The system sends this string to a client whenever authorization fails. The default value is none
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Defaults<wbr>From</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the profile that you want to use as the parent profile. Your new profile inherits all settings and values from the parent profile specified.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}User defibned description
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Encrypt<wbr>Cookie<wbr>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies a passphrase for the cookie encryption
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Encrypt<wbr>Cookies</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Encrypts specified cookies that the BIG-IP system sends to a client system
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fallback<wbr>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies an HTTP fallback host. HTTP redirection allows you to redirect HTTP traffic to another protocol identifier, host name, port number
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fallback<wbr>Status<wbr>Codes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Specifies one or more three-digit status codes that can be returned by an HTTP server.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Head<wbr>Erase</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the header string that you want to erase from an HTTP request. You can also specify none
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Head<wbr>Insert</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies a quoted header string that you want to insert into an HTTP request
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Insert<wbr>Xforwarded<wbr>For</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}When using connection pooling, which allows clients to make use of other client requests' server-side connections, you can insert the X-Forwarded-For header and specify a client IP address
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Lws<wbr>Separator</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies a quoted header string that you want to insert into an HTTP request. You can also specify none.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the profile_http
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Oneconnect<wbr>Transformations</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Enables the system to perform HTTP header transformations for the purpose of  keeping server-side connections open. This feature requires configuration of a OneConnect profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Proxy<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the type of HTTP proxy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Redirect<wbr>Rewrite</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies which of the application HTTP redirects the system rewrites to HTTPS.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Request<wbr>Chunking</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies how to handle chunked and unchunked requests.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Response<wbr>Chunking</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies how to handle chunked and unchunked responses.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Response<wbr>Headers<wbr>Permitteds</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Specifies headers that the BIG-IP system allows in an HTTP response.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Server<wbr>Agent<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the value of the Server header in responses that the BIG-IP itself generates. The default is BigIP. If no
string is specified, then no Server header will be added to such responses
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tm<wbr>Partition</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Displays the administrative partition within which this profile resides.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Via<wbr>Host<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the hostname to include into Via header
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Via<wbr>Request</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies whether to append, remove, or preserve a Via header in an HTTP request
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Via<wbr>Response</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies whether to append, remove, or preserve a Via header in an HTTP request
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Xff<wbr>Alternative<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Specifies alternative XFF headers instead of the default X-forwarded-for header
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Accept<wbr>Xff</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Enables or disables trusting the client IP address, and statistics from the client IP address, based on the request's
XFF (X-forwarded-for) headers, if they exist.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>App<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The application service to which the object belongs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Basic<wbr>Auth<wbr>Realm</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies a quoted string for the basic authentication realm. The system sends this string to a client whenever authorization fails. The default value is none
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Defaults<wbr>From</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the profile that you want to use as the parent profile. Your new profile inherits all settings and values from the parent profile specified.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}User defibned description
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Encrypt<wbr>Cookie<wbr>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies a passphrase for the cookie encryption
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Encrypt<wbr>Cookies</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Encrypts specified cookies that the BIG-IP system sends to a client system
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fallback<wbr>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies an HTTP fallback host. HTTP redirection allows you to redirect HTTP traffic to another protocol identifier, host name, port number
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fallback<wbr>Status<wbr>Codes</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Specifies one or more three-digit status codes that can be returned by an HTTP server.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Head<wbr>Erase</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the header string that you want to erase from an HTTP request. You can also specify none
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Head<wbr>Insert</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies a quoted header string that you want to insert into an HTTP request
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Insert<wbr>Xforwarded<wbr>For</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}When using connection pooling, which allows clients to make use of other client requests' server-side connections, you can insert the X-Forwarded-For header and specify a client IP address
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Lws<wbr>Separator</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies a quoted header string that you want to insert into an HTTP request. You can also specify none.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the profile_http
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Oneconnect<wbr>Transformations</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Enables the system to perform HTTP header transformations for the purpose of  keeping server-side connections open. This feature requires configuration of a OneConnect profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Proxy<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the type of HTTP proxy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Redirect<wbr>Rewrite</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies which of the application HTTP redirects the system rewrites to HTTPS.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Request<wbr>Chunking</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies how to handle chunked and unchunked requests.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Response<wbr>Chunking</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies how to handle chunked and unchunked responses.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Response<wbr>Headers<wbr>Permitteds</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Specifies headers that the BIG-IP system allows in an HTTP response.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Server<wbr>Agent<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the value of the Server header in responses that the BIG-IP itself generates. The default is BigIP. If no
string is specified, then no Server header will be added to such responses
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tm<wbr>Partition</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Displays the administrative partition within which this profile resides.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Via<wbr>Host<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the hostname to include into Via header
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Via<wbr>Request</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies whether to append, remove, or preserve a Via header in an HTTP request
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Via<wbr>Response</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies whether to append, remove, or preserve a Via header in an HTTP request
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Xff<wbr>Alternative<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Specifies alternative XFF headers instead of the default X-forwarded-for header
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>accept<wbr>Xff</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Enables or disables trusting the client IP address, and statistics from the client IP address, based on the request's
XFF (X-forwarded-for) headers, if they exist.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>app<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The application service to which the object belongs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>basic<wbr>Auth<wbr>Realm</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies a quoted string for the basic authentication realm. The system sends this string to a client whenever authorization fails. The default value is none
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>defaults<wbr>From</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the profile that you want to use as the parent profile. Your new profile inherits all settings and values from the parent profile specified.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}User defibned description
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>encrypt<wbr>Cookie<wbr>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies a passphrase for the cookie encryption
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>encrypt<wbr>Cookies</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Encrypts specified cookies that the BIG-IP system sends to a client system
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fallback<wbr>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies an HTTP fallback host. HTTP redirection allows you to redirect HTTP traffic to another protocol identifier, host name, port number
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fallback<wbr>Status<wbr>Codes</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Specifies one or more three-digit status codes that can be returned by an HTTP server.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>head<wbr>Erase</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the header string that you want to erase from an HTTP request. You can also specify none
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>head<wbr>Insert</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies a quoted header string that you want to insert into an HTTP request
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>insert<wbr>Xforwarded<wbr>For</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}When using connection pooling, which allows clients to make use of other client requests' server-side connections, you can insert the X-Forwarded-For header and specify a client IP address
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>lws<wbr>Separator</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies a quoted header string that you want to insert into an HTTP request. You can also specify none.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the profile_http
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>oneconnect<wbr>Transformations</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Enables the system to perform HTTP header transformations for the purpose of  keeping server-side connections open. This feature requires configuration of a OneConnect profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>proxy<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the type of HTTP proxy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>redirect<wbr>Rewrite</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies which of the application HTTP redirects the system rewrites to HTTPS.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>request<wbr>Chunking</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies how to handle chunked and unchunked requests.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>response<wbr>Chunking</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies how to handle chunked and unchunked responses.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>response<wbr>Headers<wbr>Permitteds</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Specifies headers that the BIG-IP system allows in an HTTP response.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>server<wbr>Agent<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the value of the Server header in responses that the BIG-IP itself generates. The default is BigIP. If no
string is specified, then no Server header will be added to such responses
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tm<wbr>Partition</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Displays the administrative partition within which this profile resides.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>via<wbr>Host<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the hostname to include into Via header
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>via<wbr>Request</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies whether to append, remove, or preserve a Via header in an HTTP request
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>via<wbr>Response</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies whether to append, remove, or preserve a Via header in an HTTP request
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>xff<wbr>Alternative<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Specifies alternative XFF headers instead of the default X-forwarded-for header
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>accept_<wbr>xff</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Enables or disables trusting the client IP address, and statistics from the client IP address, based on the request's
XFF (X-forwarded-for) headers, if they exist.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>app_<wbr>service</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The application service to which the object belongs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>basic_<wbr>auth_<wbr>realm</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies a quoted string for the basic authentication realm. The system sends this string to a client whenever authorization fails. The default value is none
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>defaults_<wbr>from</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the profile that you want to use as the parent profile. Your new profile inherits all settings and values from the parent profile specified.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}User defibned description
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>encrypt_<wbr>cookie_<wbr>secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies a passphrase for the cookie encryption
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>encrypt_<wbr>cookies</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Encrypts specified cookies that the BIG-IP system sends to a client system
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fallback_<wbr>host</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies an HTTP fallback host. HTTP redirection allows you to redirect HTTP traffic to another protocol identifier, host name, port number
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fallback_<wbr>status_<wbr>codes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Specifies one or more three-digit status codes that can be returned by an HTTP server.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>head_<wbr>erase</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the header string that you want to erase from an HTTP request. You can also specify none
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>head_<wbr>insert</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies a quoted header string that you want to insert into an HTTP request
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>insert_<wbr>xforwarded_<wbr>for</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}When using connection pooling, which allows clients to make use of other client requests' server-side connections, you can insert the X-Forwarded-For header and specify a client IP address
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>lws_<wbr>separator</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies a quoted header string that you want to insert into an HTTP request. You can also specify none.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the profile_http
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>oneconnect_<wbr>transformations</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Enables the system to perform HTTP header transformations for the purpose of  keeping server-side connections open. This feature requires configuration of a OneConnect profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>proxy_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the type of HTTP proxy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>redirect_<wbr>rewrite</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies which of the application HTTP redirects the system rewrites to HTTPS.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>request_<wbr>chunking</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies how to handle chunked and unchunked requests.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>response_<wbr>chunking</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies how to handle chunked and unchunked responses.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>response_<wbr>headers_<wbr>permitteds</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Specifies headers that the BIG-IP system allows in an HTTP response.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>server_<wbr>agent_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the value of the Server header in responses that the BIG-IP itself generates. The default is BigIP. If no
string is specified, then no Server header will be added to such responses
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tm_<wbr>partition</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Displays the administrative partition within which this profile resides.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>via_<wbr>host_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the hostname to include into Via header
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>via_<wbr>request</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies whether to append, remove, or preserve a Via header in an HTTP request
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>via_<wbr>response</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies whether to append, remove, or preserve a Via header in an HTTP request
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>xff_<wbr>alternative_<wbr>names</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Specifies alternative XFF headers instead of the default X-forwarded-for header
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## ProfileHttp Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Accept<wbr>Xff</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Enables or disables trusting the client IP address, and statistics from the client IP address, based on the request's
XFF (X-forwarded-for) headers, if they exist.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>App<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The application service to which the object belongs.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Basic<wbr>Auth<wbr>Realm</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies a quoted string for the basic authentication realm. The system sends this string to a client whenever authorization fails. The default value is none
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Defaults<wbr>From</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the profile that you want to use as the parent profile. Your new profile inherits all settings and values from the parent profile specified.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}User defibned description
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Encrypt<wbr>Cookie<wbr>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies a passphrase for the cookie encryption
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Encrypt<wbr>Cookies</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Encrypts specified cookies that the BIG-IP system sends to a client system
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Fallback<wbr>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies an HTTP fallback host. HTTP redirection allows you to redirect HTTP traffic to another protocol identifier, host name, port number
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Fallback<wbr>Status<wbr>Codes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Specifies one or more three-digit status codes that can be returned by an HTTP server.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Head<wbr>Erase</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the header string that you want to erase from an HTTP request. You can also specify none
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Head<wbr>Insert</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies a quoted header string that you want to insert into an HTTP request
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Insert<wbr>Xforwarded<wbr>For</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}When using connection pooling, which allows clients to make use of other client requests' server-side connections, you can insert the X-Forwarded-For header and specify a client IP address
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Lws<wbr>Separator</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies a quoted header string that you want to insert into an HTTP request. You can also specify none.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the profile_http
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Oneconnect<wbr>Transformations</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Enables the system to perform HTTP header transformations for the purpose of  keeping server-side connections open. This feature requires configuration of a OneConnect profile
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Proxy<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the type of HTTP proxy.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Redirect<wbr>Rewrite</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies which of the application HTTP redirects the system rewrites to HTTPS.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Request<wbr>Chunking</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies how to handle chunked and unchunked requests.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Response<wbr>Chunking</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies how to handle chunked and unchunked responses.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Response<wbr>Headers<wbr>Permitteds</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Specifies headers that the BIG-IP system allows in an HTTP response.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Server<wbr>Agent<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the value of the Server header in responses that the BIG-IP itself generates. The default is BigIP. If no
string is specified, then no Server header will be added to such responses
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tm<wbr>Partition</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Displays the administrative partition within which this profile resides.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Via<wbr>Host<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the hostname to include into Via header
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Via<wbr>Request</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies whether to append, remove, or preserve a Via header in an HTTP request
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Via<wbr>Response</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies whether to append, remove, or preserve a Via header in an HTTP request
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Xff<wbr>Alternative<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Specifies alternative XFF headers instead of the default X-forwarded-for header
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Accept<wbr>Xff</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Enables or disables trusting the client IP address, and statistics from the client IP address, based on the request's
XFF (X-forwarded-for) headers, if they exist.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>App<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The application service to which the object belongs.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Basic<wbr>Auth<wbr>Realm</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies a quoted string for the basic authentication realm. The system sends this string to a client whenever authorization fails. The default value is none
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Defaults<wbr>From</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the profile that you want to use as the parent profile. Your new profile inherits all settings and values from the parent profile specified.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}User defibned description
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Encrypt<wbr>Cookie<wbr>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies a passphrase for the cookie encryption
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Encrypt<wbr>Cookies</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Encrypts specified cookies that the BIG-IP system sends to a client system
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Fallback<wbr>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies an HTTP fallback host. HTTP redirection allows you to redirect HTTP traffic to another protocol identifier, host name, port number
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Fallback<wbr>Status<wbr>Codes</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Specifies one or more three-digit status codes that can be returned by an HTTP server.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Head<wbr>Erase</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the header string that you want to erase from an HTTP request. You can also specify none
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Head<wbr>Insert</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies a quoted header string that you want to insert into an HTTP request
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Insert<wbr>Xforwarded<wbr>For</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}When using connection pooling, which allows clients to make use of other client requests' server-side connections, you can insert the X-Forwarded-For header and specify a client IP address
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Lws<wbr>Separator</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies a quoted header string that you want to insert into an HTTP request. You can also specify none.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the profile_http
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Oneconnect<wbr>Transformations</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Enables the system to perform HTTP header transformations for the purpose of  keeping server-side connections open. This feature requires configuration of a OneConnect profile
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Proxy<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the type of HTTP proxy.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Redirect<wbr>Rewrite</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies which of the application HTTP redirects the system rewrites to HTTPS.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Request<wbr>Chunking</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies how to handle chunked and unchunked requests.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Response<wbr>Chunking</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies how to handle chunked and unchunked responses.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Response<wbr>Headers<wbr>Permitteds</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Specifies headers that the BIG-IP system allows in an HTTP response.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Server<wbr>Agent<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the value of the Server header in responses that the BIG-IP itself generates. The default is BigIP. If no
string is specified, then no Server header will be added to such responses
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tm<wbr>Partition</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Displays the administrative partition within which this profile resides.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Via<wbr>Host<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the hostname to include into Via header
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Via<wbr>Request</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies whether to append, remove, or preserve a Via header in an HTTP request
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Via<wbr>Response</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies whether to append, remove, or preserve a Via header in an HTTP request
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Xff<wbr>Alternative<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Specifies alternative XFF headers instead of the default X-forwarded-for header
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>accept<wbr>Xff</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Enables or disables trusting the client IP address, and statistics from the client IP address, based on the request's
XFF (X-forwarded-for) headers, if they exist.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>app<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The application service to which the object belongs.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>basic<wbr>Auth<wbr>Realm</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies a quoted string for the basic authentication realm. The system sends this string to a client whenever authorization fails. The default value is none
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>defaults<wbr>From</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the profile that you want to use as the parent profile. Your new profile inherits all settings and values from the parent profile specified.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}User defibned description
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>encrypt<wbr>Cookie<wbr>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies a passphrase for the cookie encryption
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>encrypt<wbr>Cookies</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Encrypts specified cookies that the BIG-IP system sends to a client system
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>fallback<wbr>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies an HTTP fallback host. HTTP redirection allows you to redirect HTTP traffic to another protocol identifier, host name, port number
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>fallback<wbr>Status<wbr>Codes</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Specifies one or more three-digit status codes that can be returned by an HTTP server.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>head<wbr>Erase</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the header string that you want to erase from an HTTP request. You can also specify none
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>head<wbr>Insert</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies a quoted header string that you want to insert into an HTTP request
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>insert<wbr>Xforwarded<wbr>For</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}When using connection pooling, which allows clients to make use of other client requests' server-side connections, you can insert the X-Forwarded-For header and specify a client IP address
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>lws<wbr>Separator</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies a quoted header string that you want to insert into an HTTP request. You can also specify none.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the profile_http
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>oneconnect<wbr>Transformations</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Enables the system to perform HTTP header transformations for the purpose of  keeping server-side connections open. This feature requires configuration of a OneConnect profile
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>proxy<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the type of HTTP proxy.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>redirect<wbr>Rewrite</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies which of the application HTTP redirects the system rewrites to HTTPS.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>request<wbr>Chunking</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies how to handle chunked and unchunked requests.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>response<wbr>Chunking</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies how to handle chunked and unchunked responses.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>response<wbr>Headers<wbr>Permitteds</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Specifies headers that the BIG-IP system allows in an HTTP response.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>server<wbr>Agent<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the value of the Server header in responses that the BIG-IP itself generates. The default is BigIP. If no
string is specified, then no Server header will be added to such responses
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tm<wbr>Partition</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Displays the administrative partition within which this profile resides.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>via<wbr>Host<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the hostname to include into Via header
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>via<wbr>Request</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies whether to append, remove, or preserve a Via header in an HTTP request
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>via<wbr>Response</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies whether to append, remove, or preserve a Via header in an HTTP request
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>xff<wbr>Alternative<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Specifies alternative XFF headers instead of the default X-forwarded-for header
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>accept_<wbr>xff</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Enables or disables trusting the client IP address, and statistics from the client IP address, based on the request's
XFF (X-forwarded-for) headers, if they exist.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>app_<wbr>service</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The application service to which the object belongs.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>basic_<wbr>auth_<wbr>realm</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies a quoted string for the basic authentication realm. The system sends this string to a client whenever authorization fails. The default value is none
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>defaults_<wbr>from</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the profile that you want to use as the parent profile. Your new profile inherits all settings and values from the parent profile specified.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}User defibned description
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>encrypt_<wbr>cookie_<wbr>secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies a passphrase for the cookie encryption
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>encrypt_<wbr>cookies</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Encrypts specified cookies that the BIG-IP system sends to a client system
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>fallback_<wbr>host</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies an HTTP fallback host. HTTP redirection allows you to redirect HTTP traffic to another protocol identifier, host name, port number
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>fallback_<wbr>status_<wbr>codes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Specifies one or more three-digit status codes that can be returned by an HTTP server.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>head_<wbr>erase</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the header string that you want to erase from an HTTP request. You can also specify none
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>head_<wbr>insert</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies a quoted header string that you want to insert into an HTTP request
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>insert_<wbr>xforwarded_<wbr>for</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}When using connection pooling, which allows clients to make use of other client requests' server-side connections, you can insert the X-Forwarded-For header and specify a client IP address
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>lws_<wbr>separator</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies a quoted header string that you want to insert into an HTTP request. You can also specify none.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the profile_http
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>oneconnect_<wbr>transformations</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Enables the system to perform HTTP header transformations for the purpose of  keeping server-side connections open. This feature requires configuration of a OneConnect profile
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>proxy_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the type of HTTP proxy.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>redirect_<wbr>rewrite</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies which of the application HTTP redirects the system rewrites to HTTPS.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>request_<wbr>chunking</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies how to handle chunked and unchunked requests.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>response_<wbr>chunking</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies how to handle chunked and unchunked responses.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>response_<wbr>headers_<wbr>permitteds</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Specifies headers that the BIG-IP system allows in an HTTP response.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>server_<wbr>agent_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the value of the Server header in responses that the BIG-IP itself generates. The default is BigIP. If no
string is specified, then no Server header will be added to such responses
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tm_<wbr>partition</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Displays the administrative partition within which this profile resides.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>via_<wbr>host_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the hostname to include into Via header
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>via_<wbr>request</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies whether to append, remove, or preserve a Via header in an HTTP request
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>via_<wbr>response</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies whether to append, remove, or preserve a Via header in an HTTP request
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>xff_<wbr>alternative_<wbr>names</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Specifies alternative XFF headers instead of the default X-forwarded-for header
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing ProfileHttp Resource

Get an existing ProfileHttp resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/f5bigip/ltm/#ProfileHttpState">ProfileHttpState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/f5bigip/ltm/#ProfileHttp">ProfileHttp</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>accept_xff=None<span class="p">, </span>app_service=None<span class="p">, </span>basic_auth_realm=None<span class="p">, </span>defaults_from=None<span class="p">, </span>description=None<span class="p">, </span>encrypt_cookie_secret=None<span class="p">, </span>encrypt_cookies=None<span class="p">, </span>fallback_host=None<span class="p">, </span>fallback_status_codes=None<span class="p">, </span>head_erase=None<span class="p">, </span>head_insert=None<span class="p">, </span>insert_xforwarded_for=None<span class="p">, </span>lws_separator=None<span class="p">, </span>name=None<span class="p">, </span>oneconnect_transformations=None<span class="p">, </span>proxy_type=None<span class="p">, </span>redirect_rewrite=None<span class="p">, </span>request_chunking=None<span class="p">, </span>response_chunking=None<span class="p">, </span>response_headers_permitteds=None<span class="p">, </span>server_agent_name=None<span class="p">, </span>tm_partition=None<span class="p">, </span>via_host_name=None<span class="p">, </span>via_request=None<span class="p">, </span>via_response=None<span class="p">, </span>xff_alternative_names=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetProfileHttp<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-f5bigip/sdk/go/f5bigip/ltm?tab=doc#ProfileHttpState">ProfileHttpState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-f5bigip/sdk/go/f5bigip/ltm?tab=doc#ProfileHttp">ProfileHttp</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.F5bigip/Pulumi.F5bigip.Ltm.ProfileHttp.html">ProfileHttp</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.F5bigip/Pulumi.F5bigip.Ltm.ProfileHttpState.html">ProfileHttpState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Accept<wbr>Xff</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Enables or disables trusting the client IP address, and statistics from the client IP address, based on the request's
XFF (X-forwarded-for) headers, if they exist.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>App<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The application service to which the object belongs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Basic<wbr>Auth<wbr>Realm</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies a quoted string for the basic authentication realm. The system sends this string to a client whenever authorization fails. The default value is none
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Defaults<wbr>From</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the profile that you want to use as the parent profile. Your new profile inherits all settings and values from the parent profile specified.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}User defibned description
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Encrypt<wbr>Cookie<wbr>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies a passphrase for the cookie encryption
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Encrypt<wbr>Cookies</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Encrypts specified cookies that the BIG-IP system sends to a client system
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fallback<wbr>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies an HTTP fallback host. HTTP redirection allows you to redirect HTTP traffic to another protocol identifier, host name, port number
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fallback<wbr>Status<wbr>Codes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Specifies one or more three-digit status codes that can be returned by an HTTP server.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Head<wbr>Erase</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the header string that you want to erase from an HTTP request. You can also specify none
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Head<wbr>Insert</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies a quoted header string that you want to insert into an HTTP request
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Insert<wbr>Xforwarded<wbr>For</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}When using connection pooling, which allows clients to make use of other client requests' server-side connections, you can insert the X-Forwarded-For header and specify a client IP address
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Lws<wbr>Separator</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies a quoted header string that you want to insert into an HTTP request. You can also specify none.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the profile_http
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Oneconnect<wbr>Transformations</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Enables the system to perform HTTP header transformations for the purpose of  keeping server-side connections open. This feature requires configuration of a OneConnect profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Proxy<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the type of HTTP proxy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Redirect<wbr>Rewrite</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies which of the application HTTP redirects the system rewrites to HTTPS.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Request<wbr>Chunking</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies how to handle chunked and unchunked requests.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Response<wbr>Chunking</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies how to handle chunked and unchunked responses.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Response<wbr>Headers<wbr>Permitteds</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Specifies headers that the BIG-IP system allows in an HTTP response.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Server<wbr>Agent<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the value of the Server header in responses that the BIG-IP itself generates. The default is BigIP. If no
string is specified, then no Server header will be added to such responses
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tm<wbr>Partition</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Displays the administrative partition within which this profile resides.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Via<wbr>Host<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the hostname to include into Via header
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Via<wbr>Request</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies whether to append, remove, or preserve a Via header in an HTTP request
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Via<wbr>Response</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies whether to append, remove, or preserve a Via header in an HTTP request
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Xff<wbr>Alternative<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Specifies alternative XFF headers instead of the default X-forwarded-for header
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Accept<wbr>Xff</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Enables or disables trusting the client IP address, and statistics from the client IP address, based on the request's
XFF (X-forwarded-for) headers, if they exist.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>App<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The application service to which the object belongs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Basic<wbr>Auth<wbr>Realm</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies a quoted string for the basic authentication realm. The system sends this string to a client whenever authorization fails. The default value is none
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Defaults<wbr>From</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the profile that you want to use as the parent profile. Your new profile inherits all settings and values from the parent profile specified.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}User defibned description
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Encrypt<wbr>Cookie<wbr>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies a passphrase for the cookie encryption
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Encrypt<wbr>Cookies</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Encrypts specified cookies that the BIG-IP system sends to a client system
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fallback<wbr>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies an HTTP fallback host. HTTP redirection allows you to redirect HTTP traffic to another protocol identifier, host name, port number
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fallback<wbr>Status<wbr>Codes</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Specifies one or more three-digit status codes that can be returned by an HTTP server.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Head<wbr>Erase</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the header string that you want to erase from an HTTP request. You can also specify none
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Head<wbr>Insert</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies a quoted header string that you want to insert into an HTTP request
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Insert<wbr>Xforwarded<wbr>For</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}When using connection pooling, which allows clients to make use of other client requests' server-side connections, you can insert the X-Forwarded-For header and specify a client IP address
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Lws<wbr>Separator</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies a quoted header string that you want to insert into an HTTP request. You can also specify none.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of the profile_http
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Oneconnect<wbr>Transformations</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Enables the system to perform HTTP header transformations for the purpose of  keeping server-side connections open. This feature requires configuration of a OneConnect profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Proxy<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the type of HTTP proxy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Redirect<wbr>Rewrite</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies which of the application HTTP redirects the system rewrites to HTTPS.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Request<wbr>Chunking</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies how to handle chunked and unchunked requests.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Response<wbr>Chunking</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies how to handle chunked and unchunked responses.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Response<wbr>Headers<wbr>Permitteds</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Specifies headers that the BIG-IP system allows in an HTTP response.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Server<wbr>Agent<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the value of the Server header in responses that the BIG-IP itself generates. The default is BigIP. If no
string is specified, then no Server header will be added to such responses
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tm<wbr>Partition</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Displays the administrative partition within which this profile resides.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Via<wbr>Host<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the hostname to include into Via header
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Via<wbr>Request</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies whether to append, remove, or preserve a Via header in an HTTP request
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Via<wbr>Response</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies whether to append, remove, or preserve a Via header in an HTTP request
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Xff<wbr>Alternative<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Specifies alternative XFF headers instead of the default X-forwarded-for header
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>accept<wbr>Xff</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Enables or disables trusting the client IP address, and statistics from the client IP address, based on the request's
XFF (X-forwarded-for) headers, if they exist.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>app<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The application service to which the object belongs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>basic<wbr>Auth<wbr>Realm</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies a quoted string for the basic authentication realm. The system sends this string to a client whenever authorization fails. The default value is none
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>defaults<wbr>From</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the profile that you want to use as the parent profile. Your new profile inherits all settings and values from the parent profile specified.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}User defibned description
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>encrypt<wbr>Cookie<wbr>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies a passphrase for the cookie encryption
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>encrypt<wbr>Cookies</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Encrypts specified cookies that the BIG-IP system sends to a client system
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fallback<wbr>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies an HTTP fallback host. HTTP redirection allows you to redirect HTTP traffic to another protocol identifier, host name, port number
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fallback<wbr>Status<wbr>Codes</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Specifies one or more three-digit status codes that can be returned by an HTTP server.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>head<wbr>Erase</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the header string that you want to erase from an HTTP request. You can also specify none
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>head<wbr>Insert</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies a quoted header string that you want to insert into an HTTP request
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>insert<wbr>Xforwarded<wbr>For</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}When using connection pooling, which allows clients to make use of other client requests' server-side connections, you can insert the X-Forwarded-For header and specify a client IP address
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>lws<wbr>Separator</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies a quoted header string that you want to insert into an HTTP request. You can also specify none.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the profile_http
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>oneconnect<wbr>Transformations</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Enables the system to perform HTTP header transformations for the purpose of  keeping server-side connections open. This feature requires configuration of a OneConnect profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>proxy<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the type of HTTP proxy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>redirect<wbr>Rewrite</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies which of the application HTTP redirects the system rewrites to HTTPS.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>request<wbr>Chunking</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies how to handle chunked and unchunked requests.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>response<wbr>Chunking</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies how to handle chunked and unchunked responses.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>response<wbr>Headers<wbr>Permitteds</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Specifies headers that the BIG-IP system allows in an HTTP response.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>server<wbr>Agent<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the value of the Server header in responses that the BIG-IP itself generates. The default is BigIP. If no
string is specified, then no Server header will be added to such responses
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tm<wbr>Partition</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Displays the administrative partition within which this profile resides.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>via<wbr>Host<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the hostname to include into Via header
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>via<wbr>Request</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies whether to append, remove, or preserve a Via header in an HTTP request
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>via<wbr>Response</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies whether to append, remove, or preserve a Via header in an HTTP request
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>xff<wbr>Alternative<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Specifies alternative XFF headers instead of the default X-forwarded-for header
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>accept_<wbr>xff</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Enables or disables trusting the client IP address, and statistics from the client IP address, based on the request's
XFF (X-forwarded-for) headers, if they exist.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>app_<wbr>service</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The application service to which the object belongs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>basic_<wbr>auth_<wbr>realm</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies a quoted string for the basic authentication realm. The system sends this string to a client whenever authorization fails. The default value is none
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>defaults_<wbr>from</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the profile that you want to use as the parent profile. Your new profile inherits all settings and values from the parent profile specified.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}User defibned description
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>encrypt_<wbr>cookie_<wbr>secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies a passphrase for the cookie encryption
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>encrypt_<wbr>cookies</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Encrypts specified cookies that the BIG-IP system sends to a client system
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fallback_<wbr>host</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies an HTTP fallback host. HTTP redirection allows you to redirect HTTP traffic to another protocol identifier, host name, port number
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fallback_<wbr>status_<wbr>codes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Specifies one or more three-digit status codes that can be returned by an HTTP server.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>head_<wbr>erase</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the header string that you want to erase from an HTTP request. You can also specify none
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>head_<wbr>insert</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies a quoted header string that you want to insert into an HTTP request
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>insert_<wbr>xforwarded_<wbr>for</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}When using connection pooling, which allows clients to make use of other client requests' server-side connections, you can insert the X-Forwarded-For header and specify a client IP address
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>lws_<wbr>separator</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies a quoted header string that you want to insert into an HTTP request. You can also specify none.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the profile_http
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>oneconnect_<wbr>transformations</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Enables the system to perform HTTP header transformations for the purpose of  keeping server-side connections open. This feature requires configuration of a OneConnect profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>proxy_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the type of HTTP proxy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>redirect_<wbr>rewrite</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies which of the application HTTP redirects the system rewrites to HTTPS.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>request_<wbr>chunking</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies how to handle chunked and unchunked requests.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>response_<wbr>chunking</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies how to handle chunked and unchunked responses.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>response_<wbr>headers_<wbr>permitteds</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Specifies headers that the BIG-IP system allows in an HTTP response.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>server_<wbr>agent_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the value of the Server header in responses that the BIG-IP itself generates. The default is BigIP. If no
string is specified, then no Server header will be added to such responses
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tm_<wbr>partition</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Displays the administrative partition within which this profile resides.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>via_<wbr>host_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the hostname to include into Via header
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>via_<wbr>request</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies whether to append, remove, or preserve a Via header in an HTTP request
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>via_<wbr>response</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies whether to append, remove, or preserve a Via header in an HTTP request
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>xff_<wbr>alternative_<wbr>names</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Specifies alternative XFF headers instead of the default X-forwarded-for header
{{% /md %}}</dd>

</dl>
{{% /choosable %}}











<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-f5bigip">https://github.com/pulumi/pulumi-f5bigip</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    
</dl>

