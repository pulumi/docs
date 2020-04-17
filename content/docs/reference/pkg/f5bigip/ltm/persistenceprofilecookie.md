
---
title: "PersistenceProfileCookie"
block_external_search_index: true
---



Configures a cookie persistence profile

## Reference

`name` - (Required) Name of the virtual address

`defaults_from` - (Required) Parent cookie persistence profile

`match_across_pools` (Optional) (enabled or disabled) match across pools with given persistence record

`match_across_services` (Optional) (enabled or disabled) match across services with given persistence record

`match_across_virtuals` (Optional) (enabled or disabled) match across virtual servers with given persistence record

`mirror` (Optional) (enabled or disabled) mirror persistence record

`timeout` (Optional) (enabled or disabled) Timeout for persistence of the session in seconds

`override_conn_limit` (Optional) (enabled or disabled) Enable or dissable pool member connection limits are overridden for persisted clients. Per-virtual connection limits remain hard limits and are not overridden.

`always_send` (Optional) (enabled or disabled) always send cookies

`cookie_encryption` (Optional) (required, preferred, or disabled) To required, preferred, or disabled policy for cookie encryption

`cookie_encryption_passphrase` (Optional) (required, preferred, or disabled) Passphrase for encrypted cookies. The field is encrypted on the server and will always return differently then set.
If this is configured specify `ignore_changes` under the `lifecycle` block to ignore returned encrypted value.

`cookie_name` (Optional) Name of the cookie to track persistence

`expiration` (Optional) Expiration TTL for cookie specified in DAY:HOUR:MIN:SECONDS (Examples: 1:0:0:0 one day, 1:0:0 one hour, 30:0 thirty minutes)

`hash_length` (Optional) (Integer) Length of hash to apply to cookie

`hash_offset` (Optional) (Integer) Number of characters to skip in the cookie for the hash

`httponly` (Optional) (enabled or disabled) Sending only over http



