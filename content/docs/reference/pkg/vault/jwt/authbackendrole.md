
---
title: "AuthBackendRole"
block_external_search_index: true
---






## Create a AuthBackendRole Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/vault/jwt/#AuthBackendRole">AuthBackendRole</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/vault/jwt/#AuthBackendRoleArgs">AuthBackendRoleArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">AuthBackendRole</span><span class="p">(resource_name, opts=None, </span>allowed_redirect_uris=None<span class="p">, </span>backend=None<span class="p">, </span>bound_audiences=None<span class="p">, </span>bound_cidrs=None<span class="p">, </span>bound_claims=None<span class="p">, </span>bound_subject=None<span class="p">, </span>claim_mappings=None<span class="p">, </span>clock_skew_leeway=None<span class="p">, </span>expiration_leeway=None<span class="p">, </span>groups_claim=None<span class="p">, </span>groups_claim_delimiter_pattern=None<span class="p">, </span>max_ttl=None<span class="p">, </span>not_before_leeway=None<span class="p">, </span>num_uses=None<span class="p">, </span>oidc_scopes=None<span class="p">, </span>period=None<span class="p">, </span>policies=None<span class="p">, </span>role_name=None<span class="p">, </span>role_type=None<span class="p">, </span>token_bound_cidrs=None<span class="p">, </span>token_explicit_max_ttl=None<span class="p">, </span>token_max_ttl=None<span class="p">, </span>token_no_default_policy=None<span class="p">, </span>token_num_uses=None<span class="p">, </span>token_period=None<span class="p">, </span>token_policies=None<span class="p">, </span>token_ttl=None<span class="p">, </span>token_type=None<span class="p">, </span>ttl=None<span class="p">, </span>user_claim=None<span class="p">, </span>verbose_oidc_logging=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewAuthBackendRole<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-vault/sdk/go/vault/jwt?tab=doc#AuthBackendRoleArgs">AuthBackendRoleArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-vault/sdk/go/vault/jwt?tab=doc#AuthBackendRole">AuthBackendRole</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Vault/Pulumi.Vault.Jwt.AuthBackendRole.html">AuthBackendRole</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Vault/Pulumi.Vault.Jwt.AuthBackendRoleArgs.html">AuthBackendRoleArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Allowed<wbr>Redirect<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The list of allowed values for redirect_uri during OIDC logins.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Unique name of the auth backend to configure.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bound<wbr>Audiences</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of aud claims to match against. Any match is sufficient.
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
        <span>Bound<wbr>Claims</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}Map of claims/values to match against. The expected value may be a single string or a comma-separated string list.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bound<wbr>Subject</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}If set, requires that the sub claim matches this value.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Claim<wbr>Mappings</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}Map of claims (keys) to be copied to specified metadata fields (values).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Clock<wbr>Skew<wbr>Leeway</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The amount of leeway to add to all claims to account for clock skew, in seconds. Defaults to 60 seconds if set to 0 and
can be disabled if set to -1. Only applicable with 'jwt' roles.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Expiration<wbr>Leeway</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The amount of leeway to add to expiration (exp) claims to account for clock skew, in seconds. Defaults to 60 seconds if
set to 0 and can be disabled if set to -1. Only applicable with 'jwt' roles.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Groups<wbr>Claim</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The claim to use to uniquely identify the set of groups to which the user belongs; this will be used as the names for
the Identity group aliases created due to a successful login. The claim value must be a list of strings.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Groups<wbr>Claim<wbr>Delimiter<wbr>Pattern</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A pattern of delimiters used to allow the groups_claim to live outside of the top-level JWT structure. For instance, a
groups_claim of meta/user.name/groups with this field set to // will expect nested structures named meta, user.name, and
groups. If this field was set to /./ the groups information would expect to be via nested structures of meta, user,
name, and groups.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}`groups_claim_delimiter_pattern` has been removed since Vault 1.1. If the groups claim is not at the top level, it can now be specified as a JSONPointer.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Number of seconds after which issued tokens can no longer be renewed.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_max_ttl` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Not<wbr>Before<wbr>Leeway</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The amount of leeway to add to not before (nbf) claims to account for clock skew, in seconds. Defaults to 150 seconds if
set to 0 and can be disabled if set to -1. Only applicable with 'jwt' roles.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Num<wbr>Uses</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Number of times issued tokens can be used. Setting this to 0 or leaving it unset means unlimited uses.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_num_uses` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Oidc<wbr>Scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of OIDC scopes to be used with an OIDC role. The standard scope "openid" is automatically included and need not be
specified.
{{% /md %}}</dd>

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
        <span>Role<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Type of role, either "oidc" (default) or "jwt"
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

    <dt class="property-required"
            title="Required">
        <span>User<wbr>Claim</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The claim to use to uniquely identify the user; this will be used as the name for the Identity entity alias created due
