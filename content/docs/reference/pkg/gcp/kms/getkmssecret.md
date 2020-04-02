
---
title: "GetKMSSecret"
block_external_search_index: true
---

This data source allows you to use data encrypted with Google Cloud KMS
within your resource definitions.

For more information see
[the official documentation](https://cloud.google.com/kms/docs/encrypt-decrypt).

> **NOTE**: Using this data provider will allow you to conceal secret data within your
resource definitions, but it does not take care of protecting that data in the
logging output, plan output, or state output.  Please take care to secure your secret
data outside of resource definitions.

> This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/google_kms_secret.html.markdown.





## Using GetKMSSecret

{{< chooser language "javascript,typescript,python,go,csharp" / >}}


{{% choosable language typescript %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getKMSSecret<span class="p">(</span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/kms/#GetKMSSecretArgs">GetKMSSecretArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#InvokeOptions">InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/kms/#GetKMSSecretResult">GetKMSSecretResult</a></span>></span></code></pre></div>
{{% /choosable %}}


{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_kms_secret(</span>additional_authenticated_data=None<span class="p">, </span>ciphertext=None<span class="p">, </span>crypto_key=None<span class="p">, </span>opts=None<span class="p">)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupKMSSecret<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/kms?tab=doc#LookupKMSSecretArgs">LookupKMSSecretArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#InvokeOption">InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/kms?tab=doc#LookupKMSSecretResult">LookupKMSSecretResult</a></span>, error)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static class </span><span class="nx">GetKMSSecret </span><span class="p">{</span><span class="k">
    public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Kms.GetKMSSecretResult.html">GetKMSSecretResult</a></span>> <span class="p">InvokeAsync(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Kms.GetKMSSecretArgs.html">GetKMSSecretArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.InvokeOptions.html">InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span><span class="p">
}</span></code></pre></div>
{{% /choosable %}}



The following arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Additional<wbr>Authenticated<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The [additional authenticated data](https://cloud.google.com/kms/docs/additional-authenticated-data) used for integrity checks during encryption and decryption.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Ciphertext</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ciphertext to be decrypted, encoded in base64
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Crypto<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The id of the CryptoKey that will be used to
decrypt the provided ciphertext. This is represented by the format
`{projectId}/{location}/{keyRingName}/{cryptoKeyName}`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Additional<wbr>Authenticated<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The [additional authenticated data](https://cloud.google.com/kms/docs/additional-authenticated-data) used for integrity checks during encryption and decryption.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Ciphertext</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ciphertext to be decrypted, encoded in base64
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Crypto<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The id of the CryptoKey that will be used to
decrypt the provided ciphertext. This is represented by the format
`{projectId}/{location}/{keyRingName}/{cryptoKeyName}`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>additional<wbr>Authenticated<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The [additional authenticated data](https://cloud.google.com/kms/docs/additional-authenticated-data) used for integrity checks during encryption and decryption.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>ciphertext</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ciphertext to be decrypted, encoded in base64
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>crypto<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The id of the CryptoKey that will be used to
decrypt the provided ciphertext. This is represented by the format
`{projectId}/{location}/{keyRingName}/{cryptoKeyName}`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>additional_<wbr>authenticated_<wbr>data</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The [additional authenticated data](https://cloud.google.com/kms/docs/additional-authenticated-data) used for integrity checks during encryption and decryption.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>ciphertext</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ciphertext to be decrypted, encoded in base64
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>crypto_<wbr>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The id of the CryptoKey that will be used to
decrypt the provided ciphertext. This is represented by the format
`{projectId}/{location}/{keyRingName}/{cryptoKeyName}`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## GetKMSSecret Result

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Additional<wbr>Authenticated<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ciphertext</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Crypto<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Plaintext</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Contains the result of decrypting the provided ciphertext.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Additional<wbr>Authenticated<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ciphertext</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Crypto<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Plaintext</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Contains the result of decrypting the provided ciphertext.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>additional<wbr>Authenticated<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ciphertext</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>crypto<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>plaintext</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Contains the result of decrypting the provided ciphertext.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>additional_<wbr>authenticated_<wbr>data</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ciphertext</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>crypto_<wbr>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>plaintext</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Contains the result of decrypting the provided ciphertext.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