## Create a PersistenceProfileCookie Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/f5bigip/ltm/#PersistenceProfileCookie">PersistenceProfileCookie</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/f5bigip/ltm/#PersistenceProfileCookieArgs">PersistenceProfileCookieArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">PersistenceProfileCookie</span><span class="p">(resource_name, opts=None, </span>always_send=None<span class="p">, </span>app_service=None<span class="p">, </span>cookie_encryption=None<span class="p">, </span>cookie_encryption_passphrase=None<span class="p">, </span>cookie_name=None<span class="p">, </span>defaults_from=None<span class="p">, </span>expiration=None<span class="p">, </span>hash_length=None<span class="p">, </span>hash_offset=None<span class="p">, </span>httponly=None<span class="p">, </span>match_across_pools=None<span class="p">, </span>match_across_services=None<span class="p">, </span>match_across_virtuals=None<span class="p">, </span>mirror=None<span class="p">, </span>name=None<span class="p">, </span>override_conn_limit=None<span class="p">, </span>timeout=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewPersistenceProfileCookie<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-f5bigip/sdk/v2/go/f5bigip/ltm?tab=doc#PersistenceProfileCookieArgs">PersistenceProfileCookieArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-f5bigip/sdk/v2/go/f5bigip/ltm?tab=doc#PersistenceProfileCookie">PersistenceProfileCookie</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.F5bigip/Pulumi.F5bigip.Ltm.PersistenceProfileCookie.html">PersistenceProfileCookie</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.F5bigip/Pulumi.F5BigIP.Ltm.PersistenceProfileCookieArgs.html">PersistenceProfileCookieArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Defaults<wbr>From</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Inherit defaults from parent profile
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Name of the persistence profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Always<wbr>Send</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}To enable _ disable always sending cookies
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>App<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cookie<wbr>Encryption</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}To required, preferred, or disabled policy for cookie encryption
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cookie<wbr>Encryption<wbr>Passphrase</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Passphrase for encrypted cookies
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cookie<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Name of the cookie to track persistence
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Expiration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Expiration TTL for cookie specified in D:H:M:S or in seconds
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hash<wbr>Length</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}Length of hash to apply to cookie
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hash<wbr>Offset</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}Number of characters to skip in the cookie for the hash
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Httponly</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}To enable _ disable sending only over http
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Match<wbr>Across<wbr>Pools</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}To enable _ disable match across pools with given persistence record
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Match<wbr>Across<wbr>Services</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}To enable _ disable match across services with given persistence record
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Match<wbr>Across<wbr>Virtuals</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}To enable _ disable match across virtual servers with given persistence record
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mirror</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}To enable _ disable
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Override<wbr>Conn<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}To enable _ disable that pool member connection limits are overridden for persisted clients. Per-virtual connection
limits remain hard limits and are not overridden.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}Timeout for persistence of the session
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Defaults<wbr>From</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Inherit defaults from parent profile
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Name of the persistence profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Always<wbr>Send</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}To enable _ disable always sending cookies
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>App<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cookie<wbr>Encryption</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}To required, preferred, or disabled policy for cookie encryption
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cookie<wbr>Encryption<wbr>Passphrase</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Passphrase for encrypted cookies
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cookie<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Name of the cookie to track persistence
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Expiration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Expiration TTL for cookie specified in D:H:M:S or in seconds
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hash<wbr>Length</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}Length of hash to apply to cookie
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hash<wbr>Offset</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}Number of characters to skip in the cookie for the hash
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Httponly</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}To enable _ disable sending only over http
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Match<wbr>Across<wbr>Pools</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}To enable _ disable match across pools with given persistence record
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Match<wbr>Across<wbr>Services</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}To enable _ disable match across services with given persistence record
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Match<wbr>Across<wbr>Virtuals</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}To enable _ disable match across virtual servers with given persistence record
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mirror</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}To enable _ disable
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Override<wbr>Conn<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}To enable _ disable that pool member connection limits are overridden for persisted clients. Per-virtual connection
limits remain hard limits and are not overridden.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}Timeout for persistence of the session
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>defaults<wbr>From</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Inherit defaults from parent profile
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Name of the persistence profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>always<wbr>Send</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}To enable _ disable always sending cookies
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>app<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cookie<wbr>Encryption</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}To required, preferred, or disabled policy for cookie encryption
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cookie<wbr>Encryption<wbr>Passphrase</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Passphrase for encrypted cookies
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cookie<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Name of the cookie to track persistence
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>expiration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Expiration TTL for cookie specified in D:H:M:S or in seconds
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hash<wbr>Length</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}Length of hash to apply to cookie
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hash<wbr>Offset</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}Number of characters to skip in the cookie for the hash
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>httponly</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}To enable _ disable sending only over http
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>match<wbr>Across<wbr>Pools</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}To enable _ disable match across pools with given persistence record
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>match<wbr>Across<wbr>Services</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}To enable _ disable match across services with given persistence record
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>match<wbr>Across<wbr>Virtuals</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}To enable _ disable match across virtual servers with given persistence record
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mirror</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}To enable _ disable
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>override<wbr>Conn<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}To enable _ disable that pool member connection limits are overridden for persisted clients. Per-virtual connection
limits remain hard limits and are not overridden.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}Timeout for persistence of the session
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>defaults_<wbr>from</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Inherit defaults from parent profile
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Name of the persistence profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>always_<wbr>send</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}To enable _ disable always sending cookies
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>app_<wbr>service</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cookie_<wbr>encryption</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}To required, preferred, or disabled policy for cookie encryption
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cookie_<wbr>encryption_<wbr>passphrase</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Passphrase for encrypted cookies
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cookie_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Name of the cookie to track persistence
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>expiration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Expiration TTL for cookie specified in D:H:M:S or in seconds
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hash_<wbr>length</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}Length of hash to apply to cookie
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hash_<wbr>offset</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}Number of characters to skip in the cookie for the hash
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>httponly</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}To enable _ disable sending only over http
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>match_<wbr>across_<wbr>pools</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}To enable _ disable match across pools with given persistence record
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>match_<wbr>across_<wbr>services</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}To enable _ disable match across services with given persistence record
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>match_<wbr>across_<wbr>virtuals</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}To enable _ disable match across virtual servers with given persistence record
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mirror</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}To enable _ disable
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>override_<wbr>conn_<wbr>limit</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}To enable _ disable that pool member connection limits are overridden for persisted clients. Per-virtual connection
limits remain hard limits and are not overridden.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}Timeout for persistence of the session
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Look up an Existing PersistenceProfileCookie Resource

