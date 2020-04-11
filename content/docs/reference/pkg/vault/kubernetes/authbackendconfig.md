
---
title: "AuthBackendConfig"
block_external_search_index: true
---






## Create a AuthBackendConfig Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/vault/kubernetes/#AuthBackendConfig">AuthBackendConfig</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/vault/kubernetes/#AuthBackendConfigArgs">AuthBackendConfigArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">AuthBackendConfig</span><span class="p">(resource_name, opts=None, </span>backend=None<span class="p">, </span>issuer=None<span class="p">, </span>kubernetes_ca_cert=None<span class="p">, </span>kubernetes_host=None<span class="p">, </span>pem_keys=None<span class="p">, </span>token_reviewer_jwt=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewAuthBackendConfig<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-vault/sdk/go/vault/kubernetes?tab=doc#AuthBackendConfigArgs">AuthBackendConfigArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-vault/sdk/go/vault/kubernetes?tab=doc#AuthBackendConfig">AuthBackendConfig</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Vault/Pulumi.Vault.Kubernetes.AuthBackendConfig.html">AuthBackendConfig</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Vault/Pulumi.Vault.Kubernetes.AuthBackendConfigArgs.html">AuthBackendConfigArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Unique name of the kubernetes backend to configure.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Issuer</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Optional JWT issuer. If no issuer is specified, kubernetes.io/serviceaccount will be used as the default issuer.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kubernetes<wbr>Ca<wbr>Cert</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}PEM encoded CA cert for use by the TLS client used to talk with the Kubernetes API.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Kubernetes<wbr>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Host must be a host string, a host:port pair, or a URL to the base of the Kubernetes API server.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pem<wbr>Keys</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Optional list of PEM-formatted public keys or certificates used to verify the signatures of Kubernetes service account
JWTs. If a certificate is given, its public key will be extracted. Not every installation of Kubernetes exposes these
keys.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Reviewer<wbr>Jwt</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A service account JWT used to access the TokenReview API to validate other JWTs during login. If not set the JWT used
for login will be used to access the API.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Unique name of the kubernetes backend to configure.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Issuer</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Optional JWT issuer. If no issuer is specified, kubernetes.io/serviceaccount will be used as the default issuer.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kubernetes<wbr>Ca<wbr>Cert</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}PEM encoded CA cert for use by the TLS client used to talk with the Kubernetes API.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Kubernetes<wbr>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Host must be a host string, a host:port pair, or a URL to the base of the Kubernetes API server.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pem<wbr>Keys</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Optional list of PEM-formatted public keys or certificates used to verify the signatures of Kubernetes service account
JWTs. If a certificate is given, its public key will be extracted. Not every installation of Kubernetes exposes these
keys.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Reviewer<wbr>Jwt</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A service account JWT used to access the TokenReview API to validate other JWTs during login. If not set the JWT used
for login will be used to access the API.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Unique name of the kubernetes backend to configure.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>issuer</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Optional JWT issuer. If no issuer is specified, kubernetes.io/serviceaccount will be used as the default issuer.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kubernetes<wbr>Ca<wbr>Cert</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}PEM encoded CA cert for use by the TLS client used to talk with the Kubernetes API.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>kubernetes<wbr>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Host must be a host string, a host:port pair, or a URL to the base of the Kubernetes API server.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pem<wbr>Keys</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Optional list of PEM-formatted public keys or certificates used to verify the signatures of Kubernetes service account
JWTs. If a certificate is given, its public key will be extracted. Not every installation of Kubernetes exposes these
keys.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token<wbr>Reviewer<wbr>Jwt</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A service account JWT used to access the TokenReview API to validate other JWTs during login. If not set the JWT used
for login will be used to access the API.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Unique name of the kubernetes backend to configure.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>issuer</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Optional JWT issuer. If no issuer is specified, kubernetes.io/serviceaccount will be used as the default issuer.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kubernetes_<wbr>ca_<wbr>cert</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}PEM encoded CA cert for use by the TLS client used to talk with the Kubernetes API.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>kubernetes_<wbr>host</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Host must be a host string, a host:port pair, or a URL to the base of the Kubernetes API server.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pem_<wbr>keys</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Optional list of PEM-formatted public keys or certificates used to verify the signatures of Kubernetes service account
JWTs. If a certificate is given, its public key will be extracted. Not every installation of Kubernetes exposes these
keys.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token_<wbr>reviewer_<wbr>jwt</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A service account JWT used to access the TokenReview API to validate other JWTs during login. If not set the JWT used
for login will be used to access the API.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## AuthBackendConfig Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Unique name of the kubernetes backend to configure.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Issuer</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Optional JWT issuer. If no issuer is specified, kubernetes.io/serviceaccount will be used as the default issuer.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Kubernetes<wbr>Ca<wbr>Cert</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}PEM encoded CA cert for use by the TLS client used to talk with the Kubernetes API.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Kubernetes<wbr>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Host must be a host string, a host:port pair, or a URL to the base of the Kubernetes API server.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Pem<wbr>Keys</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Optional list of PEM-formatted public keys or certificates used to verify the signatures of Kubernetes service account
JWTs. If a certificate is given, its public key will be extracted. Not every installation of Kubernetes exposes these
keys.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Token<wbr>Reviewer<wbr>Jwt</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A service account JWT used to access the TokenReview API to validate other JWTs during login. If not set the JWT used
for login will be used to access the API.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Unique name of the kubernetes backend to configure.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Issuer</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Optional JWT issuer. If no issuer is specified, kubernetes.io/serviceaccount will be used as the default issuer.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Kubernetes<wbr>Ca<wbr>Cert</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}PEM encoded CA cert for use by the TLS client used to talk with the Kubernetes API.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Kubernetes<wbr>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Host must be a host string, a host:port pair, or a URL to the base of the Kubernetes API server.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Pem<wbr>Keys</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Optional list of PEM-formatted public keys or certificates used to verify the signatures of Kubernetes service account
JWTs. If a certificate is given, its public key will be extracted. Not every installation of Kubernetes exposes these
keys.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Token<wbr>Reviewer<wbr>Jwt</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A service account JWT used to access the TokenReview API to validate other JWTs during login. If not set the JWT used
for login will be used to access the API.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Unique name of the kubernetes backend to configure.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>issuer</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Optional JWT issuer. If no issuer is specified, kubernetes.io/serviceaccount will be used as the default issuer.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>kubernetes<wbr>Ca<wbr>Cert</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}PEM encoded CA cert for use by the TLS client used to talk with the Kubernetes API.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>kubernetes<wbr>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Host must be a host string, a host:port pair, or a URL to the base of the Kubernetes API server.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>pem<wbr>Keys</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Optional list of PEM-formatted public keys or certificates used to verify the signatures of Kubernetes service account
JWTs. If a certificate is given, its public key will be extracted. Not every installation of Kubernetes exposes these
keys.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>token<wbr>Reviewer<wbr>Jwt</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A service account JWT used to access the TokenReview API to validate other JWTs during login. If not set the JWT used
for login will be used to access the API.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Unique name of the kubernetes backend to configure.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>issuer</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Optional JWT issuer. If no issuer is specified, kubernetes.io/serviceaccount will be used as the default issuer.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>kubernetes_<wbr>ca_<wbr>cert</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}PEM encoded CA cert for use by the TLS client used to talk with the Kubernetes API.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>kubernetes_<wbr>host</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Host must be a host string, a host:port pair, or a URL to the base of the Kubernetes API server.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>pem_<wbr>keys</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Optional list of PEM-formatted public keys or certificates used to verify the signatures of Kubernetes service account
JWTs. If a certificate is given, its public key will be extracted. Not every installation of Kubernetes exposes these
keys.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>token_<wbr>reviewer_<wbr>jwt</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A service account JWT used to access the TokenReview API to validate other JWTs during login. If not set the JWT used
for login will be used to access the API.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing AuthBackendConfig Resource

