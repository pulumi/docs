
---
title: "AuthBackendRole"
block_external_search_index: true
---






## Create a AuthBackendRole Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/vault/kubernetes/#AuthBackendRole">AuthBackendRole</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/vault/kubernetes/#AuthBackendRoleArgs">AuthBackendRoleArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">AuthBackendRole</span><span class="p">(resource_name, opts=None, </span>audience=None<span class="p">, </span>backend=None<span class="p">, </span>bound_cidrs=None<span class="p">, </span>bound_service_account_names=None<span class="p">, </span>bound_service_account_namespaces=None<span class="p">, </span>max_ttl=None<span class="p">, </span>num_uses=None<span class="p">, </span>period=None<span class="p">, </span>policies=None<span class="p">, </span>role_name=None<span class="p">, </span>token_bound_cidrs=None<span class="p">, </span>token_explicit_max_ttl=None<span class="p">, </span>token_max_ttl=None<span class="p">, </span>token_no_default_policy=None<span class="p">, </span>token_num_uses=None<span class="p">, </span>token_period=None<span class="p">, </span>token_policies=None<span class="p">, </span>token_ttl=None<span class="p">, </span>token_type=None<span class="p">, </span>ttl=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewAuthBackendRole<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-vault/sdk/go/vault/kubernetes?tab=doc#AuthBackendRoleArgs">AuthBackendRoleArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-vault/sdk/go/vault/kubernetes?tab=doc#AuthBackendRole">AuthBackendRole</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Vault/Pulumi.Vault.Kubernetes.AuthBackendRole.html">AuthBackendRole</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Vault/Pulumi.Vault.Kubernetes.AuthBackendRoleArgs.html">AuthBackendRoleArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Audience</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Optional Audience claim to verify in the JWT.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Unique name of the kubernetes backend to configure.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Bound<wbr>Cidrs</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of CIDRs valid as the source address for login requests. This value is also encoded into any resulting token.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_bound_cidrs` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-required"
            title="Required">
        <span>Bound<wbr>Service<wbr>Account<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}List of service account names able to access this role. If set to `["*"]` all names are allowed, both this and
bound_service_account_namespaces can not be "*".
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Bound<wbr>Service<wbr>Account<wbr>Namespaces</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}List of namespaces allowed to access this role. If set to `["*"]` all namespaces are allowed, both this and
bound_service_account_names can not be set to "*".
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Number of seconds after which issued tokens can no longer be renewed.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_max_ttl` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Num<wbr>Uses</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Number of times issued tokens can be used. Setting this to 0 or leaving it unset means unlimited uses.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_num_uses` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Number of seconds to set the TTL to for issued tokens upon renewal. Makes the token a periodic token, which will never
expire as long as it is renewed before the TTL each period.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_period` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Policies to be set on tokens issued using this role.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_policies` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-required"
            title="Required">
        <span>Role<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the role.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Bound<wbr>Cidrs</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Specifies the blocks of IP addresses which are allowed to use the generated token
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Explicit<wbr>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Generated Token's Explicit Maximum TTL in seconds
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The maximum lifetime of the generated token
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>No<wbr>Default<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If true, the 'default' policy will not automatically be added to generated tokens
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Num<wbr>Uses</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The maximum number of times a token may be used, a value of zero means unlimited
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Generated Token's Period
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Generated Token's Policies
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The initial ttl of the token to generate in seconds
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The type of token to generate, service or batch
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Default number of seconds to set as the TTL for issued tokens and at renewal time.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_ttl` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Audience</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Optional Audience claim to verify in the JWT.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Unique name of the kubernetes backend to configure.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Bound<wbr>Cidrs</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of CIDRs valid as the source address for login requests. This value is also encoded into any resulting token.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_bound_cidrs` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-required"
            title="Required">
        <span>Bound<wbr>Service<wbr>Account<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of service account names able to access this role. If set to `["*"]` all names are allowed, both this and
