
---
title: "GetKeys"
block_external_search_index: true
---



Get the DNSKEY and DS records of DNSSEC-signed managed zones. For more information see the
[official documentation](https://cloud.google.com/dns/docs/dnskeys/)
and [API](https://cloud.google.com/dns/docs/reference/v1/dnsKeys).

> This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/datasource_dns_keys.html.markdown.





## Using GetKeys

{{< chooser language "javascript,typescript,python,go,csharp" / >}}


{{% choosable language typescript %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getKeys<span class="p">(</span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/dns/#GetKeysArgs">GetKeysArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#InvokeOptions">InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/dns/#GetKeysResult">GetKeysResult</a></span>></span></code></pre></div>
{{% /choosable %}}


{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_keys(</span>managed_zone=None<span class="p">, </span>project=None<span class="p">, </span>opts=None<span class="p">)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupKeys<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/dns?tab=doc#LookupKeysArgs">LookupKeysArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#InvokeOption">InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/dns?tab=doc#LookupKeysResult">LookupKeysResult</a></span>, error)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static class </span><span class="nx">GetKeys </span><span class="p">{</span><span class="k">
    public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Dns.GetKeysResult.html">GetKeysResult</a></span>> <span class="p">InvokeAsync(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Dns.GetKeysArgs.html">GetKeysArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.InvokeOptions.html">InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span><span class="p">
}</span></code></pre></div>
{{% /choosable %}}



The following arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Managed<wbr>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name or id of the Cloud DNS managed zone.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs. If `project` is not provided, the provider project is used.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Managed<wbr>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name or id of the Cloud DNS managed zone.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs. If `project` is not provided, the provider project is used.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>managed<wbr>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name or id of the Cloud DNS managed zone.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs. If `project` is not provided, the provider project is used.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>managed_<wbr>zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name or id of the Cloud DNS managed zone.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs. If `project` is not provided, the provider project is used.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## GetKeys Result

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

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
        <span>Key<wbr>Signing<wbr>Keys</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkeyskeysigningkey">List&lt;Get<wbr>Keys<wbr>Key<wbr>Signing<wbr>Key&gt;</a></span>
    </dt>
    <dd>{{% md %}}A list of Key-signing key (KSK) records. Structure is documented below. Additionally, the DS record is provided:
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Managed<wbr>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Zone<wbr>Signing<wbr>Keys</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkeyszonesigningkey">List&lt;Get<wbr>Keys<wbr>Zone<wbr>Signing<wbr>Key&gt;</a></span>
    </dt>
    <dd>{{% md %}}A list of Zone-signing key (ZSK) records. Structure is documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

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
        <span>Key<wbr>Signing<wbr>Keys</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkeyskeysigningkey">[]Get<wbr>Keys<wbr>Key<wbr>Signing<wbr>Key</a></span>
    </dt>
    <dd>{{% md %}}A list of Key-signing key (KSK) records. Structure is documented below. Additionally, the DS record is provided:
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Managed<wbr>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Zone<wbr>Signing<wbr>Keys</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkeyszonesigningkey">[]Get<wbr>Keys<wbr>Zone<wbr>Signing<wbr>Key</a></span>
    </dt>
    <dd>{{% md %}}A list of Zone-signing key (ZSK) records. Structure is documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

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
        <span>key<wbr>Signing<wbr>Keys</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkeyskeysigningkey">Get<wbr>Keys<wbr>Key<wbr>Signing<wbr>Key[]</a></span>
    </dt>
    <dd>{{% md %}}A list of Key-signing key (KSK) records. Structure is documented below. Additionally, the DS record is provided:
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>managed<wbr>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>zone<wbr>Signing<wbr>Keys</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkeyszonesigningkey">Get<wbr>Keys<wbr>Zone<wbr>Signing<wbr>Key[]</a></span>
    </dt>
    <dd>{{% md %}}A list of Zone-signing key (ZSK) records. Structure is documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

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
        <span>key_<wbr>signing_<wbr>keys</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkeyskeysigningkey">List[Get<wbr>Keys<wbr>Key<wbr>Signing<wbr>Key]</a></span>
    </dt>
    <dd>{{% md %}}A list of Key-signing key (KSK) records. Structure is documented below. Additionally, the DS record is provided:
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>managed_<wbr>zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>zone_<wbr>signing_<wbr>keys</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkeyszonesigningkey">List[Get<wbr>Keys<wbr>Zone<wbr>Signing<wbr>Key]</a></span>
    </dt>
    <dd>{{% md %}}A list of Zone-signing key (ZSK) records. Structure is documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Supporting Types

<h4>Get<wbr>Keys<wbr>Key<wbr>Signing<wbr>Key</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#GetKeysKeySigningKey">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/dns?tab=doc#GetKeysKeySigningKey">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}String mnemonic specifying the DNSSEC algorithm of this key. Immutable after creation time. Possible values are `ecdsap256sha256`, `ecdsap384sha384`, `rsasha1`, `rsasha256`, and `rsasha512`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Creation<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The time that this resource was created in the control plane. This is in RFC3339 text format.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A mutable string of at most 1024 characters associated with this resource for the user's convenience.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Digests</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkeyskeysigningkeydigest">List&lt;Get<wbr>Keys<wbr>Key<wbr>Signing<wbr>Key<wbr>Digest<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}A list of cryptographic hashes of the DNSKEY resource record associated with this DnsKey. These digests are needed to construct a DS record that points at this DNS key. Each contains:
- `digest` - The base-16 encoded bytes of this digest. Suitable for use in a DS resource record.
- `type` - Specifies the algorithm used to calculate this digest. Possible values are `sha1`, `sha256` and `sha384`
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Ds<wbr>Record</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The DS record based on the KSK record. This is used when [delegating](https://cloud.google.com/dns/docs/dnssec-advanced#subdelegation) DNSSEC-signed subdomains.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Unique identifier for the resource; defined by the server.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Is<wbr>Active</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Active keys will be used to sign subsequent changes to the ManagedZone. Inactive keys will still be present as DNSKEY Resource Records for the use of resolvers validating existing signatures.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Key<wbr>Length</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Length of the key in bits. Specified at creation time then immutable.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Key<wbr>Tag</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The key tag is a non-cryptographic hash of the a DNSKEY resource record associated with this DnsKey. The key tag can be used to identify a DNSKEY more quickly (but it is not a unique identifier). In particular, the key tag is used in a parent zone's DS record to point at the DNSKEY in this child ManagedZone. The key tag is a number in the range [0, 65535] and the algorithm to calculate it is specified in RFC4034 Appendix B.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Public<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Base64 encoded public half of this key.
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
    <dd>{{% md %}}String mnemonic specifying the DNSSEC algorithm of this key. Immutable after creation time. Possible values are `ecdsap256sha256`, `ecdsap384sha384`, `rsasha1`, `rsasha256`, and `rsasha512`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Creation<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The time that this resource was created in the control plane. This is in RFC3339 text format.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A mutable string of at most 1024 characters associated with this resource for the user's convenience.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Digests</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkeyskeysigningkeydigest">[]Get<wbr>Keys<wbr>Key<wbr>Signing<wbr>Key<wbr>Digest</a></span>
    </dt>
    <dd>{{% md %}}A list of cryptographic hashes of the DNSKEY resource record associated with this DnsKey. These digests are needed to construct a DS record that points at this DNS key. Each contains:
- `digest` - The base-16 encoded bytes of this digest. Suitable for use in a DS resource record.
- `type` - Specifies the algorithm used to calculate this digest. Possible values are `sha1`, `sha256` and `sha384`
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Ds<wbr>Record</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The DS record based on the KSK record. This is used when [delegating](https://cloud.google.com/dns/docs/dnssec-advanced#subdelegation) DNSSEC-signed subdomains.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Unique identifier for the resource; defined by the server.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Is<wbr>Active</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Active keys will be used to sign subsequent changes to the ManagedZone. Inactive keys will still be present as DNSKEY Resource Records for the use of resolvers validating existing signatures.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Key<wbr>Length</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Length of the key in bits. Specified at creation time then immutable.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Key<wbr>Tag</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The key tag is a non-cryptographic hash of the a DNSKEY resource record associated with this DnsKey. The key tag can be used to identify a DNSKEY more quickly (but it is not a unique identifier). In particular, the key tag is used in a parent zone's DS record to point at the DNSKEY in this child ManagedZone. The key tag is a number in the range [0, 65535] and the algorithm to calculate it is specified in RFC4034 Appendix B.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Public<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Base64 encoded public half of this key.
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
    <dd>{{% md %}}String mnemonic specifying the DNSSEC algorithm of this key. Immutable after creation time. Possible values are `ecdsap256sha256`, `ecdsap384sha384`, `rsasha1`, `rsasha256`, and `rsasha512`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>creation<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The time that this resource was created in the control plane. This is in RFC3339 text format.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A mutable string of at most 1024 characters associated with this resource for the user's convenience.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>digests</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkeyskeysigningkeydigest">Get<wbr>Keys<wbr>Key<wbr>Signing<wbr>Key<wbr>Digest[]</a></span>
    </dt>
    <dd>{{% md %}}A list of cryptographic hashes of the DNSKEY resource record associated with this DnsKey. These digests are needed to construct a DS record that points at this DNS key. Each contains:
- `digest` - The base-16 encoded bytes of this digest. Suitable for use in a DS resource record.
- `type` - Specifies the algorithm used to calculate this digest. Possible values are `sha1`, `sha256` and `sha384`
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>ds<wbr>Record</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The DS record based on the KSK record. This is used when [delegating](https://cloud.google.com/dns/docs/dnssec-advanced#subdelegation) DNSSEC-signed subdomains.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Unique identifier for the resource; defined by the server.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>is<wbr>Active</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Active keys will be used to sign subsequent changes to the ManagedZone. Inactive keys will still be present as DNSKEY Resource Records for the use of resolvers validating existing signatures.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>key<wbr>Length</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Length of the key in bits. Specified at creation time then immutable.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>key<wbr>Tag</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The key tag is a non-cryptographic hash of the a DNSKEY resource record associated with this DnsKey. The key tag can be used to identify a DNSKEY more quickly (but it is not a unique identifier). In particular, the key tag is used in a parent zone's DS record to point at the DNSKEY in this child ManagedZone. The key tag is a number in the range [0, 65535] and the algorithm to calculate it is specified in RFC4034 Appendix B.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>public<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Base64 encoded public half of this key.
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
    <dd>{{% md %}}String mnemonic specifying the DNSSEC algorithm of this key. Immutable after creation time. Possible values are `ecdsap256sha256`, `ecdsap384sha384`, `rsasha1`, `rsasha256`, and `rsasha512`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>creation_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The time that this resource was created in the control plane. This is in RFC3339 text format.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A mutable string of at most 1024 characters associated with this resource for the user's convenience.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>digests</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkeyskeysigningkeydigest">List[Get<wbr>Keys<wbr>Key<wbr>Signing<wbr>Key<wbr>Digest]</a></span>
    </dt>
    <dd>{{% md %}}A list of cryptographic hashes of the DNSKEY resource record associated with this DnsKey. These digests are needed to construct a DS record that points at this DNS key. Each contains:
- `digest` - The base-16 encoded bytes of this digest. Suitable for use in a DS resource record.
- `type` - Specifies the algorithm used to calculate this digest. Possible values are `sha1`, `sha256` and `sha384`
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>ds<wbr>Record</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The DS record based on the KSK record. This is used when [delegating](https://cloud.google.com/dns/docs/dnssec-advanced#subdelegation) DNSSEC-signed subdomains.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Unique identifier for the resource; defined by the server.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>is<wbr>Active</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Active keys will be used to sign subsequent changes to the ManagedZone. Inactive keys will still be present as DNSKEY Resource Records for the use of resolvers validating existing signatures.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>key<wbr>Length</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Length of the key in bits. Specified at creation time then immutable.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>key<wbr>Tag</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The key tag is a non-cryptographic hash of the a DNSKEY resource record associated with this DnsKey. The key tag can be used to identify a DNSKEY more quickly (but it is not a unique identifier). In particular, the key tag is used in a parent zone's DS record to point at the DNSKEY in this child ManagedZone. The key tag is a number in the range [0, 65535] and the algorithm to calculate it is specified in RFC4034 Appendix B.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>public_<wbr>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Base64 encoded public half of this key.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Get<wbr>Keys<wbr>Key<wbr>Signing<wbr>Key<wbr>Digest</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#GetKeysKeySigningKeyDigest">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/dns?tab=doc#GetKeysKeySigningKeyDigest">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Digest</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Digest</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>digest</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>digest</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Get<wbr>Keys<wbr>Zone<wbr>Signing<wbr>Key</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#GetKeysZoneSigningKey">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/dns?tab=doc#GetKeysZoneSigningKey">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}String mnemonic specifying the DNSSEC algorithm of this key. Immutable after creation time. Possible values are `ecdsap256sha256`, `ecdsap384sha384`, `rsasha1`, `rsasha256`, and `rsasha512`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Creation<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The time that this resource was created in the control plane. This is in RFC3339 text format.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A mutable string of at most 1024 characters associated with this resource for the user's convenience.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Digests</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkeyszonesigningkeydigest">List&lt;Get<wbr>Keys<wbr>Zone<wbr>Signing<wbr>Key<wbr>Digest<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}A list of cryptographic hashes of the DNSKEY resource record associated with this DnsKey. These digests are needed to construct a DS record that points at this DNS key. Each contains:
- `digest` - The base-16 encoded bytes of this digest. Suitable for use in a DS resource record.
- `type` - Specifies the algorithm used to calculate this digest. Possible values are `sha1`, `sha256` and `sha384`
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Unique identifier for the resource; defined by the server.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Is<wbr>Active</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Active keys will be used to sign subsequent changes to the ManagedZone. Inactive keys will still be present as DNSKEY Resource Records for the use of resolvers validating existing signatures.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Key<wbr>Length</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Length of the key in bits. Specified at creation time then immutable.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Key<wbr>Tag</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The key tag is a non-cryptographic hash of the a DNSKEY resource record associated with this DnsKey. The key tag can be used to identify a DNSKEY more quickly (but it is not a unique identifier). In particular, the key tag is used in a parent zone's DS record to point at the DNSKEY in this child ManagedZone. The key tag is a number in the range [0, 65535] and the algorithm to calculate it is specified in RFC4034 Appendix B.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Public<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Base64 encoded public half of this key.
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
    <dd>{{% md %}}String mnemonic specifying the DNSSEC algorithm of this key. Immutable after creation time. Possible values are `ecdsap256sha256`, `ecdsap384sha384`, `rsasha1`, `rsasha256`, and `rsasha512`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Creation<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The time that this resource was created in the control plane. This is in RFC3339 text format.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A mutable string of at most 1024 characters associated with this resource for the user's convenience.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Digests</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkeyszonesigningkeydigest">[]Get<wbr>Keys<wbr>Zone<wbr>Signing<wbr>Key<wbr>Digest</a></span>
    </dt>
    <dd>{{% md %}}A list of cryptographic hashes of the DNSKEY resource record associated with this DnsKey. These digests are needed to construct a DS record that points at this DNS key. Each contains:
- `digest` - The base-16 encoded bytes of this digest. Suitable for use in a DS resource record.
- `type` - Specifies the algorithm used to calculate this digest. Possible values are `sha1`, `sha256` and `sha384`
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Unique identifier for the resource; defined by the server.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Is<wbr>Active</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Active keys will be used to sign subsequent changes to the ManagedZone. Inactive keys will still be present as DNSKEY Resource Records for the use of resolvers validating existing signatures.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Key<wbr>Length</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Length of the key in bits. Specified at creation time then immutable.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Key<wbr>Tag</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The key tag is a non-cryptographic hash of the a DNSKEY resource record associated with this DnsKey. The key tag can be used to identify a DNSKEY more quickly (but it is not a unique identifier). In particular, the key tag is used in a parent zone's DS record to point at the DNSKEY in this child ManagedZone. The key tag is a number in the range [0, 65535] and the algorithm to calculate it is specified in RFC4034 Appendix B.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Public<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Base64 encoded public half of this key.
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
    <dd>{{% md %}}String mnemonic specifying the DNSSEC algorithm of this key. Immutable after creation time. Possible values are `ecdsap256sha256`, `ecdsap384sha384`, `rsasha1`, `rsasha256`, and `rsasha512`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>creation<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The time that this resource was created in the control plane. This is in RFC3339 text format.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A mutable string of at most 1024 characters associated with this resource for the user's convenience.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>digests</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkeyszonesigningkeydigest">Get<wbr>Keys<wbr>Zone<wbr>Signing<wbr>Key<wbr>Digest[]</a></span>
    </dt>
    <dd>{{% md %}}A list of cryptographic hashes of the DNSKEY resource record associated with this DnsKey. These digests are needed to construct a DS record that points at this DNS key. Each contains:
- `digest` - The base-16 encoded bytes of this digest. Suitable for use in a DS resource record.
- `type` - Specifies the algorithm used to calculate this digest. Possible values are `sha1`, `sha256` and `sha384`
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Unique identifier for the resource; defined by the server.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>is<wbr>Active</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Active keys will be used to sign subsequent changes to the ManagedZone. Inactive keys will still be present as DNSKEY Resource Records for the use of resolvers validating existing signatures.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>key<wbr>Length</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Length of the key in bits. Specified at creation time then immutable.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>key<wbr>Tag</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The key tag is a non-cryptographic hash of the a DNSKEY resource record associated with this DnsKey. The key tag can be used to identify a DNSKEY more quickly (but it is not a unique identifier). In particular, the key tag is used in a parent zone's DS record to point at the DNSKEY in this child ManagedZone. The key tag is a number in the range [0, 65535] and the algorithm to calculate it is specified in RFC4034 Appendix B.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>public<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Base64 encoded public half of this key.
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
    <dd>{{% md %}}String mnemonic specifying the DNSSEC algorithm of this key. Immutable after creation time. Possible values are `ecdsap256sha256`, `ecdsap384sha384`, `rsasha1`, `rsasha256`, and `rsasha512`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>creation_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The time that this resource was created in the control plane. This is in RFC3339 text format.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A mutable string of at most 1024 characters associated with this resource for the user's convenience.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>digests</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkeyszonesigningkeydigest">List[Get<wbr>Keys<wbr>Zone<wbr>Signing<wbr>Key<wbr>Digest]</a></span>
    </dt>
    <dd>{{% md %}}A list of cryptographic hashes of the DNSKEY resource record associated with this DnsKey. These digests are needed to construct a DS record that points at this DNS key. Each contains:
- `digest` - The base-16 encoded bytes of this digest. Suitable for use in a DS resource record.
- `type` - Specifies the algorithm used to calculate this digest. Possible values are `sha1`, `sha256` and `sha384`
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Unique identifier for the resource; defined by the server.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>is<wbr>Active</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Active keys will be used to sign subsequent changes to the ManagedZone. Inactive keys will still be present as DNSKEY Resource Records for the use of resolvers validating existing signatures.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>key<wbr>Length</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Length of the key in bits. Specified at creation time then immutable.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>key<wbr>Tag</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The key tag is a non-cryptographic hash of the a DNSKEY resource record associated with this DnsKey. The key tag can be used to identify a DNSKEY more quickly (but it is not a unique identifier). In particular, the key tag is used in a parent zone's DS record to point at the DNSKEY in this child ManagedZone. The key tag is a number in the range [0, 65535] and the algorithm to calculate it is specified in RFC4034 Appendix B.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>public_<wbr>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Base64 encoded public half of this key.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Get<wbr>Keys<wbr>Zone<wbr>Signing<wbr>Key<wbr>Digest</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#GetKeysZoneSigningKeyDigest">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/dns?tab=doc#GetKeysZoneSigningKeyDigest">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Digest</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Digest</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>digest</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>digest</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}







