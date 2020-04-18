
---
title: "Token"
block_external_search_index: true
---






## Create a Token Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/vault/#Token">Token</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/vault/#TokenArgs">TokenArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Token</span><span class="p">(resource_name, opts=None, </span>display_name=None<span class="p">, </span>explicit_max_ttl=None<span class="p">, </span>no_default_policy=None<span class="p">, </span>no_parent=None<span class="p">, </span>num_uses=None<span class="p">, </span>period=None<span class="p">, </span>policies=None<span class="p">, </span>renew_increment=None<span class="p">, </span>renew_min_lease=None<span class="p">, </span>renewable=None<span class="p">, </span>role_name=None<span class="p">, </span>ttl=None<span class="p">, </span>wrapping_ttl=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewToken<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-vault/sdk/go/vault/?tab=doc#TokenArgs">TokenArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-vault/sdk/go/vault/?tab=doc#Token">Token</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Vault/Pulumi.Vault..Token.html">Token</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Vault/Pulumi.Vault.TokenArgs.html">TokenArgs</a></span>? <span class="nx">args = null<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The display name of the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Explicit<wbr>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The explicit max TTL of the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>No<wbr>Default<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to disable the default policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>No<wbr>Parent</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to create a token without parent.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Num<wbr>Uses</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The number of allowed uses of the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The period of the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of policies.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Renew<wbr>Increment</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The renew increment.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Renew<wbr>Min<wbr>Lease</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The minimum lease to renew token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Renewable</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to allow the token to be renewed
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Role<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The token role name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The TTL period of the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Wrapping<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The TTL period of the wrapped token.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The display name of the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Explicit<wbr>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The explicit max TTL of the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>No<wbr>Default<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to disable the default policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>No<wbr>Parent</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to create a token without parent.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Num<wbr>Uses</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The number of allowed uses of the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The period of the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of policies.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Renew<wbr>Increment</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The renew increment.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Renew<wbr>Min<wbr>Lease</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The minimum lease to renew token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Renewable</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to allow the token to be renewed
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Role<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The token role name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The TTL period of the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Wrapping<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The TTL period of the wrapped token.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The display name of the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>explicit<wbr>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The explicit max TTL of the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>no<wbr>Default<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to disable the default policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>no<wbr>Parent</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to create a token without parent.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>num<wbr>Uses</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The number of allowed uses of the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The period of the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>policies</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of policies.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>renew<wbr>Increment</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The renew increment.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>renew<wbr>Min<wbr>Lease</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The minimum lease to renew token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>renewable</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to allow the token to be renewed
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>role<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The token role name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The TTL period of the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>wrapping<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The TTL period of the wrapped token.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>display_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The display name of the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>explicit_<wbr>max_<wbr>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The explicit max TTL of the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>no_<wbr>default_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to disable the default policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>no_<wbr>parent</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to create a token without parent.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>num_<wbr>uses</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The number of allowed uses of the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The period of the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>policies</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of policies.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>renew_<wbr>increment</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The renew increment.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>renew_<wbr>min_<wbr>lease</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The minimum lease to renew token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>renewable</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to allow the token to be renewed
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>role_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The token role name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The TTL period of the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>wrapping_<wbr>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The TTL period of the wrapped token.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## Token Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Client<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The client token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The display name of the token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Explicit<wbr>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The explicit max TTL of the token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Lease<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The token lease duration.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Lease<wbr>Started</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The token lease started on.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>No<wbr>Default<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to disable the default policy.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>No<wbr>Parent</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to create a token without parent.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Num<wbr>Uses</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The number of allowed uses of the token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The period of the token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of policies.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Renew<wbr>Increment</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The renew increment.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Renew<wbr>Min<wbr>Lease</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The minimum lease to renew token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Renewable</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to allow the token to be renewed
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Role<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The token role name.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The TTL period of the token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Wrapped<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The client wrapped token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Wrapping<wbr>Accessor</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The client wrapping accessor.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Wrapping<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The TTL period of the wrapped token.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Client<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The client token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The display name of the token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Explicit<wbr>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The explicit max TTL of the token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Lease<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The token lease duration.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Lease<wbr>Started</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The token lease started on.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>No<wbr>Default<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to disable the default policy.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>No<wbr>Parent</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to create a token without parent.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Num<wbr>Uses</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The number of allowed uses of the token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The period of the token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of policies.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Renew<wbr>Increment</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The renew increment.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Renew<wbr>Min<wbr>Lease</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The minimum lease to renew token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Renewable</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to allow the token to be renewed
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Role<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The token role name.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The TTL period of the token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Wrapped<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The client wrapped token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Wrapping<wbr>Accessor</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The client wrapping accessor.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Wrapping<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The TTL period of the wrapped token.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>client<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The client token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The display name of the token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>explicit<wbr>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The explicit max TTL of the token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>lease<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The token lease duration.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>lease<wbr>Started</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The token lease started on.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>no<wbr>Default<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to disable the default policy.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>no<wbr>Parent</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Flag to create a token without parent.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>num<wbr>Uses</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The number of allowed uses of the token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The period of the token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>policies</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of policies.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>renew<wbr>Increment</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The renew increment.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>renew<wbr>Min<wbr>Lease</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The minimum lease to renew token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>renewable</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Flag to allow the token to be renewed
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>role<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The token role name.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The TTL period of the token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>wrapped<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The client wrapped token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>wrapping<wbr>Accessor</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The client wrapping accessor.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>wrapping<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The TTL period of the wrapped token.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>client_<wbr>token</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The client token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>display_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The display name of the token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>explicit_<wbr>max_<wbr>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The explicit max TTL of the token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>lease_<wbr>duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The token lease duration.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>lease_<wbr>started</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The token lease started on.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>no_<wbr>default_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to disable the default policy.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>no_<wbr>parent</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to create a token without parent.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>num_<wbr>uses</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The number of allowed uses of the token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The period of the token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>policies</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of policies.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>renew_<wbr>increment</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The renew increment.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>renew_<wbr>min_<wbr>lease</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The minimum lease to renew token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>renewable</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to allow the token to be renewed
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>role_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The token role name.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The TTL period of the token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>wrapped_<wbr>token</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The client wrapped token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>wrapping_<wbr>accessor</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The client wrapping accessor.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>wrapping_<wbr>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The TTL period of the wrapped token.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing Token Resource