to a successful login.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Verbose<wbr>Oidc<wbr>Logging</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Log received OIDC tokens and claims when debug-level logging is active. Not recommended in production since sensitive
information may be present in OIDC responses.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Allowed<wbr>Redirect<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The list of allowed values for redirect_uri during OIDC logins.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Unique name of the auth backend to configure.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bound<wbr>Audiences</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of aud claims to match against. Any match is sufficient.
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
        <span>Bound<wbr>Claims</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}Map of claims/values to match against. The expected value may be a single string or a comma-separated string list.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bound<wbr>Subject</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}If set, requires that the sub claim matches this value.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Claim<wbr>Mappings</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}Map of claims (keys) to be copied to specified metadata fields (values).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Clock<wbr>Skew<wbr>Leeway</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The amount of leeway to add to all claims to account for clock skew, in seconds. Defaults to 60 seconds if set to 0 and
can be disabled if set to -1. Only applicable with 'jwt' roles.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Expiration<wbr>Leeway</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The amount of leeway to add to expiration (exp) claims to account for clock skew, in seconds. Defaults to 60 seconds if
set to 0 and can be disabled if set to -1. Only applicable with 'jwt' roles.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Groups<wbr>Claim</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The claim to use to uniquely identify the set of groups to which the user belongs; this will be used as the names for
the Identity group aliases created due to a successful login. The claim value must be a list of strings.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Groups<wbr>Claim<wbr>Delimiter<wbr>Pattern</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A pattern of delimiters used to allow the groups_claim to live outside of the top-level JWT structure. For instance, a
groups_claim of meta/user.name/groups with this field set to // will expect nested structures named meta, user.name, and
groups. If this field was set to /./ the groups information would expect to be via nested structures of meta, user,
name, and groups.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}`groups_claim_delimiter_pattern` has been removed since Vault 1.1. If the groups claim is not at the top level, it can now be specified as a JSONPointer.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Number of seconds after which issued tokens can no longer be renewed.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_max_ttl` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Not<wbr>Before<wbr>Leeway</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The amount of leeway to add to not before (nbf) claims to account for clock skew, in seconds. Defaults to 150 seconds if
set to 0 and can be disabled if set to -1. Only applicable with 'jwt' roles.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Num<wbr>Uses</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Number of times issued tokens can be used. Setting this to 0 or leaving it unset means unlimited uses.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_num_uses` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Oidc<wbr>Scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of OIDC scopes to be used with an OIDC role. The standard scope "openid" is automatically included and need not be
specified.
{{% /md %}}</dd>

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
        <span>Role<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Type of role, either "oidc" (default) or "jwt"
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

    <dt class="property-required"
            title="Required">
        <span>User<wbr>Claim</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The claim to use to uniquely identify the user; this will be used as the name for the Identity entity alias created due
to a successful login.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Verbose<wbr>Oidc<wbr>Logging</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Log received OIDC tokens and claims when debug-level logging is active. Not recommended in production since sensitive
information may be present in OIDC responses.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>allowed<wbr>Redirect<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The list of allowed values for redirect_uri during OIDC logins.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Unique name of the auth backend to configure.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bound<wbr>Audiences</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of aud claims to match against. Any match is sufficient.
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
        <span>bound<wbr>Claims</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}Map of claims/values to match against. The expected value may be a single string or a comma-separated string list.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bound<wbr>Subject</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}If set, requires that the sub claim matches this value.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>claim<wbr>Mappings</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}Map of claims (keys) to be copied to specified metadata fields (values).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>clock<wbr>Skew<wbr>Leeway</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The amount of leeway to add to all claims to account for clock skew, in seconds. Defaults to 60 seconds if set to 0 and
can be disabled if set to -1. Only applicable with 'jwt' roles.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>expiration<wbr>Leeway</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The amount of leeway to add to expiration (exp) claims to account for clock skew, in seconds. Defaults to 60 seconds if
set to 0 and can be disabled if set to -1. Only applicable with 'jwt' roles.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>groups<wbr>Claim</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The claim to use to uniquely identify the set of groups to which the user belongs; this will be used as the names for
the Identity group aliases created due to a successful login. The claim value must be a list of strings.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>groups<wbr>Claim<wbr>Delimiter<wbr>Pattern</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A pattern of delimiters used to allow the groups_claim to live outside of the top-level JWT structure. For instance, a
groups_claim of meta/user.name/groups with this field set to // will expect nested structures named meta, user.name, and
groups. If this field was set to /./ the groups information would expect to be via nested structures of meta, user,
name, and groups.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}`groups_claim_delimiter_pattern` has been removed since Vault 1.1. If the groups claim is not at the top level, it can now be specified as a JSONPointer.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Number of seconds after which issued tokens can no longer be renewed.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_max_ttl` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>not<wbr>Before<wbr>Leeway</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The amount of leeway to add to not before (nbf) claims to account for clock skew, in seconds. Defaults to 150 seconds if
set to 0 and can be disabled if set to -1. Only applicable with 'jwt' roles.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>num<wbr>Uses</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Number of times issued tokens can be used. Setting this to 0 or leaving it unset means unlimited uses.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_num_uses` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>oidc<wbr>Scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of OIDC scopes to be used with an OIDC role. The standard scope "openid" is automatically included and need not be
specified.
{{% /md %}}</dd>

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
        <span>role<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Type of role, either "oidc" (default) or "jwt"
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

    <dt class="property-required"
            title="Required">
        <span>user<wbr>Claim</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The claim to use to uniquely identify the user; this will be used as the name for the Identity entity alias created due