Get an existing AuthBackendConfig resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/vault/kubernetes/#AuthBackendConfigState">AuthBackendConfigState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/vault/kubernetes/#AuthBackendConfig">AuthBackendConfig</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>backend=None<span class="p">, </span>issuer=None<span class="p">, </span>kubernetes_ca_cert=None<span class="p">, </span>kubernetes_host=None<span class="p">, </span>pem_keys=None<span class="p">, </span>token_reviewer_jwt=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetAuthBackendConfig<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-vault/sdk/go/vault/kubernetes?tab=doc#AuthBackendConfigState">AuthBackendConfigState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-vault/sdk/go/vault/kubernetes?tab=doc#AuthBackendConfig">AuthBackendConfig</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Vault/Pulumi.Vault.Kubernetes.AuthBackendConfig.html">AuthBackendConfig</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Vault/Pulumi.Vault.Kubernetes.AuthBackendConfigState.html">AuthBackendConfigState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Unique name of the kubernetes backend to configure.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Issuer</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Optional JWT issuer. If no issuer is specified, kubernetes.io/serviceaccount will be used as the default issuer.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kubernetes<wbr>Ca<wbr>Cert</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}PEM encoded CA cert for use by the TLS client used to talk with the Kubernetes API.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kubernetes<wbr>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Host must be a host string, a host:port pair, or a URL to the base of the Kubernetes API server.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pem<wbr>Keys</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Optional list of PEM-formatted public keys or certificates used to verify the signatures of Kubernetes service account
JWTs. If a certificate is given, its public key will be extracted. Not every installation of Kubernetes exposes these
keys.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Reviewer<wbr>Jwt</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A service account JWT used to access the TokenReview API to validate other JWTs during login. If not set the JWT used
for login will be used to access the API.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Unique name of the kubernetes backend to configure.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Issuer</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Optional JWT issuer. If no issuer is specified, kubernetes.io/serviceaccount will be used as the default issuer.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kubernetes<wbr>Ca<wbr>Cert</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}PEM encoded CA cert for use by the TLS client used to talk with the Kubernetes API.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kubernetes<wbr>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Host must be a host string, a host:port pair, or a URL to the base of the Kubernetes API server.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pem<wbr>Keys</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Optional list of PEM-formatted public keys or certificates used to verify the signatures of Kubernetes service account
JWTs. If a certificate is given, its public key will be extracted. Not every installation of Kubernetes exposes these
keys.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Reviewer<wbr>Jwt</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A service account JWT used to access the TokenReview API to validate other JWTs during login. If not set the JWT used
for login will be used to access the API.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Unique name of the kubernetes backend to configure.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>issuer</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Optional JWT issuer. If no issuer is specified, kubernetes.io/serviceaccount will be used as the default issuer.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kubernetes<wbr>Ca<wbr>Cert</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}PEM encoded CA cert for use by the TLS client used to talk with the Kubernetes API.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kubernetes<wbr>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Host must be a host string, a host:port pair, or a URL to the base of the Kubernetes API server.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pem<wbr>Keys</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Optional list of PEM-formatted public keys or certificates used to verify the signatures of Kubernetes service account
JWTs. If a certificate is given, its public key will be extracted. Not every installation of Kubernetes exposes these
keys.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token<wbr>Reviewer<wbr>Jwt</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A service account JWT used to access the TokenReview API to validate other JWTs during login. If not set the JWT used
for login will be used to access the API.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Unique name of the kubernetes backend to configure.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>issuer</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Optional JWT issuer. If no issuer is specified, kubernetes.io/serviceaccount will be used as the default issuer.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kubernetes_<wbr>ca_<wbr>cert</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}PEM encoded CA cert for use by the TLS client used to talk with the Kubernetes API.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kubernetes_<wbr>host</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Host must be a host string, a host:port pair, or a URL to the base of the Kubernetes API server.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pem_<wbr>keys</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Optional list of PEM-formatted public keys or certificates used to verify the signatures of Kubernetes service account
JWTs. If a certificate is given, its public key will be extracted. Not every installation of Kubernetes exposes these
keys.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token_<wbr>reviewer_<wbr>jwt</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A service account JWT used to access the TokenReview API to validate other JWTs during login. If not set the JWT used
for login will be used to access the API.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}











<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-vault">https://github.com/pulumi/pulumi-vault</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    
</dl>

