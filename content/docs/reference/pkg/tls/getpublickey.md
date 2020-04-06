
---
title: "GetPublicKey"
block_external_search_index: true
---



Use this data source to get the public key from a PEM-encoded private key for use in other
resources.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as fs from "fs";
import * as tls from "@pulumi/tls";

const example = pulumi.output(tls.getPublicKey({
    privateKeyPem: fs.readFileSync("~/.ssh/id_rsa", "utf-8"),
}, { async: true }));
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-tls/blob/master/website/docs/d/public_key.html.md.





## Using GetPublicKey

{{< chooser language "javascript,typescript,python,go,csharp" / >}}


{{% choosable language typescript %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getPublicKey<span class="p">(</span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/tls/#GetPublicKeyArgs">GetPublicKeyArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#InvokeOptions">InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/tls/#GetPublicKeyResult">GetPublicKeyResult</a></span>></span></code></pre></div>
{{% /choosable %}}


{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_public_key(</span>private_key_pem=None<span class="p">, </span>opts=None<span class="p">)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupPublicKey<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-tls/sdk/go/tls/?tab=doc#GetPublicKeyArgs">GetPublicKeyArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#InvokeOption">InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-tls/sdk/go/tls/?tab=doc#LookupPublicKeyResult">LookupPublicKeyResult</a></span>, error)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static class </span><span class="nx">GetPublicKey </span><span class="p">{</span><span class="k">
    public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Tls/Pulumi.Tls.GetPublicKeyResult.html">GetPublicKeyResult</a></span>> <span class="p">InvokeAsync(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Tls/Pulumi.Tls.GetPublicKeyArgs.html">GetPublicKeyArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.InvokeOptions.html">InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span><span class="p">
}</span></code></pre></div>
{{% /choosable %}}



The following arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Private<wbr>Key<wbr>Pem</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The private key to use. Currently-supported key types are "RSA" or "ECDSA".
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Private<wbr>Key<wbr>Pem</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The private key to use. Currently-supported key types are "RSA" or "ECDSA".
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>private<wbr>Key<wbr>Pem</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The private key to use. Currently-supported key types are "RSA" or "ECDSA".
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>private_<wbr>key_<wbr>pem</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The private key to use. Currently-supported key types are "RSA" or "ECDSA".
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## GetPublicKey Result

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Algorithm</span>
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
        <span>Algorithm</span>
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
        <span>algorithm</span>
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
        <span>algorithm</span>
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