to a successful login.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>verbose<wbr>Oidc<wbr>Logging</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Log received OIDC tokens and claims when debug-level logging is active. Not recommended in production since sensitive
information may be present in OIDC responses.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>allowed_<wbr>redirect_<wbr>uris</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The list of allowed values for redirect_uri during OIDC logins.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Unique name of the auth backend to configure.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bound_<wbr>audiences</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of aud claims to match against. Any match is sufficient.
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
        <span>bound_<wbr>claims</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Map of claims/values to match against. The expected value may be a single string or a comma-separated string list.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bound_<wbr>subject</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}If set, requires that the sub claim matches this value.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>claim_<wbr>mappings</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Map of claims (keys) to be copied to specified metadata fields (values).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>clock_<wbr>skew_<wbr>leeway</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of leeway to add to all claims to account for clock skew, in seconds. Defaults to 60 seconds if set to 0 and
can be disabled if set to -1. Only applicable with 'jwt' roles.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>expiration_<wbr>leeway</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of leeway to add to expiration (exp) claims to account for clock skew, in seconds. Defaults to 60 seconds if
set to 0 and can be disabled if set to -1. Only applicable with 'jwt' roles.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>groups_<wbr>claim</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The claim to use to uniquely identify the set of groups to which the user belongs; this will be used as the names for
the Identity group aliases created due to a successful login. The claim value must be a list of strings.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>groups_<wbr>claim_<wbr>delimiter_<wbr>pattern</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A pattern of delimiters used to allow the groups_claim to live outside of the top-level JWT structure. For instance, a
groups_claim of meta/user.name/groups with this field set to // will expect nested structures named meta, user.name, and
groups. If this field was set to /./ the groups information would expect to be via nested structures of meta, user,
name, and groups.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}`groups_claim_delimiter_pattern` has been removed since Vault 1.1. If the groups claim is not at the top level, it can now be specified as a JSONPointer.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>max_<wbr>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Number of seconds after which issued tokens can no longer be renewed.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_max_ttl` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>not_<wbr>before_<wbr>leeway</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of leeway to add to not before (nbf) claims to account for clock skew, in seconds. Defaults to 150 seconds if
set to 0 and can be disabled if set to -1. Only applicable with 'jwt' roles.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>num_<wbr>uses</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Number of times issued tokens can be used. Setting this to 0 or leaving it unset means unlimited uses.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_num_uses` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>oidc_<wbr>scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of OIDC scopes to be used with an OIDC role. The standard scope "openid" is automatically included and need not be
specified.
{{% /md %}}</dd>

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
        <span>role_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Type of role, either "oidc" (default) or "jwt"
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

    <dt class="property-required"
            title="Required">
        <span>user_<wbr>claim</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The claim to use to uniquely identify the user; this will be used as the name for the Identity entity alias created due
to a successful login.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>verbose_<wbr>oidc_<wbr>logging</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Log received OIDC tokens and claims when debug-level logging is active. Not recommended in production since sensitive
information may be present in OIDC responses.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## AuthBackendRole Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Allowed<wbr>Redirect<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The list of allowed values for redirect_uri during OIDC logins.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Unique name of the auth backend to configure.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Bound<wbr>Audiences</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of aud claims to match against. Any match is sufficient.
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
        <span>Bound<wbr>Claims</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}Map of claims/values to match against. The expected value may be a single string or a comma-separated string list.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Bound<wbr>Subject</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}If set, requires that the sub claim matches this value.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Claim<wbr>Mappings</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}Map of claims (keys) to be copied to specified metadata fields (values).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Clock<wbr>Skew<wbr>Leeway</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The amount of leeway to add to all claims to account for clock skew, in seconds. Defaults to 60 seconds if set to 0 and
