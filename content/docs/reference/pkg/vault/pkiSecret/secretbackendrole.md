
---
title: "SecretBackendRole"
block_external_search_index: true
---






## Create a SecretBackendRole Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/vault/pkiSecret/#SecretBackendRole">SecretBackendRole</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/vault/pkiSecret/#SecretBackendRoleArgs">SecretBackendRoleArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">SecretBackendRole</span><span class="p">(resource_name, opts=None, </span>allow_any_name=None<span class="p">, </span>allow_bare_domains=None<span class="p">, </span>allow_glob_domains=None<span class="p">, </span>allow_ip_sans=None<span class="p">, </span>allow_localhost=None<span class="p">, </span>allow_subdomains=None<span class="p">, </span>allowed_domains=None<span class="p">, </span>allowed_other_sans=None<span class="p">, </span>allowed_uri_sans=None<span class="p">, </span>backend=None<span class="p">, </span>basic_constraints_valid_for_non_ca=None<span class="p">, </span>client_flag=None<span class="p">, </span>code_signing_flag=None<span class="p">, </span>countries=None<span class="p">, </span>email_protection_flag=None<span class="p">, </span>enforce_hostnames=None<span class="p">, </span>ext_key_usages=None<span class="p">, </span>generate_lease=None<span class="p">, </span>key_bits=None<span class="p">, </span>key_type=None<span class="p">, </span>key_usages=None<span class="p">, </span>localities=None<span class="p">, </span>max_ttl=None<span class="p">, </span>name=None<span class="p">, </span>no_store=None<span class="p">, </span>not_before_duration=None<span class="p">, </span>organization_unit=None<span class="p">, </span>organizations=None<span class="p">, </span>policy_identifiers=None<span class="p">, </span>postal_codes=None<span class="p">, </span>provinces=None<span class="p">, </span>require_cn=None<span class="p">, </span>server_flag=None<span class="p">, </span>street_addresses=None<span class="p">, </span>ttl=None<span class="p">, </span>use_csr_common_name=None<span class="p">, </span>use_csr_sans=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewSecretBackendRole<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-vault/sdk/go/vault/pkiSecret?tab=doc#SecretBackendRoleArgs">SecretBackendRoleArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-vault/sdk/go/vault/pkiSecret?tab=doc#SecretBackendRole">SecretBackendRole</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Vault/Pulumi.Vault.PkiSecret.SecretBackendRole.html">SecretBackendRole</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Vault/Pulumi.Vault.PkiSecret.SecretBackendRoleArgs.html">SecretBackendRoleArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Allow<wbr>Any<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to allow any name
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Bare<wbr>Domains</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to allow certificates matching the actual domain.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Glob<wbr>Domains</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to allow names containing glob patterns.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Ip<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to allow IP SANs
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Localhost</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to allow certificates for localhost.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Subdomains</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to allow certificates matching subdomains.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allowed<wbr>Domains</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The domains of the role.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allowed<wbr>Other<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Defines allowed custom SANs
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allowed<wbr>Uri<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Defines allowed URI SANs
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The path of the PKI secret backend the resource belongs to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Basic<wbr>Constraints<wbr>Valid<wbr>For<wbr>Non<wbr>Ca</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to mark basic constraints valid when issuing non-CA certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Flag</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to specify certificates for client use.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Code<wbr>Signing<wbr>Flag</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to specify certificates for code signing use.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Countries</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The country of generated certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Email<wbr>Protection<wbr>Flag</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to specify certificates for email protection use.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enforce<wbr>Hostnames</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to allow only valid host names
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ext<wbr>Key<wbr>Usages</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Specify the allowed extended key usage constraint on issued certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Generate<wbr>Lease</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to generate leases with certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Key<wbr>Bits</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The number of bits of generated keys.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Key<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The type of generated keys.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Key<wbr>Usages</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Specify the allowed key usage constraint on issued certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Localities</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The locality of generated certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The maximum TTL.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Unique name for the role.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>No<wbr>Store</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to not store certificates in the storage backend.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Not<wbr>Before<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the duration by which to backdate the NotBefore property.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Organization<wbr>Unit</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The organization unit of generated certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Organizations</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The organization of generated certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Policy<wbr>Identifiers</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Specify the list of allowed policies IODs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Postal<wbr>Codes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The postal code of generated certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Provinces</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The province of generated certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Require<wbr>Cn</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to force CN usage.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Server<wbr>Flag</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to specify certificates for server use.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Street<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The street address of generated certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The TTL.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Use<wbr>Csr<wbr>Common<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to use the CN in the CSR.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Use<wbr>Csr<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to use the SANs in the CSR.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Any<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to allow any name
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Bare<wbr>Domains</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to allow certificates matching the actual domain.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Glob<wbr>Domains</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to allow names containing glob patterns.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Ip<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to allow IP SANs
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Localhost</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to allow certificates for localhost.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Subdomains</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to allow certificates matching subdomains.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allowed<wbr>Domains</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The domains of the role.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allowed<wbr>Other<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Defines allowed custom SANs
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allowed<wbr>Uri<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Defines allowed URI SANs
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The path of the PKI secret backend the resource belongs to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Basic<wbr>Constraints<wbr>Valid<wbr>For<wbr>Non<wbr>Ca</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to mark basic constraints valid when issuing non-CA certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Flag</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to specify certificates for client use.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Code<wbr>Signing<wbr>Flag</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to specify certificates for code signing use.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Countries</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The country of generated certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Email<wbr>Protection<wbr>Flag</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to specify certificates for email protection use.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enforce<wbr>Hostnames</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to allow only valid host names
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ext<wbr>Key<wbr>Usages</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Specify the allowed extended key usage constraint on issued certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Generate<wbr>Lease</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to generate leases with certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Key<wbr>Bits</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The number of bits of generated keys.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Key<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The type of generated keys.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Key<wbr>Usages</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Specify the allowed key usage constraint on issued certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Localities</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The locality of generated certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The maximum TTL.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Unique name for the role.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>No<wbr>Store</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to not store certificates in the storage backend.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Not<wbr>Before<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the duration by which to backdate the NotBefore property.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Organization<wbr>Unit</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The organization unit of generated certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Organizations</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The organization of generated certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Policy<wbr>Identifiers</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Specify the list of allowed policies IODs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Postal<wbr>Codes</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The postal code of generated certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Provinces</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The province of generated certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Require<wbr>Cn</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to force CN usage.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Server<wbr>Flag</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to specify certificates for server use.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Street<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The street address of generated certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The TTL.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Use<wbr>Csr<wbr>Common<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to use the CN in the CSR.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Use<wbr>Csr<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to use the SANs in the CSR.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Any<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to allow any name
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Bare<wbr>Domains</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to allow certificates matching the actual domain.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Glob<wbr>Domains</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to allow names containing glob patterns.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Ip<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to allow IP SANs
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Localhost</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to allow certificates for localhost.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Subdomains</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to allow certificates matching subdomains.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allowed<wbr>Domains</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The domains of the role.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allowed<wbr>Other<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Defines allowed custom SANs
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allowed<wbr>Uri<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Defines allowed URI SANs
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The path of the PKI secret backend the resource belongs to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>basic<wbr>Constraints<wbr>Valid<wbr>For<wbr>Non<wbr>Ca</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to mark basic constraints valid when issuing non-CA certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>client<wbr>Flag</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to specify certificates for client use.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>code<wbr>Signing<wbr>Flag</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to specify certificates for code signing use.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>countries</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The country of generated certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>email<wbr>Protection<wbr>Flag</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to specify certificates for email protection use.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enforce<wbr>Hostnames</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to allow only valid host names
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ext<wbr>Key<wbr>Usages</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Specify the allowed extended key usage constraint on issued certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>generate<wbr>Lease</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to generate leases with certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>key<wbr>Bits</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The number of bits of generated keys.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>key<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The type of generated keys.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>key<wbr>Usages</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Specify the allowed key usage constraint on issued certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>localities</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The locality of generated certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The maximum TTL.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Unique name for the role.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>no<wbr>Store</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to not store certificates in the storage backend.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>not<wbr>Before<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the duration by which to backdate the NotBefore property.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>organization<wbr>Unit</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The organization unit of generated certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>organizations</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The organization of generated certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>policy<wbr>Identifiers</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Specify the list of allowed policies IODs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>postal<wbr>Codes</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The postal code of generated certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>provinces</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The province of generated certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>require<wbr>Cn</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to force CN usage.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>server<wbr>Flag</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to specify certificates for server use.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>street<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The street address of generated certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The TTL.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>use<wbr>Csr<wbr>Common<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to use the CN in the CSR.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>use<wbr>Csr<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to use the SANs in the CSR.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>allow_<wbr>any_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to allow any name
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow_<wbr>bare_<wbr>domains</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to allow certificates matching the actual domain.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow_<wbr>glob_<wbr>domains</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to allow names containing glob patterns.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow_<wbr>ip_<wbr>sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to allow IP SANs
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow_<wbr>localhost</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to allow certificates for localhost.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow_<wbr>subdomains</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to allow certificates matching subdomains.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allowed_<wbr>domains</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The domains of the role.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allowed_<wbr>other_<wbr>sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Defines allowed custom SANs
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allowed_<wbr>uri_<wbr>sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Defines allowed URI SANs
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The path of the PKI secret backend the resource belongs to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>basic_<wbr>constraints_<wbr>valid_<wbr>for_<wbr>non_<wbr>ca</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to mark basic constraints valid when issuing non-CA certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>client_<wbr>flag</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to specify certificates for client use.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>code_<wbr>signing_<wbr>flag</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to specify certificates for code signing use.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>countries</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The country of generated certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>email_<wbr>protection_<wbr>flag</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to specify certificates for email protection use.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enforce_<wbr>hostnames</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to allow only valid host names
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ext_<wbr>key_<wbr>usages</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Specify the allowed extended key usage constraint on issued certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>generate_<wbr>lease</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to generate leases with certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>key_<wbr>bits</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The number of bits of generated keys.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>key_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The type of generated keys.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>key_<wbr>usages</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Specify the allowed key usage constraint on issued certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>localities</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The locality of generated certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max_<wbr>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The maximum TTL.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Unique name for the role.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>no_<wbr>store</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to not store certificates in the storage backend.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>not_<wbr>before_<wbr>duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the duration by which to backdate the NotBefore property.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>organization_<wbr>unit</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The organization unit of generated certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>organizations</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The organization of generated certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>policy_<wbr>identifiers</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Specify the list of allowed policies IODs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>postal_<wbr>codes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The postal code of generated certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>provinces</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The province of generated certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>require_<wbr>cn</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to force CN usage.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>server_<wbr>flag</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to specify certificates for server use.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>street_<wbr>addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The street address of generated certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The TTL.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>use_<wbr>csr_<wbr>common_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to use the CN in the CSR.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>use_<wbr>csr_<wbr>sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to use the SANs in the CSR.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## SecretBackendRole Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Allow<wbr>Any<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to allow any name
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Allow<wbr>Bare<wbr>Domains</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to allow certificates matching the actual domain.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Allow<wbr>Glob<wbr>Domains</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to allow names containing glob patterns.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Allow<wbr>Ip<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to allow IP SANs
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Allow<wbr>Localhost</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to allow certificates for localhost.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Allow<wbr>Subdomains</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to allow certificates matching subdomains.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Allowed<wbr>Domains</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The domains of the role.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Allowed<wbr>Other<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Defines allowed custom SANs
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Allowed<wbr>Uri<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Defines allowed URI SANs
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The path of the PKI secret backend the resource belongs to.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Basic<wbr>Constraints<wbr>Valid<wbr>For<wbr>Non<wbr>Ca</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to mark basic constraints valid when issuing non-CA certificates.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Client<wbr>Flag</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to specify certificates for client use.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Code<wbr>Signing<wbr>Flag</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to specify certificates for code signing use.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Countries</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The country of generated certificates.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Email<wbr>Protection<wbr>Flag</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to specify certificates for email protection use.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enforce<wbr>Hostnames</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to allow only valid host names
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ext<wbr>Key<wbr>Usages</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Specify the allowed extended key usage constraint on issued certificates.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Generate<wbr>Lease</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to generate leases with certificates.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Key<wbr>Bits</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The number of bits of generated keys.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Key<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The type of generated keys.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Key<wbr>Usages</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Specify the allowed key usage constraint on issued certificates.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Localities</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The locality of generated certificates.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The maximum TTL.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Unique name for the role.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>No<wbr>Store</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to not store certificates in the storage backend.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Not<wbr>Before<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the duration by which to backdate the NotBefore property.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Organization<wbr>Unit</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The organization unit of generated certificates.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Organizations</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The organization of generated certificates.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Policy<wbr>Identifiers</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Specify the list of allowed policies IODs.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Postal<wbr>Codes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The postal code of generated certificates.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Provinces</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The province of generated certificates.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Require<wbr>Cn</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to force CN usage.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Server<wbr>Flag</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to specify certificates for server use.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Street<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The street address of generated certificates.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The TTL.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Use<wbr>Csr<wbr>Common<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to use the CN in the CSR.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Use<wbr>Csr<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to use the SANs in the CSR.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Allow<wbr>Any<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to allow any name
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Allow<wbr>Bare<wbr>Domains</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to allow certificates matching the actual domain.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Allow<wbr>Glob<wbr>Domains</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to allow names containing glob patterns.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Allow<wbr>Ip<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to allow IP SANs
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Allow<wbr>Localhost</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to allow certificates for localhost.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Allow<wbr>Subdomains</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to allow certificates matching subdomains.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Allowed<wbr>Domains</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The domains of the role.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Allowed<wbr>Other<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Defines allowed custom SANs
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Allowed<wbr>Uri<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Defines allowed URI SANs
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The path of the PKI secret backend the resource belongs to.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Basic<wbr>Constraints<wbr>Valid<wbr>For<wbr>Non<wbr>Ca</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to mark basic constraints valid when issuing non-CA certificates.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Client<wbr>Flag</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to specify certificates for client use.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Code<wbr>Signing<wbr>Flag</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to specify certificates for code signing use.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Countries</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The country of generated certificates.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Email<wbr>Protection<wbr>Flag</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to specify certificates for email protection use.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enforce<wbr>Hostnames</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to allow only valid host names
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ext<wbr>Key<wbr>Usages</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Specify the allowed extended key usage constraint on issued certificates.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Generate<wbr>Lease</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to generate leases with certificates.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Key<wbr>Bits</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The number of bits of generated keys.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Key<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The type of generated keys.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Key<wbr>Usages</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Specify the allowed key usage constraint on issued certificates.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Localities</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The locality of generated certificates.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The maximum TTL.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Unique name for the role.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>No<wbr>Store</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to not store certificates in the storage backend.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Not<wbr>Before<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the duration by which to backdate the NotBefore property.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Organization<wbr>Unit</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The organization unit of generated certificates.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Organizations</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The organization of generated certificates.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Policy<wbr>Identifiers</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Specify the list of allowed policies IODs.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Postal<wbr>Codes</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The postal code of generated certificates.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Provinces</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The province of generated certificates.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Require<wbr>Cn</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to force CN usage.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Server<wbr>Flag</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to specify certificates for server use.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Street<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The street address of generated certificates.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The TTL.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Use<wbr>Csr<wbr>Common<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to use the CN in the CSR.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Use<wbr>Csr<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to use the SANs in the CSR.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>allow<wbr>Any<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to allow any name
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>allow<wbr>Bare<wbr>Domains</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to allow certificates matching the actual domain.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>allow<wbr>Glob<wbr>Domains</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to allow names containing glob patterns.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>allow<wbr>Ip<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to allow IP SANs
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>allow<wbr>Localhost</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to allow certificates for localhost.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>allow<wbr>Subdomains</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to allow certificates matching subdomains.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>allowed<wbr>Domains</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The domains of the role.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>allowed<wbr>Other<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Defines allowed custom SANs
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>allowed<wbr>Uri<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Defines allowed URI SANs
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The path of the PKI secret backend the resource belongs to.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>basic<wbr>Constraints<wbr>Valid<wbr>For<wbr>Non<wbr>Ca</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to mark basic constraints valid when issuing non-CA certificates.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>client<wbr>Flag</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to specify certificates for client use.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>code<wbr>Signing<wbr>Flag</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to specify certificates for code signing use.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>countries</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The country of generated certificates.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>email<wbr>Protection<wbr>Flag</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to specify certificates for email protection use.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enforce<wbr>Hostnames</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to allow only valid host names
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ext<wbr>Key<wbr>Usages</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Specify the allowed extended key usage constraint on issued certificates.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>generate<wbr>Lease</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to generate leases with certificates.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>key<wbr>Bits</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The number of bits of generated keys.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>key<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The type of generated keys.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>key<wbr>Usages</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Specify the allowed key usage constraint on issued certificates.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>localities</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The locality of generated certificates.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The maximum TTL.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Unique name for the role.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>no<wbr>Store</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to not store certificates in the storage backend.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>not<wbr>Before<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the duration by which to backdate the NotBefore property.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>organization<wbr>Unit</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The organization unit of generated certificates.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>organizations</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The organization of generated certificates.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>policy<wbr>Identifiers</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Specify the list of allowed policies IODs.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>postal<wbr>Codes</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The postal code of generated certificates.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>provinces</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The province of generated certificates.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>require<wbr>Cn</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to force CN usage.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>server<wbr>Flag</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to specify certificates for server use.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>street<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The street address of generated certificates.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The TTL.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>use<wbr>Csr<wbr>Common<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to use the CN in the CSR.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>use<wbr>Csr<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to use the SANs in the CSR.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>allow_<wbr>any_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to allow any name
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>allow_<wbr>bare_<wbr>domains</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to allow certificates matching the actual domain.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>allow_<wbr>glob_<wbr>domains</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to allow names containing glob patterns.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>allow_<wbr>ip_<wbr>sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to allow IP SANs
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>allow_<wbr>localhost</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to allow certificates for localhost.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>allow_<wbr>subdomains</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to allow certificates matching subdomains.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>allowed_<wbr>domains</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The domains of the role.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>allowed_<wbr>other_<wbr>sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Defines allowed custom SANs
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>allowed_<wbr>uri_<wbr>sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Defines allowed URI SANs
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The path of the PKI secret backend the resource belongs to.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>basic_<wbr>constraints_<wbr>valid_<wbr>for_<wbr>non_<wbr>ca</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to mark basic constraints valid when issuing non-CA certificates.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>client_<wbr>flag</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to specify certificates for client use.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>code_<wbr>signing_<wbr>flag</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to specify certificates for code signing use.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>countries</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The country of generated certificates.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>email_<wbr>protection_<wbr>flag</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to specify certificates for email protection use.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enforce_<wbr>hostnames</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to allow only valid host names
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ext_<wbr>key_<wbr>usages</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Specify the allowed extended key usage constraint on issued certificates.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>generate_<wbr>lease</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to generate leases with certificates.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>key_<wbr>bits</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The number of bits of generated keys.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>key_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The type of generated keys.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>key_<wbr>usages</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Specify the allowed key usage constraint on issued certificates.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>localities</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The locality of generated certificates.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>max_<wbr>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The maximum TTL.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Unique name for the role.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>no_<wbr>store</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to not store certificates in the storage backend.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>not_<wbr>before_<wbr>duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the duration by which to backdate the NotBefore property.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>organization_<wbr>unit</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The organization unit of generated certificates.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>organizations</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The organization of generated certificates.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>policy_<wbr>identifiers</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Specify the list of allowed policies IODs.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>postal_<wbr>codes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The postal code of generated certificates.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>provinces</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The province of generated certificates.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>require_<wbr>cn</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to force CN usage.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>server_<wbr>flag</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to specify certificates for server use.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>street_<wbr>addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The street address of generated certificates.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The TTL.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>use_<wbr>csr_<wbr>common_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to use the CN in the CSR.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>use_<wbr>csr_<wbr>sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to use the SANs in the CSR.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing SecretBackendRole Resource

