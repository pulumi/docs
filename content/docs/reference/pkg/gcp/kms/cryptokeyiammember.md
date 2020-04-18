
---
title: "CryptoKeyIAMMember"
block_external_search_index: true
---



Three different resources help you manage your IAM policy for KMS crypto key. Each of these resources serves a different use case:

* `gcp.kms.CryptoKeyIAMPolicy`: Authoritative. Sets the IAM policy for the crypto key and replaces any existing policy already attached.
* `gcp.kms.CryptoKeyIAMBinding`: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the crypto key are preserved.
* `gcp.kms.CryptoKeyIAMMember`: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the crypto key are preserved.

> **Note:** `gcp.kms.CryptoKeyIAMPolicy` **cannot** be used in conjunction with `gcp.kms.CryptoKeyIAMBinding` and `gcp.kms.CryptoKeyIAMMember` or they will fight over what your policy should be.

> **Note:** `gcp.kms.CryptoKeyIAMBinding` resources **can be** used in conjunction with `gcp.kms.CryptoKeyIAMMember` resources **only if** they do not grant privilege to the same role.

With IAM Conditions:

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as gcp from "@pulumi/gcp";

const admin = gcp.organizations.getIAMPolicy({
    bindings: [{
        condition: {
            description: "Expiring at midnight of 2019-12-31",
            expression: "request.time < timestamp(\"2020-01-01T00:00:00Z\")",
            title: "expires_after_2019_12_31",
        },
        members: ["user:jane@example.com"],
        role: "roles/cloudkms.cryptoKeyEncrypter",
    }],
});
```

With IAM Conditions:


With IAM Conditions:



## Create a CryptoKeyIAMMember Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/kms/#CryptoKeyIAMMember">CryptoKeyIAMMember</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/kms/#CryptoKeyIAMMemberArgs">CryptoKeyIAMMemberArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">CryptoKeyIAMMember</span><span class="p">(resource_name, opts=None, </span>condition=None<span class="p">, </span>crypto_key_id=None<span class="p">, </span>member=None<span class="p">, </span>role=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewCryptoKeyIAMMember<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/kms?tab=doc#CryptoKeyIAMMemberArgs">CryptoKeyIAMMemberArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/kms?tab=doc#CryptoKeyIAMMember">CryptoKeyIAMMember</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Kms.CryptoKeyIAMMember.html">CryptoKeyIAMMember</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Kms.CryptoKeyIAMMemberArgs.html">CryptoKeyIAMMemberArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Crypto<wbr>Key<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The crypto key ID, in the form
`{project_id}/{location_name}/{key_ring_name}/{crypto_key_name}` or
`{location_name}/{key_ring_name}/{crypto_key_name}`. In the second form,
the provider's project setting will be used as a fallback.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Member</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Role</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The role that should be applied. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Condition</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cryptokeyiammembercondition">Crypto<wbr>Key<wbr>IAMMember<wbr>Condition<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}An [IAM Condition](https://cloud.google.com/iam/docs/conditions-overview) for a given binding.
Structure is documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Crypto<wbr>Key<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The crypto key ID, in the form
`{project_id}/{location_name}/{key_ring_name}/{crypto_key_name}` or
`{location_name}/{key_ring_name}/{crypto_key_name}`. In the second form,
the provider's project setting will be used as a fallback.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Member</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Role</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The role that should be applied. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Condition</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cryptokeyiammembercondition">Crypto<wbr>Key<wbr>IAMMember<wbr>Condition</a></span>
    </dt>
    <dd>{{% md %}}An [IAM Condition](https://cloud.google.com/iam/docs/conditions-overview) for a given binding.
Structure is documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>crypto<wbr>Key<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The crypto key ID, in the form
`{project_id}/{location_name}/{key_ring_name}/{crypto_key_name}` or
`{location_name}/{key_ring_name}/{crypto_key_name}`. In the second form,
the provider's project setting will be used as a fallback.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>member</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>role</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The role that should be applied. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>condition</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cryptokeyiammembercondition">Crypto<wbr>Key<wbr>IAMMember<wbr>Condition</a></span>
    </dt>
    <dd>{{% md %}}An [IAM Condition](https://cloud.google.com/iam/docs/conditions-overview) for a given binding.
Structure is documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>crypto_<wbr>key_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The crypto key ID, in the form
`{project_id}/{location_name}/{key_ring_name}/{crypto_key_name}` or
`{location_name}/{key_ring_name}/{crypto_key_name}`. In the second form,
the provider's project setting will be used as a fallback.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>member</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>role</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The role that should be applied. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>condition</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cryptokeyiammembercondition">Dict[Crypto<wbr>Key<wbr>IAMMember<wbr>Condition]</a></span>
    </dt>
    <dd>{{% md %}}An [IAM Condition](https://cloud.google.com/iam/docs/conditions-overview) for a given binding.
Structure is documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## CryptoKeyIAMMember Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Etag</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}(Computed) The etag of the project's IAM policy.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Etag</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}(Computed) The etag of the project's IAM policy.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>etag</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}(Computed) The etag of the project's IAM policy.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>etag</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}(Computed) The etag of the project's IAM policy.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing CryptoKeyIAMMember Resource

Get an existing CryptoKeyIAMMember resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/kms/#CryptoKeyIAMMemberState">CryptoKeyIAMMemberState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/kms/#CryptoKeyIAMMember">CryptoKeyIAMMember</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>condition=None<span class="p">, </span>crypto_key_id=None<span class="p">, </span>etag=None<span class="p">, </span>member=None<span class="p">, </span>role=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetCryptoKeyIAMMember<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/kms?tab=doc#CryptoKeyIAMMemberState">CryptoKeyIAMMemberState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/kms?tab=doc#CryptoKeyIAMMember">CryptoKeyIAMMember</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Kms.CryptoKeyIAMMember.html">CryptoKeyIAMMember</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Kms.CryptoKeyIAMMemberState.html">CryptoKeyIAMMemberState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Condition</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cryptokeyiammembercondition">Crypto<wbr>Key<wbr>IAMMember<wbr>Condition<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}An [IAM Condition](https://cloud.google.com/iam/docs/conditions-overview) for a given binding.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Crypto<wbr>Key<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The crypto key ID, in the form
`{project_id}/{location_name}/{key_ring_name}/{crypto_key_name}` or
`{location_name}/{key_ring_name}/{crypto_key_name}`. In the second form,
the provider's project setting will be used as a fallback.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Etag</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}(Computed) The etag of the project's IAM policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Member</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Role</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The role that should be applied. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Condition</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cryptokeyiammembercondition">Crypto<wbr>Key<wbr>IAMMember<wbr>Condition</a></span>
    </dt>
    <dd>{{% md %}}An [IAM Condition](https://cloud.google.com/iam/docs/conditions-overview) for a given binding.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Crypto<wbr>Key<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The crypto key ID, in the form
`{project_id}/{location_name}/{key_ring_name}/{crypto_key_name}` or
`{location_name}/{key_ring_name}/{crypto_key_name}`. In the second form,
the provider's project setting will be used as a fallback.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Etag</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}(Computed) The etag of the project's IAM policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Member</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Role</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The role that should be applied. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>condition</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cryptokeyiammembercondition">Crypto<wbr>Key<wbr>IAMMember<wbr>Condition</a></span>
    </dt>
    <dd>{{% md %}}An [IAM Condition](https://cloud.google.com/iam/docs/conditions-overview) for a given binding.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>crypto<wbr>Key<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The crypto key ID, in the form
`{project_id}/{location_name}/{key_ring_name}/{crypto_key_name}` or
`{location_name}/{key_ring_name}/{crypto_key_name}`. In the second form,
the provider's project setting will be used as a fallback.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>etag</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}(Computed) The etag of the project's IAM policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>member</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>role</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The role that should be applied. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>condition</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cryptokeyiammembercondition">Dict[Crypto<wbr>Key<wbr>IAMMember<wbr>Condition]</a></span>
    </dt>
    <dd>{{% md %}}An [IAM Condition](https://cloud.google.com/iam/docs/conditions-overview) for a given binding.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>crypto_<wbr>key_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The crypto key ID, in the form
`{project_id}/{location_name}/{key_ring_name}/{crypto_key_name}` or
`{location_name}/{key_ring_name}/{crypto_key_name}`. In the second form,
the provider's project setting will be used as a fallback.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>etag</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}(Computed) The etag of the project's IAM policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>member</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>role</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The role that should be applied. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Crypto<wbr>Key<wbr>IAMMember<wbr>Condition</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#CryptoKeyIAMMemberCondition">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#CryptoKeyIAMMemberCondition">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/kms?tab=doc#CryptoKeyIAMMemberConditionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/kms?tab=doc#CryptoKeyIAMMemberConditionOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Expression</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Textual representation of an expression in Common Expression Language syntax.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Title</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}A title for the expression, i.e. a short string describing its purpose.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}An optional description of the expression. This is a longer text which describes the expression, e.g. when hovered over it in a UI.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Expression</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Textual representation of an expression in Common Expression Language syntax.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Title</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}A title for the expression, i.e. a short string describing its purpose.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}An optional description of the expression. This is a longer text which describes the expression, e.g. when hovered over it in a UI.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>expression</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Textual representation of an expression in Common Expression Language syntax.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>title</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}A title for the expression, i.e. a short string describing its purpose.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}An optional description of the expression. This is a longer text which describes the expression, e.g. when hovered over it in a UI.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>expression</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Textual representation of an expression in Common Expression Language syntax.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>title</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}A title for the expression, i.e. a short string describing its purpose.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}An optional description of the expression. This is a longer text which describes the expression, e.g. when hovered over it in a UI.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}









<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-gcp">https://github.com/pulumi/pulumi-gcp</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    <dt>Notes</dt>
	<dd>This Pulumi package is based on the [`google-beta` Terraform Provider](https://github.com/terraform-providers/terraform-provider-google-beta).</dd>
</dl>