can be disabled if set to -1. Only applicable with 'jwt' roles.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Expiration<wbr>Leeway</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The amount of leeway to add to expiration (exp) claims to account for clock skew, in seconds. Defaults to 60 seconds if
set to 0 and can be disabled if set to -1. Only applicable with 'jwt' roles.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Groups<wbr>Claim</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The claim to use to uniquely identify the set of groups to which the user belongs; this will be used as the names for
the Identity group aliases created due to a successful login. The claim value must be a list of strings.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Groups<wbr>Claim<wbr>Delimiter<wbr>Pattern</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A pattern of delimiters used to allow the groups_claim to live outside of the top-level JWT structure. For instance, a
groups_claim of meta/user.name/groups with this field set to // will expect nested structures named meta, user.name, and
groups. If this field was set to /./ the groups information would expect to be via nested structures of meta, user,
name, and groups.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}`groups_claim_delimiter_pattern` has been removed since Vault 1.1. If the groups claim is not at the top level, it can now be specified as a JSONPointer.{{% /md %}}</p></dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Number of seconds after which issued tokens can no longer be renewed.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_max_ttl` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>Not<wbr>Before<wbr>Leeway</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The amount of leeway to add to not before (nbf) claims to account for clock skew, in seconds. Defaults to 150 seconds if
set to 0 and can be disabled if set to -1. Only applicable with 'jwt' roles.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Num<wbr>Uses</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Number of times issued tokens can be used. Setting this to 0 or leaving it unset means unlimited uses.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_num_uses` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>Oidc<wbr>Scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of OIDC scopes to be used with an OIDC role. The standard scope "openid" is automatically included and need not be
specified.
{{% /md %}}</dd>

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
        <span>Role<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Type of role, either "oidc" (default) or "jwt"
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

    <dt class="property-"
            title="">
        <span>User<wbr>Claim</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The claim to use to uniquely identify the user; this will be used as the name for the Identity entity alias created due
to a successful login.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Verbose<wbr>Oidc<wbr>Logging</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Log received OIDC tokens and claims when debug-level logging is active. Not recommended in production since sensitive
information may be present in OIDC responses.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Allowed<wbr>Redirect<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The list of allowed values for redirect_uri during OIDC logins.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Unique name of the auth backend to configure.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Bound<wbr>Audiences</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of aud claims to match against. Any match is sufficient.
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
        <span>Bound<wbr>Claims</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}Map of claims/values to match against. The expected value may be a single string or a comma-separated string list.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Bound<wbr>Subject</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}If set, requires that the sub claim matches this value.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Claim<wbr>Mappings</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}Map of claims (keys) to be copied to specified metadata fields (values).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Clock<wbr>Skew<wbr>Leeway</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The amount of leeway to add to all claims to account for clock skew, in seconds. Defaults to 60 seconds if set to 0 and
can be disabled if set to -1. Only applicable with 'jwt' roles.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Expiration<wbr>Leeway</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The amount of leeway to add to expiration (exp) claims to account for clock skew, in seconds. Defaults to 60 seconds if
set to 0 and can be disabled if set to -1. Only applicable with 'jwt' roles.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Groups<wbr>Claim</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The claim to use to uniquely identify the set of groups to which the user belongs; this will be used as the names for
the Identity group aliases created due to a successful login. The claim value must be a list of strings.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Groups<wbr>Claim<wbr>Delimiter<wbr>Pattern</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A pattern of delimiters used to allow the groups_claim to live outside of the top-level JWT structure. For instance, a
groups_claim of meta/user.name/groups with this field set to // will expect nested structures named meta, user.name, and
groups. If this field was set to /./ the groups information would expect to be via nested structures of meta, user,
name, and groups.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}`groups_claim_delimiter_pattern` has been removed since Vault 1.1. If the groups claim is not at the top level, it can now be specified as a JSONPointer.{{% /md %}}</p></dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Number of seconds after which issued tokens can no longer be renewed.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_max_ttl` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>Not<wbr>Before<wbr>Leeway</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The amount of leeway to add to not before (nbf) claims to account for clock skew, in seconds. Defaults to 150 seconds if
set to 0 and can be disabled if set to -1. Only applicable with 'jwt' roles.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Num<wbr>Uses</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Number of times issued tokens can be used. Setting this to 0 or leaving it unset means unlimited uses.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_num_uses` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>Oidc<wbr>Scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of OIDC scopes to be used with an OIDC role. The standard scope "openid" is automatically included and need not be
specified.
{{% /md %}}</dd>

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
        <span>Role<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Type of role, either "oidc" (default) or "jwt"
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

    <dt class="property-"
            title="">
        <span>User<wbr>Claim</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The claim to use to uniquely identify the user; this will be used as the name for the Identity entity alias created due