Get an existing PersistenceProfileCookie resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/f5bigip/ltm/#PersistenceProfileCookieState">PersistenceProfileCookieState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/f5bigip/ltm/#PersistenceProfileCookie">PersistenceProfileCookie</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>always_send=None<span class="p">, </span>app_service=None<span class="p">, </span>cookie_encryption=None<span class="p">, </span>cookie_encryption_passphrase=None<span class="p">, </span>cookie_name=None<span class="p">, </span>defaults_from=None<span class="p">, </span>expiration=None<span class="p">, </span>hash_length=None<span class="p">, </span>hash_offset=None<span class="p">, </span>httponly=None<span class="p">, </span>match_across_pools=None<span class="p">, </span>match_across_services=None<span class="p">, </span>match_across_virtuals=None<span class="p">, </span>mirror=None<span class="p">, </span>name=None<span class="p">, </span>override_conn_limit=None<span class="p">, </span>timeout=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetPersistenceProfileCookie<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-f5bigip/sdk/v2/go/f5bigip/ltm?tab=doc#PersistenceProfileCookieState">PersistenceProfileCookieState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-f5bigip/sdk/v2/go/f5bigip/ltm?tab=doc#PersistenceProfileCookie">PersistenceProfileCookie</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.F5bigip/Pulumi.F5bigip.Ltm.PersistenceProfileCookie.html">PersistenceProfileCookie</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.F5bigip/Pulumi.F5bigip.Ltm.PersistenceProfileCookieState.html">PersistenceProfileCookieState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Always<wbr>Send</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}To enable _ disable always sending cookies
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>App<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cookie<wbr>Encryption</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}To required, preferred, or disabled policy for cookie encryption
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cookie<wbr>Encryption<wbr>Passphrase</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Passphrase for encrypted cookies
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cookie<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Name of the cookie to track persistence
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Defaults<wbr>From</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Inherit defaults from parent profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Expiration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Expiration TTL for cookie specified in D:H:M:S or in seconds
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hash<wbr>Length</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}Length of hash to apply to cookie
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hash<wbr>Offset</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}Number of characters to skip in the cookie for the hash
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Httponly</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}To enable _ disable sending only over http
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Match<wbr>Across<wbr>Pools</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}To enable _ disable match across pools with given persistence record
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Match<wbr>Across<wbr>Services</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}To enable _ disable match across services with given persistence record
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Match<wbr>Across<wbr>Virtuals</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}To enable _ disable match across virtual servers with given persistence record
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mirror</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}To enable _ disable
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Name of the persistence profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Override<wbr>Conn<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}To enable _ disable that pool member connection limits are overridden for persisted clients. Per-virtual connection
limits remain hard limits and are not overridden.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}Timeout for persistence of the session
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Always<wbr>Send</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}To enable _ disable always sending cookies
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>App<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cookie<wbr>Encryption</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}To required, preferred, or disabled policy for cookie encryption
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cookie<wbr>Encryption<wbr>Passphrase</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Passphrase for encrypted cookies
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cookie<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Name of the cookie to track persistence
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Defaults<wbr>From</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Inherit defaults from parent profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Expiration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Expiration TTL for cookie specified in D:H:M:S or in seconds
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hash<wbr>Length</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}Length of hash to apply to cookie
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hash<wbr>Offset</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}Number of characters to skip in the cookie for the hash
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Httponly</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}To enable _ disable sending only over http
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Match<wbr>Across<wbr>Pools</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}To enable _ disable match across pools with given persistence record
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Match<wbr>Across<wbr>Services</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}To enable _ disable match across services with given persistence record
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Match<wbr>Across<wbr>Virtuals</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}To enable _ disable match across virtual servers with given persistence record
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mirror</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}To enable _ disable
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Name of the persistence profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Override<wbr>Conn<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}To enable _ disable that pool member connection limits are overridden for persisted clients. Per-virtual connection
limits remain hard limits and are not overridden.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}Timeout for persistence of the session
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>always<wbr>Send</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}To enable _ disable always sending cookies
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>app<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cookie<wbr>Encryption</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}To required, preferred, or disabled policy for cookie encryption
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cookie<wbr>Encryption<wbr>Passphrase</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Passphrase for encrypted cookies
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cookie<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Name of the cookie to track persistence
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>defaults<wbr>From</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Inherit defaults from parent profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>expiration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Expiration TTL for cookie specified in D:H:M:S or in seconds
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hash<wbr>Length</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}Length of hash to apply to cookie
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hash<wbr>Offset</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}Number of characters to skip in the cookie for the hash
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>httponly</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}To enable _ disable sending only over http
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>match<wbr>Across<wbr>Pools</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}To enable _ disable match across pools with given persistence record
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>match<wbr>Across<wbr>Services</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}To enable _ disable match across services with given persistence record
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>match<wbr>Across<wbr>Virtuals</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}To enable _ disable match across virtual servers with given persistence record
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mirror</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}To enable _ disable
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Name of the persistence profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>override<wbr>Conn<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}To enable _ disable that pool member connection limits are overridden for persisted clients. Per-virtual connection
limits remain hard limits and are not overridden.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}Timeout for persistence of the session
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>always_<wbr>send</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}To enable _ disable always sending cookies
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>app_<wbr>service</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cookie_<wbr>encryption</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}To required, preferred, or disabled policy for cookie encryption
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cookie_<wbr>encryption_<wbr>passphrase</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Passphrase for encrypted cookies
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cookie_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Name of the cookie to track persistence
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>defaults_<wbr>from</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Inherit defaults from parent profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>expiration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Expiration TTL for cookie specified in D:H:M:S or in seconds
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hash_<wbr>length</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}Length of hash to apply to cookie
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hash_<wbr>offset</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}Number of characters to skip in the cookie for the hash
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>httponly</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}To enable _ disable sending only over http
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>match_<wbr>across_<wbr>pools</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}To enable _ disable match across pools with given persistence record
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>match_<wbr>across_<wbr>services</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}To enable _ disable match across services with given persistence record
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>match_<wbr>across_<wbr>virtuals</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}To enable _ disable match across virtual servers with given persistence record
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mirror</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}To enable _ disable
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Name of the persistence profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>override_<wbr>conn_<wbr>limit</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}To enable _ disable that pool member connection limits are overridden for persisted clients. Per-virtual connection
limits remain hard limits and are not overridden.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}Timeout for persistence of the session
{{% /md %}}</dd>

</dl>
{{% /choosable %}}











<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-f5bigip">https://github.com/pulumi/pulumi-f5bigip</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    <dt>Notes</dt>
	<dd>This Pulumi package is based on the [`bigip` Terraform Provider](https://github.com/terraform-providers/terraform-provider-bigip).</dd>
</dl>