Get an existing SecretBackendRole resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/vault/pkiSecret/#SecretBackendRoleState">SecretBackendRoleState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/vault/pkiSecret/#SecretBackendRole">SecretBackendRole</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>allow_any_name=None<span class="p">, </span>allow_bare_domains=None<span class="p">, </span>allow_glob_domains=None<span class="p">, </span>allow_ip_sans=None<span class="p">, </span>allow_localhost=None<span class="p">, </span>allow_subdomains=None<span class="p">, </span>allowed_domains=None<span class="p">, </span>allowed_other_sans=None<span class="p">, </span>allowed_uri_sans=None<span class="p">, </span>backend=None<span class="p">, </span>basic_constraints_valid_for_non_ca=None<span class="p">, </span>client_flag=None<span class="p">, </span>code_signing_flag=None<span class="p">, </span>countries=None<span class="p">, </span>email_protection_flag=None<span class="p">, </span>enforce_hostnames=None<span class="p">, </span>ext_key_usages=None<span class="p">, </span>generate_lease=None<span class="p">, </span>key_bits=None<span class="p">, </span>key_type=None<span class="p">, </span>key_usages=None<span class="p">, </span>localities=None<span class="p">, </span>max_ttl=None<span class="p">, </span>name=None<span class="p">, </span>no_store=None<span class="p">, </span>not_before_duration=None<span class="p">, </span>organization_unit=None<span class="p">, </span>organizations=None<span class="p">, </span>policy_identifiers=None<span class="p">, </span>postal_codes=None<span class="p">, </span>provinces=None<span class="p">, </span>require_cn=None<span class="p">, </span>server_flag=None<span class="p">, </span>street_addresses=None<span class="p">, </span>ttl=None<span class="p">, </span>use_csr_common_name=None<span class="p">, </span>use_csr_sans=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetSecretBackendRole<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-vault/sdk/go/vault/pkiSecret?tab=doc#SecretBackendRoleState">SecretBackendRoleState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-vault/sdk/go/vault/pkiSecret?tab=doc#SecretBackendRole">SecretBackendRole</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Vault/Pulumi.Vault.PkiSecret.SecretBackendRole.html">SecretBackendRole</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Vault/Pulumi.Vault.PkiSecret.SecretBackendRoleState.html">SecretBackendRoleState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Allow<wbr>Any<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to allow any name
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Bare<wbr>Domains</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to allow certificates matching the actual domain.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Glob<wbr>Domains</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to allow names containing glob patterns.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Ip<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to allow IP SANs
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Localhost</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to allow certificates for localhost.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Subdomains</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to allow certificates matching subdomains.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allowed<wbr>Domains</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The domains of the role.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allowed<wbr>Other<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Defines allowed custom SANs
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allowed<wbr>Uri<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Defines allowed URI SANs
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The path of the PKI secret backend the resource belongs to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Basic<wbr>Constraints<wbr>Valid<wbr>For<wbr>Non<wbr>Ca</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to mark basic constraints valid when issuing non-CA certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Flag</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to specify certificates for client use.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Code<wbr>Signing<wbr>Flag</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to specify certificates for code signing use.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Countries</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The country of generated certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Email<wbr>Protection<wbr>Flag</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to specify certificates for email protection use.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enforce<wbr>Hostnames</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to allow only valid host names
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ext<wbr>Key<wbr>Usages</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Specify the allowed extended key usage constraint on issued certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Generate<wbr>Lease</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to generate leases with certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Key<wbr>Bits</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The number of bits of generated keys.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Key<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The type of generated keys.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Key<wbr>Usages</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Specify the allowed key usage constraint on issued certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Localities</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The locality of generated certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The maximum TTL.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Unique name for the role.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>No<wbr>Store</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to not store certificates in the storage backend.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Not<wbr>Before<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the duration by which to backdate the NotBefore property.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Organization<wbr>Unit</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The organization unit of generated certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Organizations</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The organization of generated certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Policy<wbr>Identifiers</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Specify the list of allowed policies IODs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Postal<wbr>Codes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The postal code of generated certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Provinces</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The province of generated certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Require<wbr>Cn</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to force CN usage.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Server<wbr>Flag</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to specify certificates for server use.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Street<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The street address of generated certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The TTL.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Use<wbr>Csr<wbr>Common<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to use the CN in the CSR.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Use<wbr>Csr<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to use the SANs in the CSR.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Any<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to allow any name
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Bare<wbr>Domains</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to allow certificates matching the actual domain.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Glob<wbr>Domains</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to allow names containing glob patterns.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Ip<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to allow IP SANs
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Localhost</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to allow certificates for localhost.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Subdomains</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to allow certificates matching subdomains.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allowed<wbr>Domains</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The domains of the role.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allowed<wbr>Other<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Defines allowed custom SANs
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allowed<wbr>Uri<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Defines allowed URI SANs
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The path of the PKI secret backend the resource belongs to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Basic<wbr>Constraints<wbr>Valid<wbr>For<wbr>Non<wbr>Ca</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to mark basic constraints valid when issuing non-CA certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Flag</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to specify certificates for client use.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Code<wbr>Signing<wbr>Flag</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to specify certificates for code signing use.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Countries</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The country of generated certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Email<wbr>Protection<wbr>Flag</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to specify certificates for email protection use.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enforce<wbr>Hostnames</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to allow only valid host names
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ext<wbr>Key<wbr>Usages</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Specify the allowed extended key usage constraint on issued certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Generate<wbr>Lease</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to generate leases with certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Key<wbr>Bits</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The number of bits of generated keys.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Key<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The type of generated keys.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Key<wbr>Usages</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Specify the allowed key usage constraint on issued certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Localities</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The locality of generated certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The maximum TTL.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Unique name for the role.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>No<wbr>Store</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to not store certificates in the storage backend.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Not<wbr>Before<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the duration by which to backdate the NotBefore property.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Organization<wbr>Unit</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The organization unit of generated certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Organizations</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The organization of generated certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Policy<wbr>Identifiers</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Specify the list of allowed policies IODs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Postal<wbr>Codes</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The postal code of generated certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Provinces</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The province of generated certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Require<wbr>Cn</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to force CN usage.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Server<wbr>Flag</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to specify certificates for server use.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Street<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The street address of generated certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The TTL.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Use<wbr>Csr<wbr>Common<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to use the CN in the CSR.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Use<wbr>Csr<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to use the SANs in the CSR.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Any<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to allow any name
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Bare<wbr>Domains</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to allow certificates matching the actual domain.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Glob<wbr>Domains</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to allow names containing glob patterns.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Ip<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to allow IP SANs
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Localhost</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to allow certificates for localhost.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Subdomains</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to allow certificates matching subdomains.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allowed<wbr>Domains</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The domains of the role.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allowed<wbr>Other<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Defines allowed custom SANs
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allowed<wbr>Uri<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Defines allowed URI SANs
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The path of the PKI secret backend the resource belongs to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>basic<wbr>Constraints<wbr>Valid<wbr>For<wbr>Non<wbr>Ca</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to mark basic constraints valid when issuing non-CA certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>client<wbr>Flag</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to specify certificates for client use.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>code<wbr>Signing<wbr>Flag</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to specify certificates for code signing use.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>countries</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The country of generated certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>email<wbr>Protection<wbr>Flag</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to specify certificates for email protection use.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enforce<wbr>Hostnames</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to allow only valid host names
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ext<wbr>Key<wbr>Usages</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Specify the allowed extended key usage constraint on issued certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>generate<wbr>Lease</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to generate leases with certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>key<wbr>Bits</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The number of bits of generated keys.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>key<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The type of generated keys.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>key<wbr>Usages</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Specify the allowed key usage constraint on issued certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>localities</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The locality of generated certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The maximum TTL.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Unique name for the role.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>no<wbr>Store</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to not store certificates in the storage backend.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>not<wbr>Before<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the duration by which to backdate the NotBefore property.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>organization<wbr>Unit</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The organization unit of generated certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>organizations</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The organization of generated certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>policy<wbr>Identifiers</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Specify the list of allowed policies IODs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>postal<wbr>Codes</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The postal code of generated certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>provinces</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The province of generated certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>require<wbr>Cn</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to force CN usage.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>server<wbr>Flag</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to specify certificates for server use.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>street<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The street address of generated certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The TTL.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>use<wbr>Csr<wbr>Common<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to use the CN in the CSR.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>use<wbr>Csr<wbr>Sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to use the SANs in the CSR.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>allow_<wbr>any_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to allow any name
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow_<wbr>bare_<wbr>domains</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to allow certificates matching the actual domain.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow_<wbr>glob_<wbr>domains</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to allow names containing glob patterns.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow_<wbr>ip_<wbr>sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to allow IP SANs
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow_<wbr>localhost</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to allow certificates for localhost.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow_<wbr>subdomains</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to allow certificates matching subdomains.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allowed_<wbr>domains</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The domains of the role.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allowed_<wbr>other_<wbr>sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Defines allowed custom SANs
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allowed_<wbr>uri_<wbr>sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Defines allowed URI SANs
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The path of the PKI secret backend the resource belongs to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>basic_<wbr>constraints_<wbr>valid_<wbr>for_<wbr>non_<wbr>ca</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to mark basic constraints valid when issuing non-CA certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>client_<wbr>flag</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to specify certificates for client use.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>code_<wbr>signing_<wbr>flag</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to specify certificates for code signing use.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>countries</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The country of generated certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>email_<wbr>protection_<wbr>flag</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to specify certificates for email protection use.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enforce_<wbr>hostnames</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to allow only valid host names
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ext_<wbr>key_<wbr>usages</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Specify the allowed extended key usage constraint on issued certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>generate_<wbr>lease</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to generate leases with certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>key_<wbr>bits</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The number of bits of generated keys.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>key_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The type of generated keys.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>key_<wbr>usages</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Specify the allowed key usage constraint on issued certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>localities</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The locality of generated certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max_<wbr>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The maximum TTL.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Unique name for the role.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>no_<wbr>store</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to not store certificates in the storage backend.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>not_<wbr>before_<wbr>duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the duration by which to backdate the NotBefore property.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>organization_<wbr>unit</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The organization unit of generated certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>organizations</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The organization of generated certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>policy_<wbr>identifiers</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Specify the list of allowed policies IODs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>postal_<wbr>codes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The postal code of generated certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>provinces</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The province of generated certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>require_<wbr>cn</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to force CN usage.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>server_<wbr>flag</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to specify certificates for server use.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>street_<wbr>addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The street address of generated certificates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The TTL.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>use_<wbr>csr_<wbr>common_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to use the CN in the CSR.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>use_<wbr>csr_<wbr>sans</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to use the SANs in the CSR.
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