Get an existing Token resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/vault/#TokenState">TokenState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/vault/#Token">Token</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>client_token=None<span class="p">, </span>display_name=None<span class="p">, </span>explicit_max_ttl=None<span class="p">, </span>lease_duration=None<span class="p">, </span>lease_started=None<span class="p">, </span>no_default_policy=None<span class="p">, </span>no_parent=None<span class="p">, </span>num_uses=None<span class="p">, </span>period=None<span class="p">, </span>policies=None<span class="p">, </span>renew_increment=None<span class="p">, </span>renew_min_lease=None<span class="p">, </span>renewable=None<span class="p">, </span>role_name=None<span class="p">, </span>ttl=None<span class="p">, </span>wrapped_token=None<span class="p">, </span>wrapping_accessor=None<span class="p">, </span>wrapping_ttl=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetToken<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-vault/sdk/go/vault/?tab=doc#TokenState">TokenState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-vault/sdk/go/vault/?tab=doc#Token">Token</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Vault/Pulumi.Vault..Token.html">Token</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Vault/Pulumi.Vault..TokenState.html">TokenState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Client<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The client token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The display name of the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Explicit<wbr>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The explicit max TTL of the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Lease<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The token lease duration.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Lease<wbr>Started</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The token lease started on.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>No<wbr>Default<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to disable the default policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>No<wbr>Parent</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to create a token without parent.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Num<wbr>Uses</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The number of allowed uses of the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The period of the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of policies.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Renew<wbr>Increment</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The renew increment.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Renew<wbr>Min<wbr>Lease</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The minimum lease to renew token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Renewable</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to allow the token to be renewed
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Role<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The token role name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The TTL period of the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Wrapped<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The client wrapped token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Wrapping<wbr>Accessor</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The client wrapping accessor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Wrapping<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The TTL period of the wrapped token.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The client token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The display name of the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Explicit<wbr>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The explicit max TTL of the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Lease<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The token lease duration.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Lease<wbr>Started</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The token lease started on.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>No<wbr>Default<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to disable the default policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>No<wbr>Parent</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to create a token without parent.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Num<wbr>Uses</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The number of allowed uses of the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The period of the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of policies.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Renew<wbr>Increment</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The renew increment.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Renew<wbr>Min<wbr>Lease</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The minimum lease to renew token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Renewable</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to allow the token to be renewed
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Role<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The token role name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The TTL period of the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Wrapped<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The client wrapped token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Wrapping<wbr>Accessor</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The client wrapping accessor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Wrapping<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The TTL period of the wrapped token.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>client<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The client token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The display name of the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>explicit<wbr>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The explicit max TTL of the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>lease<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The token lease duration.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>lease<wbr>Started</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The token lease started on.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>no<wbr>Default<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to disable the default policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>no<wbr>Parent</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to create a token without parent.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>num<wbr>Uses</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The number of allowed uses of the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The period of the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>policies</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of policies.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>renew<wbr>Increment</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The renew increment.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>renew<wbr>Min<wbr>Lease</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The minimum lease to renew token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>renewable</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to allow the token to be renewed
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>role<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The token role name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The TTL period of the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>wrapped<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The client wrapped token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>wrapping<wbr>Accessor</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The client wrapping accessor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>wrapping<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The TTL period of the wrapped token.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>client_<wbr>token</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The client token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>display_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The display name of the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>explicit_<wbr>max_<wbr>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The explicit max TTL of the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>lease_<wbr>duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The token lease duration.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>lease_<wbr>started</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The token lease started on.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>no_<wbr>default_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to disable the default policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>no_<wbr>parent</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to create a token without parent.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>num_<wbr>uses</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The number of allowed uses of the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The period of the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>policies</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of policies.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>renew_<wbr>increment</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The renew increment.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>renew_<wbr>min_<wbr>lease</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The minimum lease to renew token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>renewable</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to allow the token to be renewed
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>role_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The token role name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The TTL period of the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>wrapped_<wbr>token</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The client wrapped token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>wrapping_<wbr>accessor</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The client wrapping accessor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>wrapping_<wbr>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The TTL period of the wrapped token.
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

