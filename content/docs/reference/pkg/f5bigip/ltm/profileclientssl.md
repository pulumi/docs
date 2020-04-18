
---
title: "ProfileClientSsl"
block_external_search_index: true
---



`f5bigip.ltm.ProfileClientSsl` Manages client SSL profiles on a BIG-IP



{{% examples %}}
## Example Usage
{{% example %}}
    

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as f5bigip from "@pulumi/f5bigip";

const test_ClientSsl = new f5bigip.ltm.ProfileClientSsl("test-ClientSsl", {
    authenticate: "always",
    ciphers: "DEFAULT",
    defaultsFrom: "/Common/clientssl",
    name: "/Common/test-ClientSsl",
    partition: "Common",
});
```

{{% /example %}}
{{% /examples %}}



## Create a ProfileClientSsl Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/f5bigip/ltm/#ProfileClientSsl">ProfileClientSsl</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/f5bigip/ltm/#ProfileClientSslArgs">ProfileClientSslArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">ProfileClientSsl</span><span class="p">(resource_name, opts=None, </span>alert_timeout=None<span class="p">, </span>allow_non_ssl=None<span class="p">, </span>authenticate=None<span class="p">, </span>authenticate_depth=None<span class="p">, </span>ca_file=None<span class="p">, </span>cache_size=None<span class="p">, </span>cache_timeout=None<span class="p">, </span>cert=None<span class="p">, </span>cert_extension_includes=None<span class="p">, </span>cert_key_chains=None<span class="p">, </span>cert_life_span=None<span class="p">, </span>cert_lookup_by_ipaddr_port=None<span class="p">, </span>chain=None<span class="p">, </span>ciphers=None<span class="p">, </span>client_cert_ca=None<span class="p">, </span>crl_file=None<span class="p">, </span>defaults_from=None<span class="p">, </span>forward_proxy_bypass_default_action=None<span class="p">, </span>full_path=None<span class="p">, </span>generation=None<span class="p">, </span>generic_alert=None<span class="p">, </span>handshake_timeout=None<span class="p">, </span>inherit_cert_keychain=None<span class="p">, </span>key=None<span class="p">, </span>mod_ssl_methods=None<span class="p">, </span>mode=None<span class="p">, </span>name=None<span class="p">, </span>partition=None<span class="p">, </span>passphrase=None<span class="p">, </span>peer_cert_mode=None<span class="p">, </span>proxy_ca_cert=None<span class="p">, </span>proxy_ca_key=None<span class="p">, </span>proxy_ca_passphrase=None<span class="p">, </span>proxy_ssl=None<span class="p">, </span>proxy_ssl_passthrough=None<span class="p">, </span>renegotiate_period=None<span class="p">, </span>renegotiate_size=None<span class="p">, </span>renegotiation=None<span class="p">, </span>retain_certificate=None<span class="p">, </span>secure_renegotiation=None<span class="p">, </span>server_name=None<span class="p">, </span>session_mirroring=None<span class="p">, </span>session_ticket=None<span class="p">, </span>sni_default=None<span class="p">, </span>sni_require=None<span class="p">, </span>ssl_forward_proxy=None<span class="p">, </span>ssl_forward_proxy_bypass=None<span class="p">, </span>ssl_sign_hash=None<span class="p">, </span>strict_resume=None<span class="p">, </span>tm_options=None<span class="p">, </span>unclean_shutdown=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewProfileClientSsl<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-f5bigip/sdk/v2/go/f5bigip/ltm?tab=doc#ProfileClientSslArgs">ProfileClientSslArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-f5bigip/sdk/v2/go/f5bigip/ltm?tab=doc#ProfileClientSsl">ProfileClientSsl</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.F5bigip/Pulumi.F5bigip.Ltm.ProfileClientSsl.html">ProfileClientSsl</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.F5bigip/Pulumi.F5BigIP.Ltm.ProfileClientSslArgs.html">ProfileClientSslArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the name of the profile. (type `string`)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Alert<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Alert time out
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Non<wbr>Ssl</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Enables or disables acceptance of non-SSL connections, When creating a new profile, the setting is provided by the parent profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Authenticate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the frequency of client authentication for an SSL session.When `once`,specifies that the system authenticates the client once for an SSL session.
When `always`, specifies that the system authenticates the client once for an SSL session and also upon reuse of that session.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Authenticate<wbr>Depth</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}Specifies the maximum number of certificates to be traversed in a client certificate chain
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ca<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Client certificate file path. Default None.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cache<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}Cache size (sessions).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cache<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}Cache time out
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cert</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies a cert name for use.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cert<wbr>Extension<wbr>Includes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}Cert extension includes for ssl forward proxy
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cert<wbr>Key<wbr>Chains</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#profileclientsslcertkeychain">List&lt;Pulumi.<wbr>F5Big<wbr>IP.<wbr>Ltm.<wbr>Inputs.<wbr>Profile<wbr>Client<wbr>Ssl<wbr>Cert<wbr>Key<wbr>Chain<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cert<wbr>Life<wbr>Span</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}Life span of the certificate in days for ssl forward proxy
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cert<wbr>Lookup<wbr>By<wbr>Ipaddr<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Cert lookup by ip address and port enabled / disabled
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Chain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Contains a certificate chain that is relevant to the certificate and key mentioned earlier.This key is optional
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ciphers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the list of ciphers that the system supports. When creating a new profile, the default cipher list is provided by the parent profile.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Cert<wbr>Ca</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}client certificate name
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Crl<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Certificate revocation file name
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Defaults<wbr>From</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The parent template of this monitor template. Once this value has been set, it cannot be changed. By default, this value is the `clientssl` parent on the `Common` partition.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Forward<wbr>Proxy<wbr>Bypass<wbr>Default<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Forward proxy bypass default action. (enabled / disabled)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Full<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}full path of the profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Generation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}generation
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Generic<wbr>Alert</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Generic alerts enabled / disabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Handshake<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Handshake time out (seconds)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Inherit<wbr>Cert<wbr>Keychain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Inherit cert key chain
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Contains a key name
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mod<wbr>Ssl<wbr>Methods</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}ModSSL Methods enabled / disabled. Default is disabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}ModSSL Methods enabled / disabled. Default is disabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Partition</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Device partition to manage resources on.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Passphrase</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Client Certificate Constrained Delegation CA passphrase
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Peer<wbr>Cert<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the way the system handles client certificates.When ignore, specifies that the system ignores certificates from client systems.When require, specifies that the system requires a client to present a valid certificate.When request, specifies that the system requests a valid certificate from a client but always authenticate the client.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Proxy<wbr>Ca<wbr>Cert</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Proxy CA Cert
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Proxy<wbr>Ca<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Proxy CA Key
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Proxy<wbr>Ca<wbr>Passphrase</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Proxy CA Passphrase
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Proxy<wbr>Ssl</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Proxy SSL enabled / disabled. Default is disabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Proxy<wbr>Ssl<wbr>Passthrough</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Proxy SSL passthrough enabled / disabled. Default is disabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Renegotiate<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Renogotiate Period (seconds)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Renegotiate<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Renogotiate Size
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Renegotiation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Enables or disables SSL renegotiation.When creating a new profile, the setting is provided by the parent profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Retain<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}When `true`, client certificate is retained in SSL session.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Secure<wbr>Renegotiation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the method of secure renegotiations for SSL connections. When creating a new profile, the setting is provided by the parent profile.
When `request` is set the system request secure renegotation of SSL connections.
`require` is a default setting and when set the system permits initial SSL handshakes from clients but terminates renegotiations from unpatched clients.
The `require-strict` setting the system requires strict renegotiation of SSL connections. In this mode the system refuses connections to insecure servers, and terminates existing SSL connections to insecure servers
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Server<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the fully qualified DNS hostname of the server used in Server Name Indication communications. When creating a new profile, the setting is provided by the parent profile.The server name can also be a wildcard string containing the asterisk `*` character.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Session<wbr>Mirroring</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Session Mirroring (enabled / disabled)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Session<wbr>Ticket</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Session Ticket (enabled / disabled)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sni<wbr>Default</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Indicates that the system uses this profile as the default SSL profile when there is no match to the server name, or when the client provides no SNI extension support.When creating a new profile, the setting is provided by the parent profile.
There can be only one SSL profile with this setting enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sni<wbr>Require</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Requires that the network peers also provide SNI support, this setting only takes effect when `sni_default` is set to `true`.When creating a new profile, the setting is provided by the parent profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ssl<wbr>Forward<wbr>Proxy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}SSL forward Proxy (enabled / disabled)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ssl<wbr>Forward<wbr>Proxy<wbr>Bypass</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}SSL forward Proxy Bypass (enabled / disabled)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ssl<wbr>Sign<wbr>Hash</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}SSL sign hash (any, sha1, sha256, sha384)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Strict<wbr>Resume</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Enables or disables the resumption of SSL sessions after an unclean shutdown.When creating a new profile, the setting is provided by the parent profile. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tm<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Unclean<wbr>Shutdown</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Unclean Shutdown (enabled / disabled)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the name of the profile. (type `string`)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Alert<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Alert time out
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Non<wbr>Ssl</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Enables or disables acceptance of non-SSL connections, When creating a new profile, the setting is provided by the parent profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Authenticate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the frequency of client authentication for an SSL session.When `once`,specifies that the system authenticates the client once for an SSL session.
When `always`, specifies that the system authenticates the client once for an SSL session and also upon reuse of that session.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Authenticate<wbr>Depth</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}Specifies the maximum number of certificates to be traversed in a client certificate chain
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ca<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Client certificate file path. Default None.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cache<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}Cache size (sessions).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cache<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}Cache time out
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cert</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies a cert name for use.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cert<wbr>Extension<wbr>Includes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}Cert extension includes for ssl forward proxy
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cert<wbr>Key<wbr>Chains</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#profileclientsslcertkeychain">[]Profile<wbr>Client<wbr>Ssl<wbr>Cert<wbr>Key<wbr>Chain</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cert<wbr>Life<wbr>Span</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}Life span of the certificate in days for ssl forward proxy
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cert<wbr>Lookup<wbr>By<wbr>Ipaddr<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Cert lookup by ip address and port enabled / disabled
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Chain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Contains a certificate chain that is relevant to the certificate and key mentioned earlier.This key is optional
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ciphers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the list of ciphers that the system supports. When creating a new profile, the default cipher list is provided by the parent profile.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Cert<wbr>Ca</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}client certificate name
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Crl<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Certificate revocation file name
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Defaults<wbr>From</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The parent template of this monitor template. Once this value has been set, it cannot be changed. By default, this value is the `clientssl` parent on the `Common` partition.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Forward<wbr>Proxy<wbr>Bypass<wbr>Default<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Forward proxy bypass default action. (enabled / disabled)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Full<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}full path of the profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Generation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}generation
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Generic<wbr>Alert</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Generic alerts enabled / disabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Handshake<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Handshake time out (seconds)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Inherit<wbr>Cert<wbr>Keychain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Inherit cert key chain
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Contains a key name
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mod<wbr>Ssl<wbr>Methods</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}ModSSL Methods enabled / disabled. Default is disabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}ModSSL Methods enabled / disabled. Default is disabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Partition</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Device partition to manage resources on.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Passphrase</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Client Certificate Constrained Delegation CA passphrase
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Peer<wbr>Cert<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the way the system handles client certificates.When ignore, specifies that the system ignores certificates from client systems.When require, specifies that the system requires a client to present a valid certificate.When request, specifies that the system requests a valid certificate from a client but always authenticate the client.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Proxy<wbr>Ca<wbr>Cert</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Proxy CA Cert
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Proxy<wbr>Ca<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Proxy CA Key
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Proxy<wbr>Ca<wbr>Passphrase</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Proxy CA Passphrase
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Proxy<wbr>Ssl</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Proxy SSL enabled / disabled. Default is disabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Proxy<wbr>Ssl<wbr>Passthrough</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Proxy SSL passthrough enabled / disabled. Default is disabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Renegotiate<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Renogotiate Period (seconds)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Renegotiate<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Renogotiate Size
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Renegotiation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Enables or disables SSL renegotiation.When creating a new profile, the setting is provided by the parent profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Retain<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}When `true`, client certificate is retained in SSL session.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Secure<wbr>Renegotiation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the method of secure renegotiations for SSL connections. When creating a new profile, the setting is provided by the parent profile.
When `request` is set the system request secure renegotation of SSL connections.
`require` is a default setting and when set the system permits initial SSL handshakes from clients but terminates renegotiations from unpatched clients.
The `require-strict` setting the system requires strict renegotiation of SSL connections. In this mode the system refuses connections to insecure servers, and terminates existing SSL connections to insecure servers
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Server<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the fully qualified DNS hostname of the server used in Server Name Indication communications. When creating a new profile, the setting is provided by the parent profile.The server name can also be a wildcard string containing the asterisk `*` character.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Session<wbr>Mirroring</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Session Mirroring (enabled / disabled)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Session<wbr>Ticket</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Session Ticket (enabled / disabled)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sni<wbr>Default</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Indicates that the system uses this profile as the default SSL profile when there is no match to the server name, or when the client provides no SNI extension support.When creating a new profile, the setting is provided by the parent profile.
There can be only one SSL profile with this setting enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sni<wbr>Require</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Requires that the network peers also provide SNI support, this setting only takes effect when `sni_default` is set to `true`.When creating a new profile, the setting is provided by the parent profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ssl<wbr>Forward<wbr>Proxy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}SSL forward Proxy (enabled / disabled)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ssl<wbr>Forward<wbr>Proxy<wbr>Bypass</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}SSL forward Proxy Bypass (enabled / disabled)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ssl<wbr>Sign<wbr>Hash</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}SSL sign hash (any, sha1, sha256, sha384)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Strict<wbr>Resume</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Enables or disables the resumption of SSL sessions after an unclean shutdown.When creating a new profile, the setting is provided by the parent profile. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tm<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Unclean<wbr>Shutdown</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Unclean Shutdown (enabled / disabled)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the name of the profile. (type `string`)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>alert<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Alert time out
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Non<wbr>Ssl</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Enables or disables acceptance of non-SSL connections, When creating a new profile, the setting is provided by the parent profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>authenticate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the frequency of client authentication for an SSL session.When `once`,specifies that the system authenticates the client once for an SSL session.
When `always`, specifies that the system authenticates the client once for an SSL session and also upon reuse of that session.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>authenticate<wbr>Depth</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}Specifies the maximum number of certificates to be traversed in a client certificate chain
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ca<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Client certificate file path. Default None.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cache<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}Cache size (sessions).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cache<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}Cache time out
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cert</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies a cert name for use.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cert<wbr>Extension<wbr>Includes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}Cert extension includes for ssl forward proxy
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cert<wbr>Key<wbr>Chains</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#profileclientsslcertkeychain">Profile<wbr>Client<wbr>Ssl<wbr>Cert<wbr>Key<wbr>Chain[]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cert<wbr>Life<wbr>Span</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}Life span of the certificate in days for ssl forward proxy
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cert<wbr>Lookup<wbr>By<wbr>Ipaddr<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Cert lookup by ip address and port enabled / disabled
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>chain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Contains a certificate chain that is relevant to the certificate and key mentioned earlier.This key is optional
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ciphers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the list of ciphers that the system supports. When creating a new profile, the default cipher list is provided by the parent profile.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>client<wbr>Cert<wbr>Ca</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}client certificate name
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>crl<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Certificate revocation file name
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>defaults<wbr>From</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The parent template of this monitor template. Once this value has been set, it cannot be changed. By default, this value is the `clientssl` parent on the `Common` partition.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>forward<wbr>Proxy<wbr>Bypass<wbr>Default<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Forward proxy bypass default action. (enabled / disabled)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>full<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}full path of the profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>generation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}generation
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>generic<wbr>Alert</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Generic alerts enabled / disabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>handshake<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Handshake time out (seconds)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>inherit<wbr>Cert<wbr>Keychain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Inherit cert key chain
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Contains a key name
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mod<wbr>Ssl<wbr>Methods</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}ModSSL Methods enabled / disabled. Default is disabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}ModSSL Methods enabled / disabled. Default is disabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>partition</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Device partition to manage resources on.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>passphrase</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Client Certificate Constrained Delegation CA passphrase
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>peer<wbr>Cert<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the way the system handles client certificates.When ignore, specifies that the system ignores certificates from client systems.When require, specifies that the system requires a client to present a valid certificate.When request, specifies that the system requests a valid certificate from a client but always authenticate the client.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>proxy<wbr>Ca<wbr>Cert</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Proxy CA Cert
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>proxy<wbr>Ca<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Proxy CA Key
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>proxy<wbr>Ca<wbr>Passphrase</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Proxy CA Passphrase
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>proxy<wbr>Ssl</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Proxy SSL enabled / disabled. Default is disabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>proxy<wbr>Ssl<wbr>Passthrough</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Proxy SSL passthrough enabled / disabled. Default is disabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>renegotiate<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Renogotiate Period (seconds)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>renegotiate<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Renogotiate Size
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>renegotiation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Enables or disables SSL renegotiation.When creating a new profile, the setting is provided by the parent profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>retain<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}When `true`, client certificate is retained in SSL session.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secure<wbr>Renegotiation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the method of secure renegotiations for SSL connections. When creating a new profile, the setting is provided by the parent profile.
When `request` is set the system request secure renegotation of SSL connections.
`require` is a default setting and when set the system permits initial SSL handshakes from clients but terminates renegotiations from unpatched clients.
The `require-strict` setting the system requires strict renegotiation of SSL connections. In this mode the system refuses connections to insecure servers, and terminates existing SSL connections to insecure servers
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>server<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the fully qualified DNS hostname of the server used in Server Name Indication communications. When creating a new profile, the setting is provided by the parent profile.The server name can also be a wildcard string containing the asterisk `*` character.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>session<wbr>Mirroring</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Session Mirroring (enabled / disabled)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>session<wbr>Ticket</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Session Ticket (enabled / disabled)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sni<wbr>Default</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Indicates that the system uses this profile as the default SSL profile when there is no match to the server name, or when the client provides no SNI extension support.When creating a new profile, the setting is provided by the parent profile.
There can be only one SSL profile with this setting enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sni<wbr>Require</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Requires that the network peers also provide SNI support, this setting only takes effect when `sni_default` is set to `true`.When creating a new profile, the setting is provided by the parent profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ssl<wbr>Forward<wbr>Proxy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}SSL forward Proxy (enabled / disabled)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ssl<wbr>Forward<wbr>Proxy<wbr>Bypass</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}SSL forward Proxy Bypass (enabled / disabled)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ssl<wbr>Sign<wbr>Hash</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}SSL sign hash (any, sha1, sha256, sha384)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>strict<wbr>Resume</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Enables or disables the resumption of SSL sessions after an unclean shutdown.When creating a new profile, the setting is provided by the parent profile. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tm<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>unclean<wbr>Shutdown</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Unclean Shutdown (enabled / disabled)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Specifies the name of the profile. (type `string`)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>alert_<wbr>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Alert time out
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow_<wbr>non_<wbr>ssl</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Enables or disables acceptance of non-SSL connections, When creating a new profile, the setting is provided by the parent profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>authenticate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Specifies the frequency of client authentication for an SSL session.When `once`,specifies that the system authenticates the client once for an SSL session.
When `always`, specifies that the system authenticates the client once for an SSL session and also upon reuse of that session.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>authenticate_<wbr>depth</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}Specifies the maximum number of certificates to be traversed in a client certificate chain
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ca_<wbr>file</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Client certificate file path. Default None.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cache_<wbr>size</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}Cache size (sessions).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cache_<wbr>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}Cache time out
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cert</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Specifies a cert name for use.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cert_<wbr>extension_<wbr>includes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}Cert extension includes for ssl forward proxy
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cert_<wbr>key_<wbr>chains</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#profileclientsslcertkeychain">List[Profile<wbr>Client<wbr>Ssl<wbr>Cert<wbr>Key<wbr>Chain]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cert_<wbr>life_<wbr>span</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}Life span of the certificate in days for ssl forward proxy
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cert_<wbr>lookup_<wbr>by_<wbr>ipaddr_<wbr>port</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Cert lookup by ip address and port enabled / disabled
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>chain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Contains a certificate chain that is relevant to the certificate and key mentioned earlier.This key is optional
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ciphers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Specifies the list of ciphers that the system supports. When creating a new profile, the default cipher list is provided by the parent profile.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>client_<wbr>cert_<wbr>ca</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}client certificate name
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>crl_<wbr>file</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Certificate revocation file name
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>defaults_<wbr>from</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The parent template of this monitor template. Once this value has been set, it cannot be changed. By default, this value is the `clientssl` parent on the `Common` partition.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>forward_<wbr>proxy_<wbr>bypass_<wbr>default_<wbr>action</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Forward proxy bypass default action. (enabled / disabled)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>full_<wbr>path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}full path of the profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>generation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}generation
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>generic_<wbr>alert</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Generic alerts enabled / disabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>handshake_<wbr>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Handshake time out (seconds)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>inherit_<wbr>cert_<wbr>keychain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Inherit cert key chain
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Contains a key name
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mod_<wbr>ssl_<wbr>methods</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}ModSSL Methods enabled / disabled. Default is disabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}ModSSL Methods enabled / disabled. Default is disabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>partition</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Device partition to manage resources on.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>passphrase</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Client Certificate Constrained Delegation CA passphrase
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>peer_<wbr>cert_<wbr>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Specifies the way the system handles client certificates.When ignore, specifies that the system ignores certificates from client systems.When require, specifies that the system requires a client to present a valid certificate.When request, specifies that the system requests a valid certificate from a client but always authenticate the client.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>proxy_<wbr>ca_<wbr>cert</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Proxy CA Cert
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>proxy_<wbr>ca_<wbr>key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Proxy CA Key
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>proxy_<wbr>ca_<wbr>passphrase</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Proxy CA Passphrase
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>proxy_<wbr>ssl</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Proxy SSL enabled / disabled. Default is disabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>proxy_<wbr>ssl_<wbr>passthrough</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Proxy SSL passthrough enabled / disabled. Default is disabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>renegotiate_<wbr>period</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Renogotiate Period (seconds)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>renegotiate_<wbr>size</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Renogotiate Size
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>renegotiation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Enables or disables SSL renegotiation.When creating a new profile, the setting is provided by the parent profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>retain_<wbr>certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}When `true`, client certificate is retained in SSL session.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secure_<wbr>renegotiation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Specifies the method of secure renegotiations for SSL connections. When creating a new profile, the setting is provided by the parent profile.
When `request` is set the system request secure renegotation of SSL connections.
`require` is a default setting and when set the system permits initial SSL handshakes from clients but terminates renegotiations from unpatched clients.
The `require-strict` setting the system requires strict renegotiation of SSL connections. In this mode the system refuses connections to insecure servers, and terminates existing SSL connections to insecure servers
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>server_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Specifies the fully qualified DNS hostname of the server used in Server Name Indication communications. When creating a new profile, the setting is provided by the parent profile.The server name can also be a wildcard string containing the asterisk `*` character.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>session_<wbr>mirroring</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Session Mirroring (enabled / disabled)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>session_<wbr>ticket</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Session Ticket (enabled / disabled)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sni_<wbr>default</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Indicates that the system uses this profile as the default SSL profile when there is no match to the server name, or when the client provides no SNI extension support.When creating a new profile, the setting is provided by the parent profile.
There can be only one SSL profile with this setting enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sni_<wbr>require</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Requires that the network peers also provide SNI support, this setting only takes effect when `sni_default` is set to `true`.When creating a new profile, the setting is provided by the parent profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ssl_<wbr>forward_<wbr>proxy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}SSL forward Proxy (enabled / disabled)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ssl_<wbr>forward_<wbr>proxy_<wbr>bypass</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}SSL forward Proxy Bypass (enabled / disabled)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ssl_<wbr>sign_<wbr>hash</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}SSL sign hash (any, sha1, sha256, sha384)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>strict_<wbr>resume</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Enables or disables the resumption of SSL sessions after an unclean shutdown.When creating a new profile, the setting is provided by the parent profile. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tm_<wbr>options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>unclean_<wbr>shutdown</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Unclean Shutdown (enabled / disabled)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Look up an Existing ProfileClientSsl Resource

Get an existing ProfileClientSsl resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/f5bigip/ltm/#ProfileClientSslState">ProfileClientSslState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/f5bigip/ltm/#ProfileClientSsl">ProfileClientSsl</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>alert_timeout=None<span class="p">, </span>allow_non_ssl=None<span class="p">, </span>authenticate=None<span class="p">, </span>authenticate_depth=None<span class="p">, </span>ca_file=None<span class="p">, </span>cache_size=None<span class="p">, </span>cache_timeout=None<span class="p">, </span>cert=None<span class="p">, </span>cert_extension_includes=None<span class="p">, </span>cert_key_chains=None<span class="p">, </span>cert_life_span=None<span class="p">, </span>cert_lookup_by_ipaddr_port=None<span class="p">, </span>chain=None<span class="p">, </span>ciphers=None<span class="p">, </span>client_cert_ca=None<span class="p">, </span>crl_file=None<span class="p">, </span>defaults_from=None<span class="p">, </span>forward_proxy_bypass_default_action=None<span class="p">, </span>full_path=None<span class="p">, </span>generation=None<span class="p">, </span>generic_alert=None<span class="p">, </span>handshake_timeout=None<span class="p">, </span>inherit_cert_keychain=None<span class="p">, </span>key=None<span class="p">, </span>mod_ssl_methods=None<span class="p">, </span>mode=None<span class="p">, </span>name=None<span class="p">, </span>partition=None<span class="p">, </span>passphrase=None<span class="p">, </span>peer_cert_mode=None<span class="p">, </span>proxy_ca_cert=None<span class="p">, </span>proxy_ca_key=None<span class="p">, </span>proxy_ca_passphrase=None<span class="p">, </span>proxy_ssl=None<span class="p">, </span>proxy_ssl_passthrough=None<span class="p">, </span>renegotiate_period=None<span class="p">, </span>renegotiate_size=None<span class="p">, </span>renegotiation=None<span class="p">, </span>retain_certificate=None<span class="p">, </span>secure_renegotiation=None<span class="p">, </span>server_name=None<span class="p">, </span>session_mirroring=None<span class="p">, </span>session_ticket=None<span class="p">, </span>sni_default=None<span class="p">, </span>sni_require=None<span class="p">, </span>ssl_forward_proxy=None<span class="p">, </span>ssl_forward_proxy_bypass=None<span class="p">, </span>ssl_sign_hash=None<span class="p">, </span>strict_resume=None<span class="p">, </span>tm_options=None<span class="p">, </span>unclean_shutdown=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetProfileClientSsl<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-f5bigip/sdk/v2/go/f5bigip/ltm?tab=doc#ProfileClientSslState">ProfileClientSslState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-f5bigip/sdk/v2/go/f5bigip/ltm?tab=doc#ProfileClientSsl">ProfileClientSsl</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.F5bigip/Pulumi.F5bigip.Ltm.ProfileClientSsl.html">ProfileClientSsl</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.F5bigip/Pulumi.F5bigip.Ltm.ProfileClientSslState.html">ProfileClientSslState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Alert<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Alert time out
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Non<wbr>Ssl</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Enables or disables acceptance of non-SSL connections, When creating a new profile, the setting is provided by the parent profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Authenticate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the frequency of client authentication for an SSL session.When `once`,specifies that the system authenticates the client once for an SSL session.
When `always`, specifies that the system authenticates the client once for an SSL session and also upon reuse of that session.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Authenticate<wbr>Depth</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}Specifies the maximum number of certificates to be traversed in a client certificate chain
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ca<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Client certificate file path. Default None.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cache<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}Cache size (sessions).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cache<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}Cache time out
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cert</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies a cert name for use.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cert<wbr>Extension<wbr>Includes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}Cert extension includes for ssl forward proxy
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cert<wbr>Key<wbr>Chains</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#profileclientsslcertkeychain">List&lt;Pulumi.<wbr>F5Big<wbr>IP.<wbr>Ltm.<wbr>Inputs.<wbr>Profile<wbr>Client<wbr>Ssl<wbr>Cert<wbr>Key<wbr>Chain<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cert<wbr>Life<wbr>Span</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}Life span of the certificate in days for ssl forward proxy
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cert<wbr>Lookup<wbr>By<wbr>Ipaddr<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Cert lookup by ip address and port enabled / disabled
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Chain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Contains a certificate chain that is relevant to the certificate and key mentioned earlier.This key is optional
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ciphers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the list of ciphers that the system supports. When creating a new profile, the default cipher list is provided by the parent profile.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Cert<wbr>Ca</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}client certificate name
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Crl<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Certificate revocation file name
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Defaults<wbr>From</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The parent template of this monitor template. Once this value has been set, it cannot be changed. By default, this value is the `clientssl` parent on the `Common` partition.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Forward<wbr>Proxy<wbr>Bypass<wbr>Default<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Forward proxy bypass default action. (enabled / disabled)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Full<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}full path of the profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Generation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}generation
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Generic<wbr>Alert</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Generic alerts enabled / disabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Handshake<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Handshake time out (seconds)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Inherit<wbr>Cert<wbr>Keychain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Inherit cert key chain
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Contains a key name
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mod<wbr>Ssl<wbr>Methods</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}ModSSL Methods enabled / disabled. Default is disabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}ModSSL Methods enabled / disabled. Default is disabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the name of the profile. (type `string`)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Partition</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Device partition to manage resources on.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Passphrase</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Client Certificate Constrained Delegation CA passphrase
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Peer<wbr>Cert<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the way the system handles client certificates.When ignore, specifies that the system ignores certificates from client systems.When require, specifies that the system requires a client to present a valid certificate.When request, specifies that the system requests a valid certificate from a client but always authenticate the client.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Proxy<wbr>Ca<wbr>Cert</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Proxy CA Cert
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Proxy<wbr>Ca<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Proxy CA Key
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Proxy<wbr>Ca<wbr>Passphrase</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Proxy CA Passphrase
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Proxy<wbr>Ssl</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Proxy SSL enabled / disabled. Default is disabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Proxy<wbr>Ssl<wbr>Passthrough</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Proxy SSL passthrough enabled / disabled. Default is disabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Renegotiate<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Renogotiate Period (seconds)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Renegotiate<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Renogotiate Size
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Renegotiation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Enables or disables SSL renegotiation.When creating a new profile, the setting is provided by the parent profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Retain<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}When `true`, client certificate is retained in SSL session.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Secure<wbr>Renegotiation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the method of secure renegotiations for SSL connections. When creating a new profile, the setting is provided by the parent profile.
When `request` is set the system request secure renegotation of SSL connections.
`require` is a default setting and when set the system permits initial SSL handshakes from clients but terminates renegotiations from unpatched clients.
The `require-strict` setting the system requires strict renegotiation of SSL connections. In this mode the system refuses connections to insecure servers, and terminates existing SSL connections to insecure servers
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Server<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the fully qualified DNS hostname of the server used in Server Name Indication communications. When creating a new profile, the setting is provided by the parent profile.The server name can also be a wildcard string containing the asterisk `*` character.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Session<wbr>Mirroring</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Session Mirroring (enabled / disabled)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Session<wbr>Ticket</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Session Ticket (enabled / disabled)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sni<wbr>Default</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Indicates that the system uses this profile as the default SSL profile when there is no match to the server name, or when the client provides no SNI extension support.When creating a new profile, the setting is provided by the parent profile.
There can be only one SSL profile with this setting enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sni<wbr>Require</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Requires that the network peers also provide SNI support, this setting only takes effect when `sni_default` is set to `true`.When creating a new profile, the setting is provided by the parent profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ssl<wbr>Forward<wbr>Proxy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}SSL forward Proxy (enabled / disabled)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ssl<wbr>Forward<wbr>Proxy<wbr>Bypass</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}SSL forward Proxy Bypass (enabled / disabled)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ssl<wbr>Sign<wbr>Hash</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}SSL sign hash (any, sha1, sha256, sha384)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Strict<wbr>Resume</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Enables or disables the resumption of SSL sessions after an unclean shutdown.When creating a new profile, the setting is provided by the parent profile. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tm<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Unclean<wbr>Shutdown</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Unclean Shutdown (enabled / disabled)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Alert<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Alert time out
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Non<wbr>Ssl</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Enables or disables acceptance of non-SSL connections, When creating a new profile, the setting is provided by the parent profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Authenticate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the frequency of client authentication for an SSL session.When `once`,specifies that the system authenticates the client once for an SSL session.
When `always`, specifies that the system authenticates the client once for an SSL session and also upon reuse of that session.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Authenticate<wbr>Depth</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}Specifies the maximum number of certificates to be traversed in a client certificate chain
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ca<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Client certificate file path. Default None.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cache<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}Cache size (sessions).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cache<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}Cache time out
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cert</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies a cert name for use.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cert<wbr>Extension<wbr>Includes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}Cert extension includes for ssl forward proxy
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cert<wbr>Key<wbr>Chains</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#profileclientsslcertkeychain">[]Profile<wbr>Client<wbr>Ssl<wbr>Cert<wbr>Key<wbr>Chain</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cert<wbr>Life<wbr>Span</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}Life span of the certificate in days for ssl forward proxy
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cert<wbr>Lookup<wbr>By<wbr>Ipaddr<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Cert lookup by ip address and port enabled / disabled
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Chain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Contains a certificate chain that is relevant to the certificate and key mentioned earlier.This key is optional
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ciphers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the list of ciphers that the system supports. When creating a new profile, the default cipher list is provided by the parent profile.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Cert<wbr>Ca</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}client certificate name
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Crl<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Certificate revocation file name
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Defaults<wbr>From</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The parent template of this monitor template. Once this value has been set, it cannot be changed. By default, this value is the `clientssl` parent on the `Common` partition.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Forward<wbr>Proxy<wbr>Bypass<wbr>Default<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Forward proxy bypass default action. (enabled / disabled)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Full<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}full path of the profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Generation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}generation
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Generic<wbr>Alert</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Generic alerts enabled / disabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Handshake<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Handshake time out (seconds)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Inherit<wbr>Cert<wbr>Keychain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Inherit cert key chain
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Contains a key name
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mod<wbr>Ssl<wbr>Methods</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}ModSSL Methods enabled / disabled. Default is disabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}ModSSL Methods enabled / disabled. Default is disabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the name of the profile. (type `string`)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Partition</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Device partition to manage resources on.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Passphrase</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Client Certificate Constrained Delegation CA passphrase
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Peer<wbr>Cert<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the way the system handles client certificates.When ignore, specifies that the system ignores certificates from client systems.When require, specifies that the system requires a client to present a valid certificate.When request, specifies that the system requests a valid certificate from a client but always authenticate the client.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Proxy<wbr>Ca<wbr>Cert</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Proxy CA Cert
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Proxy<wbr>Ca<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Proxy CA Key
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Proxy<wbr>Ca<wbr>Passphrase</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Proxy CA Passphrase
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Proxy<wbr>Ssl</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Proxy SSL enabled / disabled. Default is disabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Proxy<wbr>Ssl<wbr>Passthrough</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Proxy SSL passthrough enabled / disabled. Default is disabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Renegotiate<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Renogotiate Period (seconds)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Renegotiate<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Renogotiate Size
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Renegotiation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Enables or disables SSL renegotiation.When creating a new profile, the setting is provided by the parent profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Retain<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}When `true`, client certificate is retained in SSL session.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Secure<wbr>Renegotiation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the method of secure renegotiations for SSL connections. When creating a new profile, the setting is provided by the parent profile.
When `request` is set the system request secure renegotation of SSL connections.
`require` is a default setting and when set the system permits initial SSL handshakes from clients but terminates renegotiations from unpatched clients.
The `require-strict` setting the system requires strict renegotiation of SSL connections. In this mode the system refuses connections to insecure servers, and terminates existing SSL connections to insecure servers
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Server<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the fully qualified DNS hostname of the server used in Server Name Indication communications. When creating a new profile, the setting is provided by the parent profile.The server name can also be a wildcard string containing the asterisk `*` character.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Session<wbr>Mirroring</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Session Mirroring (enabled / disabled)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Session<wbr>Ticket</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Session Ticket (enabled / disabled)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sni<wbr>Default</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Indicates that the system uses this profile as the default SSL profile when there is no match to the server name, or when the client provides no SNI extension support.When creating a new profile, the setting is provided by the parent profile.
There can be only one SSL profile with this setting enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sni<wbr>Require</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Requires that the network peers also provide SNI support, this setting only takes effect when `sni_default` is set to `true`.When creating a new profile, the setting is provided by the parent profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ssl<wbr>Forward<wbr>Proxy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}SSL forward Proxy (enabled / disabled)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ssl<wbr>Forward<wbr>Proxy<wbr>Bypass</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}SSL forward Proxy Bypass (enabled / disabled)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ssl<wbr>Sign<wbr>Hash</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}SSL sign hash (any, sha1, sha256, sha384)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Strict<wbr>Resume</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Enables or disables the resumption of SSL sessions after an unclean shutdown.When creating a new profile, the setting is provided by the parent profile. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tm<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Unclean<wbr>Shutdown</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Unclean Shutdown (enabled / disabled)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>alert<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Alert time out
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Non<wbr>Ssl</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Enables or disables acceptance of non-SSL connections, When creating a new profile, the setting is provided by the parent profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>authenticate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the frequency of client authentication for an SSL session.When `once`,specifies that the system authenticates the client once for an SSL session.
When `always`, specifies that the system authenticates the client once for an SSL session and also upon reuse of that session.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>authenticate<wbr>Depth</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}Specifies the maximum number of certificates to be traversed in a client certificate chain
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ca<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Client certificate file path. Default None.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cache<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}Cache size (sessions).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cache<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}Cache time out
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cert</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies a cert name for use.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cert<wbr>Extension<wbr>Includes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}Cert extension includes for ssl forward proxy
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cert<wbr>Key<wbr>Chains</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#profileclientsslcertkeychain">Profile<wbr>Client<wbr>Ssl<wbr>Cert<wbr>Key<wbr>Chain[]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cert<wbr>Life<wbr>Span</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}Life span of the certificate in days for ssl forward proxy
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cert<wbr>Lookup<wbr>By<wbr>Ipaddr<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Cert lookup by ip address and port enabled / disabled
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>chain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Contains a certificate chain that is relevant to the certificate and key mentioned earlier.This key is optional
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ciphers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the list of ciphers that the system supports. When creating a new profile, the default cipher list is provided by the parent profile.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>client<wbr>Cert<wbr>Ca</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}client certificate name
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>crl<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Certificate revocation file name
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>defaults<wbr>From</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The parent template of this monitor template. Once this value has been set, it cannot be changed. By default, this value is the `clientssl` parent on the `Common` partition.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>forward<wbr>Proxy<wbr>Bypass<wbr>Default<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Forward proxy bypass default action. (enabled / disabled)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>full<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}full path of the profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>generation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}generation
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>generic<wbr>Alert</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Generic alerts enabled / disabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>handshake<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Handshake time out (seconds)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>inherit<wbr>Cert<wbr>Keychain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Inherit cert key chain
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Contains a key name
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mod<wbr>Ssl<wbr>Methods</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}ModSSL Methods enabled / disabled. Default is disabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}ModSSL Methods enabled / disabled. Default is disabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the name of the profile. (type `string`)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>partition</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Device partition to manage resources on.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>passphrase</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Client Certificate Constrained Delegation CA passphrase
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>peer<wbr>Cert<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the way the system handles client certificates.When ignore, specifies that the system ignores certificates from client systems.When require, specifies that the system requires a client to present a valid certificate.When request, specifies that the system requests a valid certificate from a client but always authenticate the client.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>proxy<wbr>Ca<wbr>Cert</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Proxy CA Cert
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>proxy<wbr>Ca<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Proxy CA Key
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>proxy<wbr>Ca<wbr>Passphrase</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Proxy CA Passphrase
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>proxy<wbr>Ssl</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Proxy SSL enabled / disabled. Default is disabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>proxy<wbr>Ssl<wbr>Passthrough</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Proxy SSL passthrough enabled / disabled. Default is disabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>renegotiate<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Renogotiate Period (seconds)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>renegotiate<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Renogotiate Size
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>renegotiation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Enables or disables SSL renegotiation.When creating a new profile, the setting is provided by the parent profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>retain<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}When `true`, client certificate is retained in SSL session.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secure<wbr>Renegotiation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the method of secure renegotiations for SSL connections. When creating a new profile, the setting is provided by the parent profile.
When `request` is set the system request secure renegotation of SSL connections.
`require` is a default setting and when set the system permits initial SSL handshakes from clients but terminates renegotiations from unpatched clients.
The `require-strict` setting the system requires strict renegotiation of SSL connections. In this mode the system refuses connections to insecure servers, and terminates existing SSL connections to insecure servers
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>server<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the fully qualified DNS hostname of the server used in Server Name Indication communications. When creating a new profile, the setting is provided by the parent profile.The server name can also be a wildcard string containing the asterisk `*` character.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>session<wbr>Mirroring</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Session Mirroring (enabled / disabled)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>session<wbr>Ticket</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Session Ticket (enabled / disabled)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sni<wbr>Default</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Indicates that the system uses this profile as the default SSL profile when there is no match to the server name, or when the client provides no SNI extension support.When creating a new profile, the setting is provided by the parent profile.
There can be only one SSL profile with this setting enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sni<wbr>Require</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Requires that the network peers also provide SNI support, this setting only takes effect when `sni_default` is set to `true`.When creating a new profile, the setting is provided by the parent profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ssl<wbr>Forward<wbr>Proxy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}SSL forward Proxy (enabled / disabled)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ssl<wbr>Forward<wbr>Proxy<wbr>Bypass</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}SSL forward Proxy Bypass (enabled / disabled)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ssl<wbr>Sign<wbr>Hash</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}SSL sign hash (any, sha1, sha256, sha384)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>strict<wbr>Resume</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Enables or disables the resumption of SSL sessions after an unclean shutdown.When creating a new profile, the setting is provided by the parent profile. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tm<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>unclean<wbr>Shutdown</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Unclean Shutdown (enabled / disabled)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>alert_<wbr>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Alert time out
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow_<wbr>non_<wbr>ssl</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Enables or disables acceptance of non-SSL connections, When creating a new profile, the setting is provided by the parent profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>authenticate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Specifies the frequency of client authentication for an SSL session.When `once`,specifies that the system authenticates the client once for an SSL session.
When `always`, specifies that the system authenticates the client once for an SSL session and also upon reuse of that session.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>authenticate_<wbr>depth</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}Specifies the maximum number of certificates to be traversed in a client certificate chain
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ca_<wbr>file</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Client certificate file path. Default None.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cache_<wbr>size</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}Cache size (sessions).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cache_<wbr>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}Cache time out
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cert</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Specifies a cert name for use.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cert_<wbr>extension_<wbr>includes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}Cert extension includes for ssl forward proxy
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cert_<wbr>key_<wbr>chains</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#profileclientsslcertkeychain">List[Profile<wbr>Client<wbr>Ssl<wbr>Cert<wbr>Key<wbr>Chain]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cert_<wbr>life_<wbr>span</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}Life span of the certificate in days for ssl forward proxy
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cert_<wbr>lookup_<wbr>by_<wbr>ipaddr_<wbr>port</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Cert lookup by ip address and port enabled / disabled
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>chain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Contains a certificate chain that is relevant to the certificate and key mentioned earlier.This key is optional
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ciphers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Specifies the list of ciphers that the system supports. When creating a new profile, the default cipher list is provided by the parent profile.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>client_<wbr>cert_<wbr>ca</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}client certificate name
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>crl_<wbr>file</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Certificate revocation file name
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>defaults_<wbr>from</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The parent template of this monitor template. Once this value has been set, it cannot be changed. By default, this value is the `clientssl` parent on the `Common` partition.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>forward_<wbr>proxy_<wbr>bypass_<wbr>default_<wbr>action</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Forward proxy bypass default action. (enabled / disabled)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>full_<wbr>path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}full path of the profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>generation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}generation
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>generic_<wbr>alert</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Generic alerts enabled / disabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>handshake_<wbr>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Handshake time out (seconds)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>inherit_<wbr>cert_<wbr>keychain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Inherit cert key chain
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Contains a key name
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mod_<wbr>ssl_<wbr>methods</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}ModSSL Methods enabled / disabled. Default is disabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}ModSSL Methods enabled / disabled. Default is disabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Specifies the name of the profile. (type `string`)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>partition</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Device partition to manage resources on.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>passphrase</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Client Certificate Constrained Delegation CA passphrase
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>peer_<wbr>cert_<wbr>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Specifies the way the system handles client certificates.When ignore, specifies that the system ignores certificates from client systems.When require, specifies that the system requires a client to present a valid certificate.When request, specifies that the system requests a valid certificate from a client but always authenticate the client.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>proxy_<wbr>ca_<wbr>cert</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Proxy CA Cert
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>proxy_<wbr>ca_<wbr>key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Proxy CA Key
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>proxy_<wbr>ca_<wbr>passphrase</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Proxy CA Passphrase
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>proxy_<wbr>ssl</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Proxy SSL enabled / disabled. Default is disabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>proxy_<wbr>ssl_<wbr>passthrough</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Proxy SSL passthrough enabled / disabled. Default is disabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>renegotiate_<wbr>period</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Renogotiate Period (seconds)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>renegotiate_<wbr>size</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Renogotiate Size
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>renegotiation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Enables or disables SSL renegotiation.When creating a new profile, the setting is provided by the parent profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>retain_<wbr>certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}When `true`, client certificate is retained in SSL session.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secure_<wbr>renegotiation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Specifies the method of secure renegotiations for SSL connections. When creating a new profile, the setting is provided by the parent profile.
When `request` is set the system request secure renegotation of SSL connections.
`require` is a default setting and when set the system permits initial SSL handshakes from clients but terminates renegotiations from unpatched clients.
The `require-strict` setting the system requires strict renegotiation of SSL connections. In this mode the system refuses connections to insecure servers, and terminates existing SSL connections to insecure servers
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>server_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Specifies the fully qualified DNS hostname of the server used in Server Name Indication communications. When creating a new profile, the setting is provided by the parent profile.The server name can also be a wildcard string containing the asterisk `*` character.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>session_<wbr>mirroring</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Session Mirroring (enabled / disabled)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>session_<wbr>ticket</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Session Ticket (enabled / disabled)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sni_<wbr>default</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Indicates that the system uses this profile as the default SSL profile when there is no match to the server name, or when the client provides no SNI extension support.When creating a new profile, the setting is provided by the parent profile.
There can be only one SSL profile with this setting enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sni_<wbr>require</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Requires that the network peers also provide SNI support, this setting only takes effect when `sni_default` is set to `true`.When creating a new profile, the setting is provided by the parent profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ssl_<wbr>forward_<wbr>proxy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}SSL forward Proxy (enabled / disabled)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ssl_<wbr>forward_<wbr>proxy_<wbr>bypass</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}SSL forward Proxy Bypass (enabled / disabled)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ssl_<wbr>sign_<wbr>hash</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}SSL sign hash (any, sha1, sha256, sha384)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>strict_<wbr>resume</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Enables or disables the resumption of SSL sessions after an unclean shutdown.When creating a new profile, the setting is provided by the parent profile. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tm_<wbr>options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>unclean_<wbr>shutdown</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Unclean Shutdown (enabled / disabled)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Profile<wbr>Client<wbr>Ssl<wbr>Cert<wbr>Key<wbr>Chain</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/f5bigip/types/input/#ProfileClientSslCertKeyChain">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/f5bigip/types/output/#ProfileClientSslCertKeyChain">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-f5bigip/sdk/v2/go/f5bigip/ltm?tab=doc#ProfileClientSslCertKeyChainArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-f5bigip/sdk/v2/go/f5bigip/ltm?tab=doc#ProfileClientSslCertKeyChainOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Cert</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies a cert name for use.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Chain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Contains a certificate chain that is relevant to the certificate and key mentioned earlier.This key is optional
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Contains a key name
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the name of the profile. (type `string`)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Passphrase</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Cert</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies a cert name for use.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Chain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Contains a certificate chain that is relevant to the certificate and key mentioned earlier.This key is optional
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Contains a key name
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the name of the profile. (type `string`)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Passphrase</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>cert</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies a cert name for use.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>chain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Contains a certificate chain that is relevant to the certificate and key mentioned earlier.This key is optional
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Contains a key name
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the name of the profile. (type `string`)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>passphrase</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>cert</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Specifies a cert name for use.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>chain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Contains a certificate chain that is relevant to the certificate and key mentioned earlier.This key is optional
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Contains a key name
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Specifies the name of the profile. (type `string`)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>passphrase</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

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