to a successful login.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Verbose<wbr>Oidc<wbr>Logging</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Log received OIDC tokens and claims when debug-level logging is active. Not recommended in production since sensitive
information may be present in OIDC responses.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>allowed<wbr>Redirect<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The list of allowed values for redirect_uri during OIDC logins.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Unique name of the auth backend to configure.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>bound<wbr>Audiences</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of aud claims to match against. Any match is sufficient.
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
        <span>bound<wbr>Claims</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}Map of claims/values to match against. The expected value may be a single string or a comma-separated string list.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>bound<wbr>Subject</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}If set, requires that the sub claim matches this value.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>claim<wbr>Mappings</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}Map of claims (keys) to be copied to specified metadata fields (values).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>clock<wbr>Skew<wbr>Leeway</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The amount of leeway to add to all claims to account for clock skew, in seconds. Defaults to 60 seconds if set to 0 and
can be disabled if set to -1. Only applicable with 'jwt' roles.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>expiration<wbr>Leeway</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The amount of leeway to add to expiration (exp) claims to account for clock skew, in seconds. Defaults to 60 seconds if
set to 0 and can be disabled if set to -1. Only applicable with 'jwt' roles.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>groups<wbr>Claim</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The claim to use to uniquely identify the set of groups to which the user belongs; this will be used as the names for
the Identity group aliases created due to a successful login. The claim value must be a list of strings.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>groups<wbr>Claim<wbr>Delimiter<wbr>Pattern</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A pattern of delimiters used to allow the groups_claim to live outside of the top-level JWT structure. For instance, a
groups_claim of meta/user.name/groups with this field set to // will expect nested structures named meta, user.name, and
groups. If this field was set to /./ the groups information would expect to be via nested structures of meta, user,
name, and groups.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}`groups_claim_delimiter_pattern` has been removed since Vault 1.1. If the groups claim is not at the top level, it can now be specified as a JSONPointer.{{% /md %}}</p></dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Number of seconds after which issued tokens can no longer be renewed.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_max_ttl` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>not<wbr>Before<wbr>Leeway</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The amount of leeway to add to not before (nbf) claims to account for clock skew, in seconds. Defaults to 150 seconds if
set to 0 and can be disabled if set to -1. Only applicable with 'jwt' roles.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>num<wbr>Uses</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Number of times issued tokens can be used. Setting this to 0 or leaving it unset means unlimited uses.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_num_uses` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>oidc<wbr>Scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of OIDC scopes to be used with an OIDC role. The standard scope "openid" is automatically included and need not be
specified.
{{% /md %}}</dd>

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
        <span>role<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Type of role, either "oidc" (default) or "jwt"
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

    <dt class="property-"
            title="">
        <span>user<wbr>Claim</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The claim to use to uniquely identify the user; this will be used as the name for the Identity entity alias created due
to a successful login.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>verbose<wbr>Oidc<wbr>Logging</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Log received OIDC tokens and claims when debug-level logging is active. Not recommended in production since sensitive
information may be present in OIDC responses.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>allowed_<wbr>redirect_<wbr>uris</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The list of allowed values for redirect_uri during OIDC logins.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Unique name of the auth backend to configure.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>bound_<wbr>audiences</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of aud claims to match against. Any match is sufficient.
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
        <span>bound_<wbr>claims</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Map of claims/values to match against. The expected value may be a single string or a comma-separated string list.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>bound_<wbr>subject</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}If set, requires that the sub claim matches this value.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>claim_<wbr>mappings</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Map of claims (keys) to be copied to specified metadata fields (values).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>clock_<wbr>skew_<wbr>leeway</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of leeway to add to all claims to account for clock skew, in seconds. Defaults to 60 seconds if set to 0 and
can be disabled if set to -1. Only applicable with 'jwt' roles.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>expiration_<wbr>leeway</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of leeway to add to expiration (exp) claims to account for clock skew, in seconds. Defaults to 60 seconds if
set to 0 and can be disabled if set to -1. Only applicable with 'jwt' roles.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>groups_<wbr>claim</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The claim to use to uniquely identify the set of groups to which the user belongs; this will be used as the names for
the Identity group aliases created due to a successful login. The claim value must be a list of strings.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>groups_<wbr>claim_<wbr>delimiter_<wbr>pattern</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A pattern of delimiters used to allow the groups_claim to live outside of the top-level JWT structure. For instance, a
groups_claim of meta/user.name/groups with this field set to // will expect nested structures named meta, user.name, and
groups. If this field was set to /./ the groups information would expect to be via nested structures of meta, user,
name, and groups.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}`groups_claim_delimiter_pattern` has been removed since Vault 1.1. If the groups claim is not at the top level, it can now be specified as a JSONPointer.{{% /md %}}</p></dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>max_<wbr>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Number of seconds after which issued tokens can no longer be renewed.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_max_ttl` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>not_<wbr>before_<wbr>leeway</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of leeway to add to not before (nbf) claims to account for clock skew, in seconds. Defaults to 150 seconds if
set to 0 and can be disabled if set to -1. Only applicable with 'jwt' roles.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>num_<wbr>uses</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Number of times issued tokens can be used. Setting this to 0 or leaving it unset means unlimited uses.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_num_uses` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>oidc_<wbr>scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of OIDC scopes to be used with an OIDC role. The standard scope "openid" is automatically included and need not be
specified.
{{% /md %}}</dd>

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
        <span>role_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Type of role, either "oidc" (default) or "jwt"
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

    <dt class="property-"
            title="">
        <span>user_<wbr>claim</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The claim to use to uniquely identify the user; this will be used as the name for the Identity entity alias created due
