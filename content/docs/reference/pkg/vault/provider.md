
---
title: "Provider"
block_external_search_index: true
---



The provider type for the vault package. By default, resources use package-wide configuration
settings, however an explicit `Provider` instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
[documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.

> This content is derived from https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/index.html.markdown.



## Create a Provider Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/vault/#Provider">Provider</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/vault/#ProviderArgs">ProviderArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Provider</span><span class="p">(resource_name, opts=None, </span>address=None<span class="p">, </span>auth_logins=None<span class="p">, </span>ca_cert_dir=None<span class="p">, </span>ca_cert_file=None<span class="p">, </span>client_auths=None<span class="p">, </span>max_lease_ttl_seconds=None<span class="p">, </span>max_retries=None<span class="p">, </span>namespace=None<span class="p">, </span>skip_tls_verify=None<span class="p">, </span>token=None<span class="p">, </span>token_name=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewProvider<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-vault/sdk/go/vault/?tab=doc#ProviderArgs">ProviderArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-vault/sdk/go/vault/?tab=doc#Provider">Provider</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Vault/Pulumi.Vault..Provider.html">Provider</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Vault/Pulumi.Pulumi.VaultArgs.html">ProviderArgs</a></span>? <span class="nx">args = null<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}URL of the root of the target Vault server.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Auth<wbr>Logins</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#providerauthlogin">List&lt;Provider<wbr>Auth<wbr>Login<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Login to vault with an existing auth method using auth/<mount>/login
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ca<wbr>Cert<wbr>Dir</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Path to directory containing CA certificate files to validate the server's certificate.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ca<wbr>Cert<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Path to a CA certificate file to validate the server's certificate.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Auths</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#providerclientauth">List&lt;Provider<wbr>Client<wbr>Auth<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Client authentication credentials.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Lease<wbr>Ttl<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Maximum TTL for secret leases requested by this provider
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Retries</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Maximum number of retries when a 5xx error code is encountered.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The namespace to use. Available only for Vault Enterprise
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Skip<wbr>Tls<wbr>Verify</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Set this to true only if the target Vault server is an insecure development instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Token to use to authenticate to Vault.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Token name to use for creating the Vault child token.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}URL of the root of the target Vault server.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Auth<wbr>Logins</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#providerauthlogin">[]Provider<wbr>Auth<wbr>Login</a></span>
    </dt>
    <dd>{{% md %}}Login to vault with an existing auth method using auth/<mount>/login
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ca<wbr>Cert<wbr>Dir</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Path to directory containing CA certificate files to validate the server's certificate.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ca<wbr>Cert<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Path to a CA certificate file to validate the server's certificate.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Auths</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#providerclientauth">[]Provider<wbr>Client<wbr>Auth</a></span>
    </dt>
    <dd>{{% md %}}Client authentication credentials.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Lease<wbr>Ttl<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Maximum TTL for secret leases requested by this provider
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Retries</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Maximum number of retries when a 5xx error code is encountered.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The namespace to use. Available only for Vault Enterprise
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Skip<wbr>Tls<wbr>Verify</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Set this to true only if the target Vault server is an insecure development instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Token to use to authenticate to Vault.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Token name to use for creating the Vault child token.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}URL of the root of the target Vault server.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>auth<wbr>Logins</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#providerauthlogin">Provider<wbr>Auth<wbr>Login[]?</a></span>
    </dt>
    <dd>{{% md %}}Login to vault with an existing auth method using auth/<mount>/login
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ca<wbr>Cert<wbr>Dir</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Path to directory containing CA certificate files to validate the server's certificate.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ca<wbr>Cert<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Path to a CA certificate file to validate the server's certificate.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>client<wbr>Auths</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#providerclientauth">Provider<wbr>Client<wbr>Auth[]?</a></span>
    </dt>
    <dd>{{% md %}}Client authentication credentials.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Lease<wbr>Ttl<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Maximum TTL for secret leases requested by this provider
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Retries</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Maximum number of retries when a 5xx error code is encountered.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The namespace to use. Available only for Vault Enterprise
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>skip<wbr>Tls<wbr>Verify</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Set this to true only if the target Vault server is an insecure development instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Token to use to authenticate to Vault.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Token name to use for creating the Vault child token.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>address</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}URL of the root of the target Vault server.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>auth_<wbr>logins</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#providerauthlogin">List[Provider<wbr>Auth<wbr>Login]</a></span>
    </dt>
    <dd>{{% md %}}Login to vault with an existing auth method using auth/<mount>/login
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ca_<wbr>cert_<wbr>dir</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Path to directory containing CA certificate files to validate the server's certificate.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ca_<wbr>cert_<wbr>file</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Path to a CA certificate file to validate the server's certificate.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>client_<wbr>auths</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#providerclientauth">List[Provider<wbr>Client<wbr>Auth]</a></span>
    </dt>
    <dd>{{% md %}}Client authentication credentials.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max_<wbr>lease_<wbr>ttl_<wbr>seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Maximum TTL for secret leases requested by this provider
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max_<wbr>retries</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Maximum number of retries when a 5xx error code is encountered.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The namespace to use. Available only for Vault Enterprise
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>skip_<wbr>tls_<wbr>verify</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Set this to true only if the target Vault server is an insecure development instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Token to use to authenticate to Vault.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Token name to use for creating the Vault child token.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}














## Supporting Types

<h4>Provider<wbr>Auth<wbr>Login</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/vault/types/input/#ProviderAuthLogin">input</a>   API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-vault/sdk/go/vault/?tab=doc#ProviderAuthLoginArgs">input</a>   API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Parameters</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Parameters</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>parameters</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>parameters</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>path</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Provider<wbr>Client<wbr>Auth</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/vault/types/input/#ProviderClientAuth">input</a>   API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-vault/sdk/go/vault/?tab=doc#ProviderClientAuthArgs">input</a>   API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Cert<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Key<wbr>File</span>
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
        <span>Cert<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Key<wbr>File</span>
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
        <span>cert<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>key<wbr>File</span>
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
        <span>cert<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>key<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}









<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-vault">https://github.com/pulumi/pulumi-vault</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    
</dl>

