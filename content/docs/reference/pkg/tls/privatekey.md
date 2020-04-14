
---
title: "PrivateKey"
block_external_search_index: true
---






## Create a PrivateKey Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/tls/#PrivateKey">PrivateKey</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/tls/#PrivateKeyArgs">PrivateKeyArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">PrivateKey</span><span class="p">(resource_name, opts=None, </span>algorithm=None<span class="p">, </span>ecdsa_curve=None<span class="p">, </span>rsa_bits=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewPrivateKey<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-tls/sdk/go/tls/?tab=doc#PrivateKeyArgs">PrivateKeyArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-tls/sdk/go/tls/?tab=doc#PrivateKey">PrivateKey</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Tls/Pulumi.Tls.PrivateKey.html">PrivateKey</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Tls/Pulumi.Tls.PrivateKeyArgs.html">PrivateKeyArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the algorithm to use for
the key. Currently-supported values are "RSA" and "ECDSA".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ecdsa<wbr>Curve</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}When `algorithm` is "ECDSA", the name of the elliptic
curve to use. May be any one of "P224", "P256", "P384" or "P521", with "P224" as the
default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Rsa<wbr>Bits</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}When `algorithm` is "RSA", the size of the generated
RSA key in bits. Defaults to 2048.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the algorithm to use for
the key. Currently-supported values are "RSA" and "ECDSA".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ecdsa<wbr>Curve</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}When `algorithm` is "ECDSA", the name of the elliptic
curve to use. May be any one of "P224", "P256", "P384" or "P521", with "P224" as the
default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Rsa<wbr>Bits</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}When `algorithm` is "RSA", the size of the generated
RSA key in bits. Defaults to 2048.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the algorithm to use for
the key. Currently-supported values are "RSA" and "ECDSA".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ecdsa<wbr>Curve</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}When `algorithm` is "ECDSA", the name of the elliptic
curve to use. May be any one of "P224", "P256", "P384" or "P521", with "P224" as the
default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>rsa<wbr>Bits</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}When `algorithm` is "RSA", the size of the generated
RSA key in bits. Defaults to 2048.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the algorithm to use for
the key. Currently-supported values are "RSA" and "ECDSA".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ecdsa_<wbr>curve</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}When `algorithm` is "ECDSA", the name of the elliptic
curve to use. May be any one of "P224", "P256", "P384" or "P521", with "P224" as the
default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>rsa_<wbr>bits</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}When `algorithm` is "RSA", the size of the generated
RSA key in bits. Defaults to 2048.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## PrivateKey Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Private<wbr>Key<wbr>Pem</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The private key data in PEM format.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Public<wbr>Key<wbr>Fingerprint<wbr>Md5</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The md5 hash of the public key data in
OpenSSH MD5 hash format, e.g. `aa:bb:cc:...`. Only available if the
selected private key format is compatible, as per the rules for
`public_key_openssh`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Public<wbr>Key<wbr>Openssh</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The public key data in OpenSSH `authorized_keys`
format, if the selected private key format is compatible. All RSA keys
are supported, and ECDSA keys with curves "P256", "P384" and "P521"
are supported. This attribute is empty if an incompatible ECDSA curve
is selected.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Public<wbr>Key<wbr>Pem</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The public key data in PEM format.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Private<wbr>Key<wbr>Pem</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The private key data in PEM format.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Public<wbr>Key<wbr>Fingerprint<wbr>Md5</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The md5 hash of the public key data in
OpenSSH MD5 hash format, e.g. `aa:bb:cc:...`. Only available if the
selected private key format is compatible, as per the rules for
`public_key_openssh`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Public<wbr>Key<wbr>Openssh</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The public key data in OpenSSH `authorized_keys`
format, if the selected private key format is compatible. All RSA keys
are supported, and ECDSA keys with curves "P256", "P384" and "P521"
are supported. This attribute is empty if an incompatible ECDSA curve
is selected.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Public<wbr>Key<wbr>Pem</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The public key data in PEM format.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>private<wbr>Key<wbr>Pem</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The private key data in PEM format.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>public<wbr>Key<wbr>Fingerprint<wbr>Md5</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The md5 hash of the public key data in
OpenSSH MD5 hash format, e.g. `aa:bb:cc:...`. Only available if the
selected private key format is compatible, as per the rules for
`public_key_openssh`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>public<wbr>Key<wbr>Openssh</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The public key data in OpenSSH `authorized_keys`
format, if the selected private key format is compatible. All RSA keys
are supported, and ECDSA keys with curves "P256", "P384" and "P521"
are supported. This attribute is empty if an incompatible ECDSA curve
is selected.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>public<wbr>Key<wbr>Pem</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The public key data in PEM format.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>private_<wbr>key_<wbr>pem</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The private key data in PEM format.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>public_<wbr>key_<wbr>fingerprint_<wbr>md5</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The md5 hash of the public key data in
OpenSSH MD5 hash format, e.g. `aa:bb:cc:...`. Only available if the
selected private key format is compatible, as per the rules for
`public_key_openssh`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>public_<wbr>key_<wbr>openssh</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The public key data in OpenSSH `authorized_keys`
format, if the selected private key format is compatible. All RSA keys
are supported, and ECDSA keys with curves "P256", "P384" and "P521"
are supported. This attribute is empty if an incompatible ECDSA curve
is selected.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>public_<wbr>key_<wbr>pem</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The public key data in PEM format.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing PrivateKey Resource