to a successful login.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>verbose_<wbr>oidc_<wbr>logging</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Log received OIDC tokens and claims when debug-level logging is active. Not recommended in production since sensitive
information may be present in OIDC responses.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing AuthBackendRole Resource

Get an existing AuthBackendRole resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/vault/jwt/#AuthBackendRoleState">AuthBackendRoleState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/vault/jwt/#AuthBackendRole">AuthBackendRole</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>allowed_redirect_uris=None<span class="p">, </span>backend=None<span class="p">, </span>bound_audiences=None<span class="p">, </span>bound_cidrs=None<span class="p">, </span>bound_claims=None<span class="p">, </span>bound_subject=None<span class="p">, </span>claim_mappings=None<span class="p">, </span>clock_skew_leeway=None<span class="p">, </span>expiration_leeway=None<span class="p">, </span>groups_claim=None<span class="p">, </span>groups_claim_delimiter_pattern=None<span class="p">, </span>max_ttl=None<span class="p">, </span>not_before_leeway=None<span class="p">, </span>num_uses=None<span class="p">, </span>oidc_scopes=None<span class="p">, </span>period=None<span class="p">, </span>policies=None<span class="p">, </span>role_name=None<span class="p">, </span>role_type=None<span class="p">, </span>token_bound_cidrs=None<span class="p">, </span>token_explicit_max_ttl=None<span class="p">, </span>token_max_ttl=None<span class="p">, </span>token_no_default_policy=None<span class="p">, </span>token_num_uses=None<span class="p">, </span>token_period=None<span class="p">, </span>token_policies=None<span class="p">, </span>token_ttl=None<span class="p">, </span>token_type=None<span class="p">, </span>ttl=None<span class="p">, </span>user_claim=None<span class="p">, </span>verbose_oidc_logging=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetAuthBackendRole<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-vault/sdk/go/vault/jwt?tab=doc#AuthBackendRoleState">AuthBackendRoleState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-vault/sdk/go/vault/jwt?tab=doc#AuthBackendRole">AuthBackendRole</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Vault/Pulumi.Vault.Jwt.AuthBackendRole.html">AuthBackendRole</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Vault/Pulumi.Vault.Jwt.AuthBackendRoleState.html">AuthBackendRoleState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Allowed<wbr>Redirect<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The list of allowed values for redirect_uri during OIDC logins.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Unique name of the auth backend to configure.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bound<wbr>Audiences</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of aud claims to match against. Any match is sufficient.
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
        <span>Bound<wbr>Claims</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}Map of claims/values to match against. The expected value may be a single string or a comma-separated string list.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bound<wbr>Subject</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}If set, requires that the sub claim matches this value.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Claim<wbr>Mappings</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}Map of claims (keys) to be copied to specified metadata fields (values).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Clock<wbr>Skew<wbr>Leeway</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The amount of leeway to add to all claims to account for clock skew, in seconds. Defaults to 60 seconds if set to 0 and
can be disabled if set to -1. Only applicable with 'jwt' roles.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Expiration<wbr>Leeway</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The amount of leeway to add to expiration (exp) claims to account for clock skew, in seconds. Defaults to 60 seconds if
set to 0 and can be disabled if set to -1. Only applicable with 'jwt' roles.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Groups<wbr>Claim</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The claim to use to uniquely identify the set of groups to which the user belongs; this will be used as the names for
the Identity group aliases created due to a successful login. The claim value must be a list of strings.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Groups<wbr>Claim<wbr>Delimiter<wbr>Pattern</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A pattern of delimiters used to allow the groups_claim to live outside of the top-level JWT structure. For instance, a
groups_claim of meta/user.name/groups with this field set to // will expect nested structures named meta, user.name, and
groups. If this field was set to /./ the groups information would expect to be via nested structures of meta, user,
name, and groups.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}`groups_claim_delimiter_pattern` has been removed since Vault 1.1. If the groups claim is not at the top level, it can now be specified as a JSONPointer.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Number of seconds after which issued tokens can no longer be renewed.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_max_ttl` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Not<wbr>Before<wbr>Leeway</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The amount of leeway to add to not before (nbf) claims to account for clock skew, in seconds. Defaults to 150 seconds if
set to 0 and can be disabled if set to -1. Only applicable with 'jwt' roles.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Num<wbr>Uses</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Number of times issued tokens can be used. Setting this to 0 or leaving it unset means unlimited uses.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_num_uses` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Oidc<wbr>Scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of OIDC scopes to be used with an OIDC role. The standard scope "openid" is automatically included and need not be
specified.
{{% /md %}}</dd>

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
        <span>Role<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Type of role, either "oidc" (default) or "jwt"
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

    <dt class="property-optional"
            title="Optional">
        <span>User<wbr>Claim</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The claim to use to uniquely identify the user; this will be used as the name for the Identity entity alias created due
