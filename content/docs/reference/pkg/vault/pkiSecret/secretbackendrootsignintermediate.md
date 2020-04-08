
---
title: "SecretBackendRootSignIntermediate"
block_external_search_index: true
---






## Create a SecretBackendRootSignIntermediate Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/vault/pkiSecret/#SecretBackendRootSignIntermediate">SecretBackendRootSignIntermediate</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/vault/pkiSecret/#SecretBackendRootSignIntermediateArgs">SecretBackendRootSignIntermediateArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">SecretBackendRootSignIntermediate</span><span class="p">(resource_name, opts=None, </span>alt_names=None<span class="p">, </span>backend=None<span class="p">, </span>common_name=None<span class="p">, </span>country=None<span class="p">, </span>csr=None<span class="p">, </span>exclude_cn_from_sans=None<span class="p">, </span>format=None<span class="p">, </span>ip_sans=None<span class="p">, </span>locality=None<span class="p">, </span>max_path_length=None<span class="p">, </span>organization=None<span class="p">, </span>other_sans=None<span class="p">, </span>ou=None<span class="p">, </span>permitted_dns_domains=None<span class="p">, </span>postal_code=None<span class="p">, </span>province=None<span class="p">, </span>street_address=None<span class="p">, </span>ttl=None<span class="p">, </span>uri_sans=None<span class="p">, </span>use_csr_values=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewSecretBackendRootSignIntermediate<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-vault/sdk/go/vault/pkiSecret?tab=doc#SecretBackendRootSignIntermediateArgs">SecretBackendRootSignIntermediateArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-vault/sdk/go/vault/pkiSecret?tab=doc#SecretBackendRootSignIntermediate">SecretBackendRootSignIntermediate</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Vault/Pulumi.Vault.PkiSecret.SecretBackendRootSignIntermediate.html">SecretBackendRootSignIntermediate</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Vault/Pulumi.Vault.PkiSecret.SecretBackendRootSignIntermediateArgs.html">SecretBackendRootSignIntermediateArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Alt<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of alternative names.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The PKI secret backend the resource belongs to.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Common<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}CN of intermediate to create.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Country</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The country.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Csr</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The CSR.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Exclude<wbr>Cn<wbr>From<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to exclude CN from SANs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Format</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The format of data.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ip<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of alternative IPs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Locality</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The locality.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Path<wbr>Length</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The maximum path length to encode in the generated certificate.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Organization</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The organization.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Other<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of other SANs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ou</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The organization unit.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Permitted<wbr>Dns<wbr>Domains</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of domains for which certificates are allowed to be issued.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Postal<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The postal code.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Province</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The province.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Street<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The street address.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Time to leave.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Uri<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of alterative URIs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Use<wbr>Csr<wbr>Values</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Preserve CSR values.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Alt<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of alternative names.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The PKI secret backend the resource belongs to.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Common<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}CN of intermediate to create.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Country</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The country.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Csr</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The CSR.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Exclude<wbr>Cn<wbr>From<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to exclude CN from SANs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Format</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The format of data.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ip<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of alternative IPs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Locality</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The locality.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Path<wbr>Length</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The maximum path length to encode in the generated certificate.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Organization</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The organization.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Other<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of other SANs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ou</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The organization unit.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Permitted<wbr>Dns<wbr>Domains</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of domains for which certificates are allowed to be issued.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Postal<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The postal code.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Province</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The province.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Street<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The street address.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Time to leave.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Uri<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of alterative URIs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Use<wbr>Csr<wbr>Values</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Preserve CSR values.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>alt<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of alternative names.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The PKI secret backend the resource belongs to.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>common<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}CN of intermediate to create.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>country</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The country.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>csr</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The CSR.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>exclude<wbr>Cn<wbr>From<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to exclude CN from SANs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>format</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The format of data.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ip<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of alternative IPs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>locality</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The locality.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Path<wbr>Length</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum path length to encode in the generated certificate.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>organization</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The organization.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>other<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of other SANs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ou</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The organization unit.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>permitted<wbr>Dns<wbr>Domains</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of domains for which certificates are allowed to be issued.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>postal<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The postal code.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>province</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The province.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>street<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The street address.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Time to leave.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>uri<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of alterative URIs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>use<wbr>Csr<wbr>Values</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Preserve CSR values.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>alt_<wbr>names</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of alternative names.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The PKI secret backend the resource belongs to.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>common_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}CN of intermediate to create.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>country</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The country.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>csr</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The CSR.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>exclude_<wbr>cn_<wbr>from_<wbr>sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to exclude CN from SANs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>format</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The format of data.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ip_<wbr>sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of alternative IPs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>locality</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The locality.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max_<wbr>path_<wbr>length</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum path length to encode in the generated certificate.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>organization</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The organization.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>other_<wbr>sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of other SANs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ou</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The organization unit.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>permitted_<wbr>dns_<wbr>domains</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of domains for which certificates are allowed to be issued.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>postal_<wbr>code</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The postal code.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>province</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The province.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>street_<wbr>address</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The street address.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Time to leave.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>uri_<wbr>sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of alterative URIs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>use_<wbr>csr_<wbr>values</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Preserve CSR values.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## SecretBackendRootSignIntermediate Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Alt<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of alternative names.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The PKI secret backend the resource belongs to.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ca<wbr>Chain</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The CA chain.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The certicate.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Common<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}CN of intermediate to create.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Country</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The country.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Csr</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The CSR.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Exclude<wbr>Cn<wbr>From<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to exclude CN from SANs.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Format</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The format of data.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ip<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of alternative IPs.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Issuing<wbr>Ca</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The issuing CA.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Locality</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The locality.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Max<wbr>Path<wbr>Length</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The maximum path length to encode in the generated certificate.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Organization</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The organization.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Other<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of other SANs.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ou</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The organization unit.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Permitted<wbr>Dns<wbr>Domains</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of domains for which certificates are allowed to be issued.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Postal<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The postal code.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Province</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The province.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Serial</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The serial number.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Street<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The street address.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Time to leave.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Uri<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of alterative URIs.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Use<wbr>Csr<wbr>Values</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Preserve CSR values.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Alt<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of alternative names.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The PKI secret backend the resource belongs to.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ca<wbr>Chain</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The CA chain.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The certicate.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Common<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}CN of intermediate to create.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Country</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The country.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Csr</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The CSR.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Exclude<wbr>Cn<wbr>From<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to exclude CN from SANs.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Format</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The format of data.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ip<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of alternative IPs.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Issuing<wbr>Ca</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The issuing CA.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Locality</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The locality.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Max<wbr>Path<wbr>Length</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The maximum path length to encode in the generated certificate.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Organization</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The organization.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Other<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of other SANs.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ou</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The organization unit.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Permitted<wbr>Dns<wbr>Domains</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of domains for which certificates are allowed to be issued.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Postal<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The postal code.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Province</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The province.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Serial</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The serial number.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Street<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The street address.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Time to leave.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Uri<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of alterative URIs.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Use<wbr>Csr<wbr>Values</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Preserve CSR values.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>alt<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of alternative names.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The PKI secret backend the resource belongs to.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ca<wbr>Chain</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The CA chain.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The certicate.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>common<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}CN of intermediate to create.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>country</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The country.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>csr</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The CSR.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>exclude<wbr>Cn<wbr>From<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to exclude CN from SANs.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>format</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The format of data.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ip<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of alternative IPs.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>issuing<wbr>Ca</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The issuing CA.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>locality</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The locality.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>max<wbr>Path<wbr>Length</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum path length to encode in the generated certificate.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>organization</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The organization.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>other<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of other SANs.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ou</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The organization unit.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>permitted<wbr>Dns<wbr>Domains</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of domains for which certificates are allowed to be issued.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>postal<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The postal code.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>province</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The province.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>serial</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The serial number.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>street<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The street address.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Time to leave.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>uri<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of alterative URIs.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>use<wbr>Csr<wbr>Values</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Preserve CSR values.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>alt_<wbr>names</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of alternative names.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The PKI secret backend the resource belongs to.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ca_<wbr>chain</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The CA chain.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The certicate.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>common_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}CN of intermediate to create.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>country</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The country.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>csr</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The CSR.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>exclude_<wbr>cn_<wbr>from_<wbr>sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to exclude CN from SANs.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>format</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The format of data.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ip_<wbr>sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of alternative IPs.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>issuing_<wbr>ca</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The issuing CA.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>locality</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The locality.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>max_<wbr>path_<wbr>length</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum path length to encode in the generated certificate.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>organization</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The organization.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>other_<wbr>sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of other SANs.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ou</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The organization unit.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>permitted_<wbr>dns_<wbr>domains</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of domains for which certificates are allowed to be issued.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>postal_<wbr>code</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The postal code.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>province</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The province.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>serial</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The serial number.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>street_<wbr>address</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The street address.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Time to leave.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>uri_<wbr>sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of alterative URIs.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>use_<wbr>csr_<wbr>values</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Preserve CSR values.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing SecretBackendRootSignIntermediate Resource