Get an existing PrivateKey resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/tls/#PrivateKeyState">PrivateKeyState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/tls/#PrivateKey">PrivateKey</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>algorithm=None<span class="p">, </span>ecdsa_curve=None<span class="p">, </span>private_key_pem=None<span class="p">, </span>public_key_fingerprint_md5=None<span class="p">, </span>public_key_openssh=None<span class="p">, </span>public_key_pem=None<span class="p">, </span>rsa_bits=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetPrivateKey<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-tls/sdk/go/tls/?tab=doc#PrivateKeyState">PrivateKeyState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-tls/sdk/go/tls/?tab=doc#PrivateKey">PrivateKey</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Tls/Pulumi.Tls.PrivateKey.html">PrivateKey</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Tls/Pulumi.Tls..PrivateKeyState.html">PrivateKeyState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the algorithm to use for
the key. Currently-supported values are "RSA" and "ECDSA".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ecdsa<wbr>Curve</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}When `algorithm` is "ECDSA", the name of the elliptic
curve to use. May be any one of "P224", "P256", "P384" or "P521", with "P224" as the
default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Private<wbr>Key<wbr>Pem</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The private key data in PEM format.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Public<wbr>Key<wbr>Fingerprint<wbr>Md5</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The md5 hash of the public key data in
OpenSSH MD5 hash format, e.g. `aa:bb:cc:...`. Only available if the
selected private key format is compatible, as per the rules for
`public_key_openssh`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Public<wbr>Key<wbr>Openssh</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The public key data in OpenSSH `authorized_keys`
format, if the selected private key format is compatible. All RSA keys
are supported, and ECDSA keys with curves "P256", "P384" and "P521"
are supported. This attribute is empty if an incompatible ECDSA curve
is selected.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Public<wbr>Key<wbr>Pem</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The public key data in PEM format.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Rsa<wbr>Bits</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}When `algorithm` is "RSA", the size of the generated
RSA key in bits. Defaults to 2048.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the algorithm to use for
the key. Currently-supported values are "RSA" and "ECDSA".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ecdsa<wbr>Curve</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}When `algorithm` is "ECDSA", the name of the elliptic
curve to use. May be any one of "P224", "P256", "P384" or "P521", with "P224" as the
default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Private<wbr>Key<wbr>Pem</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The private key data in PEM format.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Public<wbr>Key<wbr>Fingerprint<wbr>Md5</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The md5 hash of the public key data in
OpenSSH MD5 hash format, e.g. `aa:bb:cc:...`. Only available if the
selected private key format is compatible, as per the rules for
`public_key_openssh`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Public<wbr>Key<wbr>Openssh</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The public key data in OpenSSH `authorized_keys`
format, if the selected private key format is compatible. All RSA keys
are supported, and ECDSA keys with curves "P256", "P384" and "P521"
are supported. This attribute is empty if an incompatible ECDSA curve
is selected.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Public<wbr>Key<wbr>Pem</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The public key data in PEM format.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Rsa<wbr>Bits</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}When `algorithm` is "RSA", the size of the generated
RSA key in bits. Defaults to 2048.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the algorithm to use for
the key. Currently-supported values are "RSA" and "ECDSA".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ecdsa<wbr>Curve</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}When `algorithm` is "ECDSA", the name of the elliptic
curve to use. May be any one of "P224", "P256", "P384" or "P521", with "P224" as the
default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>private<wbr>Key<wbr>Pem</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The private key data in PEM format.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>public<wbr>Key<wbr>Fingerprint<wbr>Md5</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The md5 hash of the public key data in
OpenSSH MD5 hash format, e.g. `aa:bb:cc:...`. Only available if the
selected private key format is compatible, as per the rules for
`public_key_openssh`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>public<wbr>Key<wbr>Openssh</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The public key data in OpenSSH `authorized_keys`
format, if the selected private key format is compatible. All RSA keys
are supported, and ECDSA keys with curves "P256", "P384" and "P521"
are supported. This attribute is empty if an incompatible ECDSA curve
is selected.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>public<wbr>Key<wbr>Pem</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The public key data in PEM format.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>rsa<wbr>Bits</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}When `algorithm` is "RSA", the size of the generated
RSA key in bits. Defaults to 2048.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the algorithm to use for
the key. Currently-supported values are "RSA" and "ECDSA".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ecdsa_<wbr>curve</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}When `algorithm` is "ECDSA", the name of the elliptic
curve to use. May be any one of "P224", "P256", "P384" or "P521", with "P224" as the
default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>private_<wbr>key_<wbr>pem</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The private key data in PEM format.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>public_<wbr>key_<wbr>fingerprint_<wbr>md5</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The md5 hash of the public key data in
OpenSSH MD5 hash format, e.g. `aa:bb:cc:...`. Only available if the
selected private key format is compatible, as per the rules for
`public_key_openssh`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>public_<wbr>key_<wbr>openssh</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The public key data in OpenSSH `authorized_keys`
format, if the selected private key format is compatible. All RSA keys
are supported, and ECDSA keys with curves "P256", "P384" and "P521"
are supported. This attribute is empty if an incompatible ECDSA curve
is selected.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>public_<wbr>key_<wbr>pem</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The public key data in PEM format.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>rsa_<wbr>bits</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}When `algorithm` is "RSA", the size of the generated
RSA key in bits. Defaults to 2048.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}











<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-tls">https://github.com/pulumi/pulumi-tls</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    
</dl>