to a successful login.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Verbose<wbr>Oidc<wbr>Logging</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Log received OIDC tokens and claims when debug-level logging is active. Not recommended in production since sensitive
information may be present in OIDC responses.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Allowed<wbr>Redirect<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The list of allowed values for redirect_uri during OIDC logins.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Unique name of the auth backend to configure.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bound<wbr>Audiences</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of aud claims to match against. Any match is sufficient.
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
        <span>Bound<wbr>Claims</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}Map of claims/values to match against. The expected value may be a single string or a comma-separated string list.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bound<wbr>Subject</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}If set, requires that the sub claim matches this value.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Claim<wbr>Mappings</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}Map of claims (keys) to be copied to specified metadata fields (values).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Clock<wbr>Skew<wbr>Leeway</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The amount of leeway to add to all claims to account for clock skew, in seconds. Defaults to 60 seconds if set to 0 and
can be disabled if set to -1. Only applicable with 'jwt' roles.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Expiration<wbr>Leeway</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The amount of leeway to add to expiration (exp) claims to account for clock skew, in seconds. Defaults to 60 seconds if
set to 0 and can be disabled if set to -1. Only applicable with 'jwt' roles.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Groups<wbr>Claim</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The claim to use to uniquely identify the set of groups to which the user belongs; this will be used as the names for
the Identity group aliases created due to a successful login. The claim value must be a list of strings.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Groups<wbr>Claim<wbr>Delimiter<wbr>Pattern</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A pattern of delimiters used to allow the groups_claim to live outside of the top-level JWT structure. For instance, a
groups_claim of meta/user.name/groups with this field set to // will expect nested structures named meta, user.name, and
groups. If this field was set to /./ the groups information would expect to be via nested structures of meta, user,
name, and groups.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}`groups_claim_delimiter_pattern` has been removed since Vault 1.1. If the groups claim is not at the top level, it can now be specified as a JSONPointer.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Number of seconds after which issued tokens can no longer be renewed.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_max_ttl` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Not<wbr>Before<wbr>Leeway</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The amount of leeway to add to not before (nbf) claims to account for clock skew, in seconds. Defaults to 150 seconds if
set to 0 and can be disabled if set to -1. Only applicable with 'jwt' roles.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Num<wbr>Uses</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Number of times issued tokens can be used. Setting this to 0 or leaving it unset means unlimited uses.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_num_uses` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Oidc<wbr>Scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of OIDC scopes to be used with an OIDC role. The standard scope "openid" is automatically included and need not be
specified.
{{% /md %}}</dd>

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
        <span>Role<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Type of role, either "oidc" (default) or "jwt"
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

    <dt class="property-optional"
            title="Optional">
        <span>User<wbr>Claim</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The claim to use to uniquely identify the user; this will be used as the name for the Identity entity alias created due
to a successful login.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Verbose<wbr>Oidc<wbr>Logging</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Log received OIDC tokens and claims when debug-level logging is active. Not recommended in production since sensitive
information may be present in OIDC responses.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>allowed<wbr>Redirect<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The list of allowed values for redirect_uri during OIDC logins.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Unique name of the auth backend to configure.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bound<wbr>Audiences</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of aud claims to match against. Any match is sufficient.
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
        <span>bound<wbr>Claims</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}Map of claims/values to match against. The expected value may be a single string or a comma-separated string list.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bound<wbr>Subject</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}If set, requires that the sub claim matches this value.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>claim<wbr>Mappings</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}Map of claims (keys) to be copied to specified metadata fields (values).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>clock<wbr>Skew<wbr>Leeway</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The amount of leeway to add to all claims to account for clock skew, in seconds. Defaults to 60 seconds if set to 0 and
