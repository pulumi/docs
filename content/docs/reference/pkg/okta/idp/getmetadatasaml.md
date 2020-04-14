
---
title: "GetMetadataSaml"
block_external_search_index: true
---



Use this data source to retrieve SAML IdP metadata from Okta.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as okta from "@pulumi/okta";

const example = pulumi.output(okta.idp.getMetadataSaml({
    id: "<idp id>",
}, { async: true }));
```

> This content is derived from https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/d/idp_metadata_saml.html.markdown.





## Using GetMetadataSaml

{{< chooser language "javascript,typescript,python,go,csharp" / >}}


{{% choosable language typescript %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getMetadataSaml<span class="p">(</span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/okta/idp/#GetMetadataSamlArgs">GetMetadataSamlArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#InvokeOptions">InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/okta/idp/#GetMetadataSamlResult">GetMetadataSamlResult</a></span>></span></code></pre></div>
{{% /choosable %}}


{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_metadata_saml(</span>idp_id=None<span class="p">, </span>opts=None<span class="p">)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupMetadataSaml<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-okta/sdk/go/okta/idp?tab=doc#LookupMetadataSamlArgs">LookupMetadataSamlArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#InvokeOption">pulumi.InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-okta/sdk/go/okta/idp?tab=doc#LookupMetadataSamlResult">LookupMetadataSamlResult</a></span>, error)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static class </span><span class="nx">GetMetadataSaml </span><span class="p">{</span><span class="k">
    public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Okta/Pulumi.Okta.Idp.GetMetadataSamlResult.html">GetMetadataSamlResult</a></span>> <span class="p">InvokeAsync(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Okta/Pulumi.Okta.Idp.GetMetadataSamlArgs.html">GetMetadataSamlArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.InvokeOptions.html">InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span><span class="p">
}</span></code></pre></div>
{{% /choosable %}}



The following arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Idp<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The id of the IdP to retrieve metadata for.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Idp<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The id of the IdP to retrieve metadata for.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>idp<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The id of the IdP to retrieve metadata for.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>idp_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The id of the IdP to retrieve metadata for.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## GetMetadataSaml Result

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Assertions<wbr>Signed</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}whether assertions are signed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Authn<wbr>Request<wbr>Signed</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}whether authn requests are signed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Encryption<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}SAML request encryption certificate.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Entity<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Entity URL for instance `https://www.okta.com/saml2/service-provider/sposcfdmlybtwkdcgtuf`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Http<wbr>Post<wbr>Binding</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Post location from the SAML metadata.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Http<wbr>Redirect<wbr>Binding</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect location from the SAML metadata.
{{% /md %}}</dd>

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
        <span>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}raw IdP metadata.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Signing<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}SAML request signing certificate.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Idp<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Assertions<wbr>Signed</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}whether assertions are signed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Authn<wbr>Request<wbr>Signed</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}whether authn requests are signed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Encryption<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}SAML request encryption certificate.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Entity<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Entity URL for instance `https://www.okta.com/saml2/service-provider/sposcfdmlybtwkdcgtuf`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Http<wbr>Post<wbr>Binding</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Post location from the SAML metadata.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Http<wbr>Redirect<wbr>Binding</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect location from the SAML metadata.
{{% /md %}}</dd>

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
        <span>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}raw IdP metadata.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Signing<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}SAML request signing certificate.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Idp<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>assertions<wbr>Signed</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}whether assertions are signed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>authn<wbr>Request<wbr>Signed</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}whether authn requests are signed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>encryption<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}SAML request encryption certificate.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>entity<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Entity URL for instance `https://www.okta.com/saml2/service-provider/sposcfdmlybtwkdcgtuf`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>http<wbr>Post<wbr>Binding</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Post location from the SAML metadata.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>http<wbr>Redirect<wbr>Binding</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect location from the SAML metadata.
{{% /md %}}</dd>

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
        <span>metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}raw IdP metadata.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>signing<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}SAML request signing certificate.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>idp<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>assertions_<wbr>signed</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}whether assertions are signed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>authn_<wbr>request_<wbr>signed</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}whether authn requests are signed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>encryption_<wbr>certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}SAML request encryption certificate.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>entity_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Entity URL for instance `https://www.okta.com/saml2/service-provider/sposcfdmlybtwkdcgtuf`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>http_<wbr>post_<wbr>binding</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Post location from the SAML metadata.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>http_<wbr>redirect_<wbr>binding</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect location from the SAML metadata.
{{% /md %}}</dd>

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
        <span>metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}raw IdP metadata.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>signing_<wbr>certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}SAML request signing certificate.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>idp_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}