bound_service_account_namespaces can not be "*".
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Bound<wbr>Service<wbr>Account<wbr>Namespaces</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of namespaces allowed to access this role. If set to `["*"]` all namespaces are allowed, both this and
bound_service_account_names can not be set to "*".
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Number of seconds after which issued tokens can no longer be renewed.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_max_ttl` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Num<wbr>Uses</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Number of times issued tokens can be used. Setting this to 0 or leaving it unset means unlimited uses.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_num_uses` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Number of seconds to set the TTL to for issued tokens upon renewal. Makes the token a periodic token, which will never
expire as long as it is renewed before the TTL each period.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_period` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Policies to be set on tokens issued using this role.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_policies` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-required"
            title="Required">
        <span>Role<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the role.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Bound<wbr>Cidrs</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Specifies the blocks of IP addresses which are allowed to use the generated token
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Explicit<wbr>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Generated Token's Explicit Maximum TTL in seconds
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The maximum lifetime of the generated token
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>No<wbr>Default<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If true, the 'default' policy will not automatically be added to generated tokens
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Num<wbr>Uses</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The maximum number of times a token may be used, a value of zero means unlimited
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Generated Token's Period
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Generated Token's Policies
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The initial ttl of the token to generate in seconds
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The type of token to generate, service or batch
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Default number of seconds to set as the TTL for issued tokens and at renewal time.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_ttl` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>audience</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Optional Audience claim to verify in the JWT.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Unique name of the kubernetes backend to configure.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>bound<wbr>Cidrs</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of CIDRs valid as the source address for login requests. This value is also encoded into any resulting token.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_bound_cidrs` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-required"
            title="Required">
        <span>bound<wbr>Service<wbr>Account<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}List of service account names able to access this role. If set to `["*"]` all names are allowed, both this and
bound_service_account_namespaces can not be "*".
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>bound<wbr>Service<wbr>Account<wbr>Namespaces</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}List of namespaces allowed to access this role. If set to `["*"]` all namespaces are allowed, both this and
bound_service_account_names can not be set to "*".
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Number of seconds after which issued tokens can no longer be renewed.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_max_ttl` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>num<wbr>Uses</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Number of times issued tokens can be used. Setting this to 0 or leaving it unset means unlimited uses.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_num_uses` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Number of seconds to set the TTL to for issued tokens upon renewal. Makes the token a periodic token, which will never
expire as long as it is renewed before the TTL each period.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_period` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>policies</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Policies to be set on tokens issued using this role.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_policies` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-required"
            title="Required">
        <span>role<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the role.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token<wbr>Bound<wbr>Cidrs</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Specifies the blocks of IP addresses which are allowed to use the generated token
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token<wbr>Explicit<wbr>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Generated Token's Explicit Maximum TTL in seconds
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token<wbr>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum lifetime of the generated token
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token<wbr>No<wbr>Default<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If true, the 'default' policy will not automatically be added to generated tokens
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token<wbr>Num<wbr>Uses</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum number of times a token may be used, a value of zero means unlimited
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Generated Token's Period
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Generated Token's Policies
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The initial ttl of the token to generate in seconds
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The type of token to generate, service or batch
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Default number of seconds to set as the TTL for issued tokens and at renewal time.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_ttl` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>audience</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Optional Audience claim to verify in the JWT.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Unique name of the kubernetes backend to configure.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>bound_<wbr>cidrs</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of CIDRs valid as the source address for login requests. This value is also encoded into any resulting token.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_bound_cidrs` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-required"
            title="Required">
        <span>bound_<wbr>service_<wbr>account_<wbr>names</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of service account names able to access this role. If set to `["*"]` all names are allowed, both this and