Get an existing SecretBackendRootSignIntermediate resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/vault/pkiSecret/#SecretBackendRootSignIntermediateState">SecretBackendRootSignIntermediateState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/vault/pkiSecret/#SecretBackendRootSignIntermediate">SecretBackendRootSignIntermediate</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>alt_names=None<span class="p">, </span>backend=None<span class="p">, </span>ca_chain=None<span class="p">, </span>certificate=None<span class="p">, </span>common_name=None<span class="p">, </span>country=None<span class="p">, </span>csr=None<span class="p">, </span>exclude_cn_from_sans=None<span class="p">, </span>format=None<span class="p">, </span>ip_sans=None<span class="p">, </span>issuing_ca=None<span class="p">, </span>locality=None<span class="p">, </span>max_path_length=None<span class="p">, </span>organization=None<span class="p">, </span>other_sans=None<span class="p">, </span>ou=None<span class="p">, </span>permitted_dns_domains=None<span class="p">, </span>postal_code=None<span class="p">, </span>province=None<span class="p">, </span>serial=None<span class="p">, </span>street_address=None<span class="p">, </span>ttl=None<span class="p">, </span>uri_sans=None<span class="p">, </span>use_csr_values=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetSecretBackendRootSignIntermediate<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-vault/sdk/go/vault/pkiSecret?tab=doc#SecretBackendRootSignIntermediateState">SecretBackendRootSignIntermediateState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-vault/sdk/go/vault/pkiSecret?tab=doc#SecretBackendRootSignIntermediate">SecretBackendRootSignIntermediate</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Vault/Pulumi.Vault.PkiSecret.SecretBackendRootSignIntermediate.html">SecretBackendRootSignIntermediate</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Vault/Pulumi.Vault.PkiSecret.SecretBackendRootSignIntermediateState.html">SecretBackendRootSignIntermediateState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Alt<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of alternative names.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The PKI secret backend the resource belongs to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ca<wbr>Chain</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The CA chain.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The certicate.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Common<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}CN of intermediate to create.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Country</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The country.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Csr</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The CSR.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Exclude<wbr>Cn<wbr>From<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to exclude CN from SANs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Format</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The format of data.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ip<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of alternative IPs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Issuing<wbr>Ca</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The issuing CA.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Locality</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The locality.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Path<wbr>Length</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The maximum path length to encode in the generated certificate.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Organization</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The organization.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Other<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of other SANs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ou</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The organization unit.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Permitted<wbr>Dns<wbr>Domains</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of domains for which certificates are allowed to be issued.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Postal<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The postal code.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Province</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The province.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Serial</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The serial number.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Street<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The street address.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Time to leave.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Uri<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of alterative URIs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Use<wbr>Csr<wbr>Values</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Preserve CSR values.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Alt<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of alternative names.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The PKI secret backend the resource belongs to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ca<wbr>Chain</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The CA chain.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The certicate.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Common<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}CN of intermediate to create.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Country</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The country.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Csr</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The CSR.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Exclude<wbr>Cn<wbr>From<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to exclude CN from SANs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Format</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The format of data.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ip<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of alternative IPs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Issuing<wbr>Ca</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The issuing CA.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Locality</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The locality.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Path<wbr>Length</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The maximum path length to encode in the generated certificate.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Organization</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The organization.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Other<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of other SANs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ou</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The organization unit.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Permitted<wbr>Dns<wbr>Domains</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of domains for which certificates are allowed to be issued.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Postal<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The postal code.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Province</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The province.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Serial</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The serial number.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Street<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The street address.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Time to leave.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Uri<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of alterative URIs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Use<wbr>Csr<wbr>Values</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Preserve CSR values.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>alt<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of alternative names.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The PKI secret backend the resource belongs to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ca<wbr>Chain</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The CA chain.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The certicate.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>common<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}CN of intermediate to create.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>country</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The country.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>csr</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The CSR.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>exclude<wbr>Cn<wbr>From<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to exclude CN from SANs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>format</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The format of data.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ip<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of alternative IPs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>issuing<wbr>Ca</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The issuing CA.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>locality</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The locality.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Path<wbr>Length</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum path length to encode in the generated certificate.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>organization</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The organization.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>other<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of other SANs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ou</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The organization unit.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>permitted<wbr>Dns<wbr>Domains</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of domains for which certificates are allowed to be issued.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>postal<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The postal code.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>province</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The province.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>serial</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The serial number.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>street<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The street address.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Time to leave.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>uri<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of alterative URIs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>use<wbr>Csr<wbr>Values</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Preserve CSR values.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>alt_<wbr>names</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of alternative names.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The PKI secret backend the resource belongs to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ca_<wbr>chain</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The CA chain.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The certicate.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>common_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}CN of intermediate to create.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>country</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The country.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>csr</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The CSR.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>exclude_<wbr>cn_<wbr>from_<wbr>sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to exclude CN from SANs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>format</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The format of data.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ip_<wbr>sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of alternative IPs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>issuing_<wbr>ca</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The issuing CA.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>locality</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The locality.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max_<wbr>path_<wbr>length</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum path length to encode in the generated certificate.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>organization</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The organization.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>other_<wbr>sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of other SANs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ou</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The organization unit.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>permitted_<wbr>dns_<wbr>domains</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of domains for which certificates are allowed to be issued.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>postal_<wbr>code</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The postal code.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>province</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The province.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>serial</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The serial number.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>street_<wbr>address</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The street address.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Time to leave.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>uri_<wbr>sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of alterative URIs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>use_<wbr>csr_<wbr>values</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Preserve CSR values.
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