can be disabled if set to -1. Only applicable with 'jwt' roles.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>expiration<wbr>Leeway</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The amount of leeway to add to expiration (exp) claims to account for clock skew, in seconds. Defaults to 60 seconds if
set to 0 and can be disabled if set to -1. Only applicable with 'jwt' roles.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>groups<wbr>Claim</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The claim to use to uniquely identify the set of groups to which the user belongs; this will be used as the names for
the Identity group aliases created due to a successful login. The claim value must be a list of strings.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>groups<wbr>Claim<wbr>Delimiter<wbr>Pattern</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A pattern of delimiters used to allow the groups_claim to live outside of the top-level JWT structure. For instance, a
groups_claim of meta/user.name/groups with this field set to // will expect nested structures named meta, user.name, and
groups. If this field was set to /./ the groups information would expect to be via nested structures of meta, user,
name, and groups.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}`groups_claim_delimiter_pattern` has been removed since Vault 1.1. If the groups claim is not at the top level, it can now be specified as a JSONPointer.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Number of seconds after which issued tokens can no longer be renewed.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_max_ttl` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>not<wbr>Before<wbr>Leeway</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The amount of leeway to add to not before (nbf) claims to account for clock skew, in seconds. Defaults to 150 seconds if
set to 0 and can be disabled if set to -1. Only applicable with 'jwt' roles.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>num<wbr>Uses</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Number of times issued tokens can be used. Setting this to 0 or leaving it unset means unlimited uses.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_num_uses` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>oidc<wbr>Scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of OIDC scopes to be used with an OIDC role. The standard scope "openid" is automatically included and need not be
specified.
{{% /md %}}</dd>

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
        <span>role<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Type of role, either "oidc" (default) or "jwt"
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

    <dt class="property-optional"
            title="Optional">
        <span>user<wbr>Claim</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The claim to use to uniquely identify the user; this will be used as the name for the Identity entity alias created due
to a successful login.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>verbose<wbr>Oidc<wbr>Logging</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Log received OIDC tokens and claims when debug-level logging is active. Not recommended in production since sensitive
information may be present in OIDC responses.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>allowed_<wbr>redirect_<wbr>uris</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The list of allowed values for redirect_uri during OIDC logins.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Unique name of the auth backend to configure.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bound_<wbr>audiences</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of aud claims to match against. Any match is sufficient.
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
        <span>bound_<wbr>claims</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Map of claims/values to match against. The expected value may be a single string or a comma-separated string list.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bound_<wbr>subject</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}If set, requires that the sub claim matches this value.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>claim_<wbr>mappings</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Map of claims (keys) to be copied to specified metadata fields (values).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>clock_<wbr>skew_<wbr>leeway</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of leeway to add to all claims to account for clock skew, in seconds. Defaults to 60 seconds if set to 0 and
can be disabled if set to -1. Only applicable with 'jwt' roles.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>expiration_<wbr>leeway</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of leeway to add to expiration (exp) claims to account for clock skew, in seconds. Defaults to 60 seconds if
set to 0 and can be disabled if set to -1. Only applicable with 'jwt' roles.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>groups_<wbr>claim</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The claim to use to uniquely identify the set of groups to which the user belongs; this will be used as the names for
the Identity group aliases created due to a successful login. The claim value must be a list of strings.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>groups_<wbr>claim_<wbr>delimiter_<wbr>pattern</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A pattern of delimiters used to allow the groups_claim to live outside of the top-level JWT structure. For instance, a
groups_claim of meta/user.name/groups with this field set to // will expect nested structures named meta, user.name, and
groups. If this field was set to /./ the groups information would expect to be via nested structures of meta, user,
name, and groups.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}`groups_claim_delimiter_pattern` has been removed since Vault 1.1. If the groups claim is not at the top level, it can now be specified as a JSONPointer.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>max_<wbr>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Number of seconds after which issued tokens can no longer be renewed.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_max_ttl` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>not_<wbr>before_<wbr>leeway</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of leeway to add to not before (nbf) claims to account for clock skew, in seconds. Defaults to 150 seconds if
set to 0 and can be disabled if set to -1. Only applicable with 'jwt' roles.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>num_<wbr>uses</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Number of times issued tokens can be used. Setting this to 0 or leaving it unset means unlimited uses.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_num_uses` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>oidc_<wbr>scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of OIDC scopes to be used with an OIDC role. The standard scope "openid" is automatically included and need not be
specified.
{{% /md %}}</dd>

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
        <span>role_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Type of role, either "oidc" (default) or "jwt"
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

    <dt class="property-optional"
            title="Optional">
        <span>user_<wbr>claim</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The claim to use to uniquely identify the user; this will be used as the name for the Identity entity alias created due
to a successful login.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>verbose_<wbr>oidc_<wbr>logging</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Log received OIDC tokens and claims when debug-level logging is active. Not recommended in production since sensitive
information may be present in OIDC responses.
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