bound_service_account_namespaces can not be "*".
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>bound_<wbr>service_<wbr>account_<wbr>namespaces</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of namespaces allowed to access this role. If set to `["*"]` all namespaces are allowed, both this and
bound_service_account_names can not be set to "*".
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>max_<wbr>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Number of seconds after which issued tokens can no longer be renewed.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_max_ttl` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>num_<wbr>uses</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Number of times issued tokens can be used. Setting this to 0 or leaving it unset means unlimited uses.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_num_uses` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Number of seconds to set the TTL to for issued tokens upon renewal. Makes the token a periodic token, which will never
expire as long as it is renewed before the TTL each period.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_period` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>policies</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Policies to be set on tokens issued using this role.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_policies` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-required"
            title="Required">
        <span>role_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the role.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token_<wbr>bound_<wbr>cidrs</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Specifies the blocks of IP addresses which are allowed to use the generated token
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token_<wbr>explicit_<wbr>max_<wbr>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Generated Token's Explicit Maximum TTL in seconds
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token_<wbr>max_<wbr>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum lifetime of the generated token
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token_<wbr>no_<wbr>default_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If true, the 'default' policy will not automatically be added to generated tokens
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token_<wbr>num_<wbr>uses</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum number of times a token may be used, a value of zero means unlimited
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token_<wbr>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Generated Token's Period
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token_<wbr>policies</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Generated Token's Policies
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token_<wbr>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The initial ttl of the token to generate in seconds
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The type of token to generate, service or batch
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Default number of seconds to set as the TTL for issued tokens and at renewal time.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_ttl` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

</dl>
{{% /choosable %}}







## AuthBackendRole Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Audience</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Optional Audience claim to verify in the JWT.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Unique name of the kubernetes backend to configure.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Bound<wbr>Cidrs</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of CIDRs valid as the source address for login requests. This value is also encoded into any resulting token.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_bound_cidrs` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>Bound<wbr>Service<wbr>Account<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}List of service account names able to access this role. If set to `["*"]` all names are allowed, both this and
bound_service_account_namespaces can not be "*".
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Bound<wbr>Service<wbr>Account<wbr>Namespaces</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}List of namespaces allowed to access this role. If set to `["*"]` all namespaces are allowed, both this and
bound_service_account_names can not be set to "*".
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Number of seconds after which issued tokens can no longer be renewed.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_max_ttl` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Num<wbr>Uses</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Number of times issued tokens can be used. Setting this to 0 or leaving it unset means unlimited uses.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_num_uses` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Number of seconds to set the TTL to for issued tokens upon renewal. Makes the token a periodic token, which will never
expire as long as it is renewed before the TTL each period.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_period` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Policies to be set on tokens issued using this role.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_policies` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>Role<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the role.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Token<wbr>Bound<wbr>Cidrs</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Specifies the blocks of IP addresses which are allowed to use the generated token
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Token<wbr>Explicit<wbr>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Generated Token's Explicit Maximum TTL in seconds
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Token<wbr>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The maximum lifetime of the generated token
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Token<wbr>No<wbr>Default<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If true, the 'default' policy will not automatically be added to generated tokens
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Token<wbr>Num<wbr>Uses</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The maximum number of times a token may be used, a value of zero means unlimited
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Token<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Generated Token's Period
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Token<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Generated Token's Policies
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Token<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The initial ttl of the token to generate in seconds
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Token<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The type of token to generate, service or batch
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Default number of seconds to set as the TTL for issued tokens and at renewal time.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_ttl` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Audience</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Optional Audience claim to verify in the JWT.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Unique name of the kubernetes backend to configure.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Bound<wbr>Cidrs</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of CIDRs valid as the source address for login requests. This value is also encoded into any resulting token.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_bound_cidrs` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>Bound<wbr>Service<wbr>Account<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of service account names able to access this role. If set to `["*"]` all names are allowed, both this and
bound_service_account_namespaces can not be "*".
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Bound<wbr>Service<wbr>Account<wbr>Namespaces</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of namespaces allowed to access this role. If set to `["*"]` all namespaces are allowed, both this and
bound_service_account_names can not be set to "*".
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Number of seconds after which issued tokens can no longer be renewed.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_max_ttl` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Num<wbr>Uses</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Number of times issued tokens can be used. Setting this to 0 or leaving it unset means unlimited uses.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_num_uses` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Number of seconds to set the TTL to for issued tokens upon renewal. Makes the token a periodic token, which will never
expire as long as it is renewed before the TTL each period.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_period` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Policies to be set on tokens issued using this role.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_policies` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>Role<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the role.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Token<wbr>Bound<wbr>Cidrs</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Specifies the blocks of IP addresses which are allowed to use the generated token
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Token<wbr>Explicit<wbr>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Generated Token's Explicit Maximum TTL in seconds
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Token<wbr>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The maximum lifetime of the generated token
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Token<wbr>No<wbr>Default<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If true, the 'default' policy will not automatically be added to generated tokens
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Token<wbr>Num<wbr>Uses</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The maximum number of times a token may be used, a value of zero means unlimited
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Token<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Generated Token's Period
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Token<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Generated Token's Policies
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Token<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The initial ttl of the token to generate in seconds
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Token<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The type of token to generate, service or batch
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Default number of seconds to set as the TTL for issued tokens and at renewal time.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_ttl` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>audience</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Optional Audience claim to verify in the JWT.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Unique name of the kubernetes backend to configure.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>bound<wbr>Cidrs</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of CIDRs valid as the source address for login requests. This value is also encoded into any resulting token.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_bound_cidrs` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>bound<wbr>Service<wbr>Account<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}List of service account names able to access this role. If set to `["*"]` all names are allowed, both this and
bound_service_account_namespaces can not be "*".
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>bound<wbr>Service<wbr>Account<wbr>Namespaces</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}List of namespaces allowed to access this role. If set to `["*"]` all namespaces are allowed, both this and
bound_service_account_names can not be set to "*".
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Number of seconds after which issued tokens can no longer be renewed.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_max_ttl` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>num<wbr>Uses</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Number of times issued tokens can be used. Setting this to 0 or leaving it unset means unlimited uses.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_num_uses` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Number of seconds to set the TTL to for issued tokens upon renewal. Makes the token a periodic token, which will never
expire as long as it is renewed before the TTL each period.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_period` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>policies</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Policies to be set on tokens issued using this role.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_policies` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>role<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the role.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>token<wbr>Bound<wbr>Cidrs</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Specifies the blocks of IP addresses which are allowed to use the generated token
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>token<wbr>Explicit<wbr>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Generated Token's Explicit Maximum TTL in seconds
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>token<wbr>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum lifetime of the generated token
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>token<wbr>No<wbr>Default<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If true, the 'default' policy will not automatically be added to generated tokens
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>token<wbr>Num<wbr>Uses</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum number of times a token may be used, a value of zero means unlimited
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>token<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Generated Token's Period
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>token<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Generated Token's Policies
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>token<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The initial ttl of the token to generate in seconds
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>token<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The type of token to generate, service or batch
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Default number of seconds to set as the TTL for issued tokens and at renewal time.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_ttl` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>audience</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Optional Audience claim to verify in the JWT.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Unique name of the kubernetes backend to configure.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>bound_<wbr>cidrs</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of CIDRs valid as the source address for login requests. This value is also encoded into any resulting token.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_bound_cidrs` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>bound_<wbr>service_<wbr>account_<wbr>names</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of service account names able to access this role. If set to `["*"]` all names are allowed, both this and
bound_service_account_namespaces can not be "*".
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>bound_<wbr>service_<wbr>account_<wbr>namespaces</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of namespaces allowed to access this role. If set to `["*"]` all namespaces are allowed, both this and
bound_service_account_names can not be set to "*".
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>max_<wbr>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Number of seconds after which issued tokens can no longer be renewed.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_max_ttl` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>num_<wbr>uses</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Number of times issued tokens can be used. Setting this to 0 or leaving it unset means unlimited uses.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_num_uses` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Number of seconds to set the TTL to for issued tokens upon renewal. Makes the token a periodic token, which will never
expire as long as it is renewed before the TTL each period.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_period` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>policies</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Policies to be set on tokens issued using this role.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_policies` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>role_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the role.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>token_<wbr>bound_<wbr>cidrs</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Specifies the blocks of IP addresses which are allowed to use the generated token
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>token_<wbr>explicit_<wbr>max_<wbr>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Generated Token's Explicit Maximum TTL in seconds
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>token_<wbr>max_<wbr>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum lifetime of the generated token
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>token_<wbr>no_<wbr>default_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If true, the 'default' policy will not automatically be added to generated tokens
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>token_<wbr>num_<wbr>uses</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum number of times a token may be used, a value of zero means unlimited
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>token_<wbr>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Generated Token's Period
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>token_<wbr>policies</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Generated Token's Policies
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>token_<wbr>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The initial ttl of the token to generate in seconds
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>token_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The type of token to generate, service or batch
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Default number of seconds to set as the TTL for issued tokens and at renewal time.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_ttl` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

</dl>
{{% /choosable %}}








## Look up an Existing AuthBackendRole Resource

Get an existing AuthBackendRole resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/vault/kubernetes/#AuthBackendRoleState">AuthBackendRoleState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/vault/kubernetes/#AuthBackendRole">AuthBackendRole</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>audience=None<span class="p">, </span>backend=None<span class="p">, </span>bound_cidrs=None<span class="p">, </span>bound_service_account_names=None<span class="p">, </span>bound_service_account_namespaces=None<span class="p">, </span>max_ttl=None<span class="p">, </span>num_uses=None<span class="p">, </span>period=None<span class="p">, </span>policies=None<span class="p">, </span>role_name=None<span class="p">, </span>token_bound_cidrs=None<span class="p">, </span>token_explicit_max_ttl=None<span class="p">, </span>token_max_ttl=None<span class="p">, </span>token_no_default_policy=None<span class="p">, </span>token_num_uses=None<span class="p">, </span>token_period=None<span class="p">, </span>token_policies=None<span class="p">, </span>token_ttl=None<span class="p">, </span>token_type=None<span class="p">, </span>ttl=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetAuthBackendRole<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-vault/sdk/go/vault/kubernetes?tab=doc#AuthBackendRoleState">AuthBackendRoleState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-vault/sdk/go/vault/kubernetes?tab=doc#AuthBackendRole">AuthBackendRole</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Vault/Pulumi.Vault.Kubernetes.AuthBackendRole.html">AuthBackendRole</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Vault/Pulumi.Vault.Kubernetes.AuthBackendRoleState.html">AuthBackendRoleState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Audience</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Optional Audience claim to verify in the JWT.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Unique name of the kubernetes backend to configure.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Bound<wbr>Cidrs</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of CIDRs valid as the source address for login requests. This value is also encoded into any resulting token.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_bound_cidrs` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bound<wbr>Service<wbr>Account<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of service account names able to access this role. If set to `["*"]` all names are allowed, both this and
bound_service_account_namespaces can not be "*".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bound<wbr>Service<wbr>Account<wbr>Namespaces</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of namespaces allowed to access this role. If set to `["*"]` all namespaces are allowed, both this and
bound_service_account_names can not be set to "*".
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Number of seconds after which issued tokens can no longer be renewed.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_max_ttl` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Num<wbr>Uses</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Number of times issued tokens can be used. Setting this to 0 or leaving it unset means unlimited uses.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_num_uses` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Number of seconds to set the TTL to for issued tokens upon renewal. Makes the token a periodic token, which will never
expire as long as it is renewed before the TTL each period.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_period` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Policies to be set on tokens issued using this role.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_policies` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Role<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the role.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Bound<wbr>Cidrs</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Specifies the blocks of IP addresses which are allowed to use the generated token
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Explicit<wbr>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Generated Token's Explicit Maximum TTL in seconds
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The maximum lifetime of the generated token
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>No<wbr>Default<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If true, the 'default' policy will not automatically be added to generated tokens
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Num<wbr>Uses</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The maximum number of times a token may be used, a value of zero means unlimited
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Generated Token's Period
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Generated Token's Policies
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The initial ttl of the token to generate in seconds
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The type of token to generate, service or batch
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Default number of seconds to set as the TTL for issued tokens and at renewal time.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_ttl` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Audience</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Optional Audience claim to verify in the JWT.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Unique name of the kubernetes backend to configure.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Bound<wbr>Cidrs</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of CIDRs valid as the source address for login requests. This value is also encoded into any resulting token.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_bound_cidrs` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bound<wbr>Service<wbr>Account<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of service account names able to access this role. If set to `["*"]` all names are allowed, both this and
bound_service_account_namespaces can not be "*".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bound<wbr>Service<wbr>Account<wbr>Namespaces</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of namespaces allowed to access this role. If set to `["*"]` all namespaces are allowed, both this and
bound_service_account_names can not be set to "*".
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Number of seconds after which issued tokens can no longer be renewed.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_max_ttl` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Num<wbr>Uses</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Number of times issued tokens can be used. Setting this to 0 or leaving it unset means unlimited uses.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_num_uses` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Number of seconds to set the TTL to for issued tokens upon renewal. Makes the token a periodic token, which will never
expire as long as it is renewed before the TTL each period.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_period` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Policies to be set on tokens issued using this role.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_policies` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Role<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of the role.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Bound<wbr>Cidrs</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Specifies the blocks of IP addresses which are allowed to use the generated token
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Explicit<wbr>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Generated Token's Explicit Maximum TTL in seconds
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The maximum lifetime of the generated token
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>No<wbr>Default<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If true, the 'default' policy will not automatically be added to generated tokens
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Num<wbr>Uses</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The maximum number of times a token may be used, a value of zero means unlimited
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Generated Token's Period
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Generated Token's Policies
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The initial ttl of the token to generate in seconds
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The type of token to generate, service or batch
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Default number of seconds to set as the TTL for issued tokens and at renewal time.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_ttl` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>audience</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Optional Audience claim to verify in the JWT.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Unique name of the kubernetes backend to configure.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>bound<wbr>Cidrs</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of CIDRs valid as the source address for login requests. This value is also encoded into any resulting token.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_bound_cidrs` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>bound<wbr>Service<wbr>Account<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of service account names able to access this role. If set to `["*"]` all names are allowed, both this and
bound_service_account_namespaces can not be "*".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bound<wbr>Service<wbr>Account<wbr>Namespaces</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of namespaces allowed to access this role. If set to `["*"]` all namespaces are allowed, both this and
bound_service_account_names can not be set to "*".
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Number of seconds after which issued tokens can no longer be renewed.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_max_ttl` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>num<wbr>Uses</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Number of times issued tokens can be used. Setting this to 0 or leaving it unset means unlimited uses.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_num_uses` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Number of seconds to set the TTL to for issued tokens upon renewal. Makes the token a periodic token, which will never
expire as long as it is renewed before the TTL each period.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_period` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>policies</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Policies to be set on tokens issued using this role.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_policies` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>role<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the role.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token<wbr>Bound<wbr>Cidrs</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Specifies the blocks of IP addresses which are allowed to use the generated token
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token<wbr>Explicit<wbr>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Generated Token's Explicit Maximum TTL in seconds
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token<wbr>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum lifetime of the generated token
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token<wbr>No<wbr>Default<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If true, the 'default' policy will not automatically be added to generated tokens
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token<wbr>Num<wbr>Uses</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum number of times a token may be used, a value of zero means unlimited
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Generated Token's Period
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Generated Token's Policies
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The initial ttl of the token to generate in seconds
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The type of token to generate, service or batch
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Default number of seconds to set as the TTL for issued tokens and at renewal time.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_ttl` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>audience</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Optional Audience claim to verify in the JWT.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Unique name of the kubernetes backend to configure.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>bound_<wbr>cidrs</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of CIDRs valid as the source address for login requests. This value is also encoded into any resulting token.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_bound_cidrs` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>bound_<wbr>service_<wbr>account_<wbr>names</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of service account names able to access this role. If set to `["*"]` all names are allowed, both this and
bound_service_account_namespaces can not be "*".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bound_<wbr>service_<wbr>account_<wbr>namespaces</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of namespaces allowed to access this role. If set to `["*"]` all namespaces are allowed, both this and
bound_service_account_names can not be set to "*".
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>max_<wbr>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Number of seconds after which issued tokens can no longer be renewed.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_max_ttl` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>num_<wbr>uses</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Number of times issued tokens can be used. Setting this to 0 or leaving it unset means unlimited uses.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_num_uses` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Number of seconds to set the TTL to for issued tokens upon renewal. Makes the token a periodic token, which will never
expire as long as it is renewed before the TTL each period.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_period` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>policies</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Policies to be set on tokens issued using this role.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_policies` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>role_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the role.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token_<wbr>bound_<wbr>cidrs</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Specifies the blocks of IP addresses which are allowed to use the generated token
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token_<wbr>explicit_<wbr>max_<wbr>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Generated Token's Explicit Maximum TTL in seconds
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token_<wbr>max_<wbr>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum lifetime of the generated token
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token_<wbr>no_<wbr>default_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If true, the 'default' policy will not automatically be added to generated tokens
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token_<wbr>num_<wbr>uses</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum number of times a token may be used, a value of zero means unlimited
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token_<wbr>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Generated Token's Period
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token_<wbr>policies</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Generated Token's Policies
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token_<wbr>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The initial ttl of the token to generate in seconds
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The type of token to generate, service or batch
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Default number of seconds to set as the TTL for issued tokens and at renewal time.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_ttl` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

</dl>
{{% /choosable %}}











<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-vault">https://github.com/pulumi/pulumi-vault</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    
</dl>

