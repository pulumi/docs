
---
title: "InterconnectAttachment"
block_external_search_index: true
---



Represents an InterconnectAttachment (VLAN attachment) resource. For more
information, see Creating VLAN Attachments.



## Create a InterconnectAttachment Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/compute/#InterconnectAttachment">InterconnectAttachment</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/compute/#InterconnectAttachmentArgs">InterconnectAttachmentArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">InterconnectAttachment</span><span class="p">(resource_name, opts=None, </span>admin_enabled=None<span class="p">, </span>bandwidth=None<span class="p">, </span>candidate_subnets=None<span class="p">, </span>description=None<span class="p">, </span>edge_availability_domain=None<span class="p">, </span>interconnect=None<span class="p">, </span>name=None<span class="p">, </span>project=None<span class="p">, </span>region=None<span class="p">, </span>router=None<span class="p">, </span>type=None<span class="p">, </span>vlan_tag8021q=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewInterconnectAttachment<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/compute?tab=doc#InterconnectAttachmentArgs">InterconnectAttachmentArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/compute?tab=doc#InterconnectAttachment">InterconnectAttachment</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Compute.InterconnectAttachment.html">InterconnectAttachment</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Compute.InterconnectAttachmentArgs.html">InterconnectAttachmentArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Router</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}URL of the cloud router to be used for dynamic routing. This router must be in the same region as this
InterconnectAttachment. The InterconnectAttachment will automatically connect the Interconnect to the network & region
within which the Cloud Router is configured.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Admin<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether the VLAN attachment is enabled or disabled. When using PARTNER type this will Pre-Activate the interconnect
attachment
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bandwidth</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Provisioned bandwidth capacity for the interconnect attachment. For attachments of type DEDICATED, the user can set the
bandwidth. For attachments of type PARTNER, the Google Partner that is operating the interconnect must set the
bandwidth. Output only for PARTNER type, mutable for PARTNER_PROVIDER and DEDICATED, Defaults to BPS_10G
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Candidate<wbr>Subnets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}Up to 16 candidate prefixes that can be used to restrict the allocation of cloudRouterIpAddress and
customerRouterIpAddress for this attachment. All prefixes must be within link-local address space (169.254.0.0/16) and
must be /29 or shorter (/28, /27, etc). Google will attempt to select an unused /29 from the supplied candidate
prefix(es). The request will fail if all possible /29s are in use on Google's edge. If not supplied, Google will
randomly select an unused /29 from all of link-local space.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}An optional description of this resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Edge<wbr>Availability<wbr>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Desired availability domain for the attachment. Only available for type PARTNER, at creation time. For improved
reliability, customers should configure a pair of attachments with one per availability domain. The selected
availability domain will be provided to the Partner via the pairing key so that the provisioned circuit will lie in the
specified domain. If not specified, the value will default to AVAILABILITY_DOMAIN_ANY.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Interconnect</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}URL of the underlying Interconnect object that this attachment's traffic will traverse through. Required if type is
DEDICATED, must not be set if type is PARTNER.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and
comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression
'[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Region where the regional interconnect attachment resides.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The type of InterconnectAttachment you wish to create. Defaults to DEDICATED.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vlan<wbr>Tag8021q</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The IEEE 802.1Q VLAN tag for this attachment, in the range 2-4094. When using PARTNER type this will be managed
upstream.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Router</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}URL of the cloud router to be used for dynamic routing. This router must be in the same region as this
InterconnectAttachment. The InterconnectAttachment will automatically connect the Interconnect to the network & region
within which the Cloud Router is configured.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Admin<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether the VLAN attachment is enabled or disabled. When using PARTNER type this will Pre-Activate the interconnect
attachment
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bandwidth</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Provisioned bandwidth capacity for the interconnect attachment. For attachments of type DEDICATED, the user can set the
bandwidth. For attachments of type PARTNER, the Google Partner that is operating the interconnect must set the
bandwidth. Output only for PARTNER type, mutable for PARTNER_PROVIDER and DEDICATED, Defaults to BPS_10G
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Candidate<wbr>Subnets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}Up to 16 candidate prefixes that can be used to restrict the allocation of cloudRouterIpAddress and
customerRouterIpAddress for this attachment. All prefixes must be within link-local address space (169.254.0.0/16) and
must be /29 or shorter (/28, /27, etc). Google will attempt to select an unused /29 from the supplied candidate
prefix(es). The request will fail if all possible /29s are in use on Google's edge. If not supplied, Google will
randomly select an unused /29 from all of link-local space.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}An optional description of this resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Edge<wbr>Availability<wbr>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Desired availability domain for the attachment. Only available for type PARTNER, at creation time. For improved
reliability, customers should configure a pair of attachments with one per availability domain. The selected
availability domain will be provided to the Partner via the pairing key so that the provisioned circuit will lie in the
specified domain. If not specified, the value will default to AVAILABILITY_DOMAIN_ANY.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Interconnect</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}URL of the underlying Interconnect object that this attachment's traffic will traverse through. Required if type is
DEDICATED, must not be set if type is PARTNER.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and
comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression
'[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Region where the regional interconnect attachment resides.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The type of InterconnectAttachment you wish to create. Defaults to DEDICATED.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vlan<wbr>Tag8021q</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The IEEE 802.1Q VLAN tag for this attachment, in the range 2-4094. When using PARTNER type this will be managed
upstream.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>router</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}URL of the cloud router to be used for dynamic routing. This router must be in the same region as this
InterconnectAttachment. The InterconnectAttachment will automatically connect the Interconnect to the network & region
within which the Cloud Router is configured.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>admin<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Whether the VLAN attachment is enabled or disabled. When using PARTNER type this will Pre-Activate the interconnect
attachment
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bandwidth</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Provisioned bandwidth capacity for the interconnect attachment. For attachments of type DEDICATED, the user can set the
bandwidth. For attachments of type PARTNER, the Google Partner that is operating the interconnect must set the
bandwidth. Output only for PARTNER type, mutable for PARTNER_PROVIDER and DEDICATED, Defaults to BPS_10G
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>candidate<wbr>Subnets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}Up to 16 candidate prefixes that can be used to restrict the allocation of cloudRouterIpAddress and
customerRouterIpAddress for this attachment. All prefixes must be within link-local address space (169.254.0.0/16) and
must be /29 or shorter (/28, /27, etc). Google will attempt to select an unused /29 from the supplied candidate
prefix(es). The request will fail if all possible /29s are in use on Google's edge. If not supplied, Google will
randomly select an unused /29 from all of link-local space.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}An optional description of this resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>edge<wbr>Availability<wbr>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Desired availability domain for the attachment. Only available for type PARTNER, at creation time. For improved
reliability, customers should configure a pair of attachments with one per availability domain. The selected
availability domain will be provided to the Partner via the pairing key so that the provisioned circuit will lie in the
specified domain. If not specified, the value will default to AVAILABILITY_DOMAIN_ANY.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>interconnect</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}URL of the underlying Interconnect object that this attachment's traffic will traverse through. Required if type is
DEDICATED, must not be set if type is PARTNER.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and
comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression
'[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Region where the regional interconnect attachment resides.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The type of InterconnectAttachment you wish to create. Defaults to DEDICATED.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vlan<wbr>Tag8021q</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The IEEE 802.1Q VLAN tag for this attachment, in the range 2-4094. When using PARTNER type this will be managed
upstream.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>router</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}URL of the cloud router to be used for dynamic routing. This router must be in the same region as this
InterconnectAttachment. The InterconnectAttachment will automatically connect the Interconnect to the network & region
within which the Cloud Router is configured.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>admin_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether the VLAN attachment is enabled or disabled. When using PARTNER type this will Pre-Activate the interconnect
attachment
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bandwidth</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Provisioned bandwidth capacity for the interconnect attachment. For attachments of type DEDICATED, the user can set the
bandwidth. For attachments of type PARTNER, the Google Partner that is operating the interconnect must set the
bandwidth. Output only for PARTNER type, mutable for PARTNER_PROVIDER and DEDICATED, Defaults to BPS_10G
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>candidate_<wbr>subnets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}Up to 16 candidate prefixes that can be used to restrict the allocation of cloudRouterIpAddress and
customerRouterIpAddress for this attachment. All prefixes must be within link-local address space (169.254.0.0/16) and
must be /29 or shorter (/28, /27, etc). Google will attempt to select an unused /29 from the supplied candidate
prefix(es). The request will fail if all possible /29s are in use on Google's edge. If not supplied, Google will
randomly select an unused /29 from all of link-local space.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}An optional description of this resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>edge_<wbr>availability_<wbr>domain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Desired availability domain for the attachment. Only available for type PARTNER, at creation time. For improved
reliability, customers should configure a pair of attachments with one per availability domain. The selected
availability domain will be provided to the Partner via the pairing key so that the provisioned circuit will lie in the
specified domain. If not specified, the value will default to AVAILABILITY_DOMAIN_ANY.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>interconnect</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}URL of the underlying Interconnect object that this attachment's traffic will traverse through. Required if type is
DEDICATED, must not be set if type is PARTNER.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and
comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression
'[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Region where the regional interconnect attachment resides.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The type of InterconnectAttachment you wish to create. Defaults to DEDICATED.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vlan_<wbr>tag8021q</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The IEEE 802.1Q VLAN tag for this attachment, in the range 2-4094. When using PARTNER type this will be managed
upstream.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## InterconnectAttachment Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Cloud<wbr>Router<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}IPv4 address + prefix length to be configured on Cloud Router Interface for this interconnect attachment.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Creation<wbr>Timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Creation timestamp in RFC3339 text format.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Customer<wbr>Router<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}IPv4 address + prefix length to be configured on the customer router subinterface for this interconnect attachment.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Google<wbr>Reference<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Google reference ID, to be used when raising support tickets with Google or otherwise to debug backend connectivity
issues.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Pairing<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}[Output only for type PARTNER. Not present for DEDICATED]. The opaque identifier of an PARTNER attachment used to
initiate provisioning with a selected partner. Of the form "XXXXX/region/domain"
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Partner<wbr>Asn</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}[Output only for type PARTNER. Not present for DEDICATED]. Optional BGP ASN for the router that should be supplied by a
layer 3 Partner if they configured BGP on behalf of the customer.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Private<wbr>Interconnect<wbr>Info</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interconnectattachmentprivateinterconnectinfo">Interconnect<wbr>Attachment<wbr>Private<wbr>Interconnect<wbr>Info</a></span>
    </dt>
    <dd>{{% md %}}Information specific to an InterconnectAttachment. This property is populated if the interconnect that this is attached
to is of type DEDICATED.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>State</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}[Output Only] The current state of this attachment's functionality.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Cloud<wbr>Router<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}IPv4 address + prefix length to be configured on Cloud Router Interface for this interconnect attachment.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Creation<wbr>Timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Creation timestamp in RFC3339 text format.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Customer<wbr>Router<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}IPv4 address + prefix length to be configured on the customer router subinterface for this interconnect attachment.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Google<wbr>Reference<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Google reference ID, to be used when raising support tickets with Google or otherwise to debug backend connectivity
issues.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Pairing<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}[Output only for type PARTNER. Not present for DEDICATED]. The opaque identifier of an PARTNER attachment used to
initiate provisioning with a selected partner. Of the form "XXXXX/region/domain"
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Partner<wbr>Asn</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}[Output only for type PARTNER. Not present for DEDICATED]. Optional BGP ASN for the router that should be supplied by a
layer 3 Partner if they configured BGP on behalf of the customer.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Private<wbr>Interconnect<wbr>Info</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interconnectattachmentprivateinterconnectinfo">Interconnect<wbr>Attachment<wbr>Private<wbr>Interconnect<wbr>Info</a></span>
    </dt>
    <dd>{{% md %}}Information specific to an InterconnectAttachment. This property is populated if the interconnect that this is attached
to is of type DEDICATED.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>State</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}[Output Only] The current state of this attachment's functionality.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>cloud<wbr>Router<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}IPv4 address + prefix length to be configured on Cloud Router Interface for this interconnect attachment.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>creation<wbr>Timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Creation timestamp in RFC3339 text format.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>customer<wbr>Router<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}IPv4 address + prefix length to be configured on the customer router subinterface for this interconnect attachment.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>google<wbr>Reference<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Google reference ID, to be used when raising support tickets with Google or otherwise to debug backend connectivity
issues.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>pairing<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}[Output only for type PARTNER. Not present for DEDICATED]. The opaque identifier of an PARTNER attachment used to
initiate provisioning with a selected partner. Of the form "XXXXX/region/domain"
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>partner<wbr>Asn</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}[Output only for type PARTNER. Not present for DEDICATED]. Optional BGP ASN for the router that should be supplied by a
layer 3 Partner if they configured BGP on behalf of the customer.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>private<wbr>Interconnect<wbr>Info</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interconnectattachmentprivateinterconnectinfo">Interconnect<wbr>Attachment<wbr>Private<wbr>Interconnect<wbr>Info</a></span>
    </dt>
    <dd>{{% md %}}Information specific to an InterconnectAttachment. This property is populated if the interconnect that this is attached
to is of type DEDICATED.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>state</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}[Output Only] The current state of this attachment's functionality.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>cloud_<wbr>router_<wbr>ip_<wbr>address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}IPv4 address + prefix length to be configured on Cloud Router Interface for this interconnect attachment.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>creation_<wbr>timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Creation timestamp in RFC3339 text format.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>customer_<wbr>router_<wbr>ip_<wbr>address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}IPv4 address + prefix length to be configured on the customer router subinterface for this interconnect attachment.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>google_<wbr>reference_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Google reference ID, to be used when raising support tickets with Google or otherwise to debug backend connectivity
issues.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>pairing_<wbr>key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}[Output only for type PARTNER. Not present for DEDICATED]. The opaque identifier of an PARTNER attachment used to
initiate provisioning with a selected partner. Of the form "XXXXX/region/domain"
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>partner_<wbr>asn</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}[Output only for type PARTNER. Not present for DEDICATED]. Optional BGP ASN for the router that should be supplied by a
layer 3 Partner if they configured BGP on behalf of the customer.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>private_<wbr>interconnect_<wbr>info</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interconnectattachmentprivateinterconnectinfo">Dict[Interconnect<wbr>Attachment<wbr>Private<wbr>Interconnect<wbr>Info]</a></span>
    </dt>
    <dd>{{% md %}}Information specific to an InterconnectAttachment. This property is populated if the interconnect that this is attached
to is of type DEDICATED.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>self_<wbr>link</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>state</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}[Output Only] The current state of this attachment's functionality.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing InterconnectAttachment Resource

Get an existing InterconnectAttachment resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/compute/#InterconnectAttachmentState">InterconnectAttachmentState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/compute/#InterconnectAttachment">InterconnectAttachment</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>admin_enabled=None<span class="p">, </span>bandwidth=None<span class="p">, </span>candidate_subnets=None<span class="p">, </span>cloud_router_ip_address=None<span class="p">, </span>creation_timestamp=None<span class="p">, </span>customer_router_ip_address=None<span class="p">, </span>description=None<span class="p">, </span>edge_availability_domain=None<span class="p">, </span>google_reference_id=None<span class="p">, </span>interconnect=None<span class="p">, </span>name=None<span class="p">, </span>pairing_key=None<span class="p">, </span>partner_asn=None<span class="p">, </span>private_interconnect_info=None<span class="p">, </span>project=None<span class="p">, </span>region=None<span class="p">, </span>router=None<span class="p">, </span>self_link=None<span class="p">, </span>state=None<span class="p">, </span>type=None<span class="p">, </span>vlan_tag8021q=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetInterconnectAttachment<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/compute?tab=doc#InterconnectAttachmentState">InterconnectAttachmentState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/compute?tab=doc#InterconnectAttachment">InterconnectAttachment</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Compute.InterconnectAttachment.html">InterconnectAttachment</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Compute.InterconnectAttachmentState.html">InterconnectAttachmentState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Admin<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether the VLAN attachment is enabled or disabled. When using PARTNER type this will Pre-Activate the interconnect
attachment
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bandwidth</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Provisioned bandwidth capacity for the interconnect attachment. For attachments of type DEDICATED, the user can set the
bandwidth. For attachments of type PARTNER, the Google Partner that is operating the interconnect must set the
bandwidth. Output only for PARTNER type, mutable for PARTNER_PROVIDER and DEDICATED, Defaults to BPS_10G
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Candidate<wbr>Subnets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}Up to 16 candidate prefixes that can be used to restrict the allocation of cloudRouterIpAddress and
customerRouterIpAddress for this attachment. All prefixes must be within link-local address space (169.254.0.0/16) and
must be /29 or shorter (/28, /27, etc). Google will attempt to select an unused /29 from the supplied candidate
prefix(es). The request will fail if all possible /29s are in use on Google's edge. If not supplied, Google will
randomly select an unused /29 from all of link-local space.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cloud<wbr>Router<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}IPv4 address + prefix length to be configured on Cloud Router Interface for this interconnect attachment.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Creation<wbr>Timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Creation timestamp in RFC3339 text format.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Customer<wbr>Router<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}IPv4 address + prefix length to be configured on the customer router subinterface for this interconnect attachment.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}An optional description of this resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Edge<wbr>Availability<wbr>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Desired availability domain for the attachment. Only available for type PARTNER, at creation time. For improved
reliability, customers should configure a pair of attachments with one per availability domain. The selected
availability domain will be provided to the Partner via the pairing key so that the provisioned circuit will lie in the
specified domain. If not specified, the value will default to AVAILABILITY_DOMAIN_ANY.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Google<wbr>Reference<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Google reference ID, to be used when raising support tickets with Google or otherwise to debug backend connectivity
issues.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Interconnect</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}URL of the underlying Interconnect object that this attachment's traffic will traverse through. Required if type is
DEDICATED, must not be set if type is PARTNER.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and
comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression
'[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pairing<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}[Output only for type PARTNER. Not present for DEDICATED]. The opaque identifier of an PARTNER attachment used to
initiate provisioning with a selected partner. Of the form "XXXXX/region/domain"
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Partner<wbr>Asn</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}[Output only for type PARTNER. Not present for DEDICATED]. Optional BGP ASN for the router that should be supplied by a
layer 3 Partner if they configured BGP on behalf of the customer.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Private<wbr>Interconnect<wbr>Info</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interconnectattachmentprivateinterconnectinfo">Interconnect<wbr>Attachment<wbr>Private<wbr>Interconnect<wbr>Info<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}Information specific to an InterconnectAttachment. This property is populated if the interconnect that this is attached
to is of type DEDICATED.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Region where the regional interconnect attachment resides.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Router</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}URL of the cloud router to be used for dynamic routing. This router must be in the same region as this
InterconnectAttachment. The InterconnectAttachment will automatically connect the Interconnect to the network & region
within which the Cloud Router is configured.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>State</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}[Output Only] The current state of this attachment's functionality.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The type of InterconnectAttachment you wish to create. Defaults to DEDICATED.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vlan<wbr>Tag8021q</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The IEEE 802.1Q VLAN tag for this attachment, in the range 2-4094. When using PARTNER type this will be managed
upstream.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Admin<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether the VLAN attachment is enabled or disabled. When using PARTNER type this will Pre-Activate the interconnect
attachment
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bandwidth</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Provisioned bandwidth capacity for the interconnect attachment. For attachments of type DEDICATED, the user can set the
bandwidth. For attachments of type PARTNER, the Google Partner that is operating the interconnect must set the
bandwidth. Output only for PARTNER type, mutable for PARTNER_PROVIDER and DEDICATED, Defaults to BPS_10G
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Candidate<wbr>Subnets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}Up to 16 candidate prefixes that can be used to restrict the allocation of cloudRouterIpAddress and
customerRouterIpAddress for this attachment. All prefixes must be within link-local address space (169.254.0.0/16) and
must be /29 or shorter (/28, /27, etc). Google will attempt to select an unused /29 from the supplied candidate
prefix(es). The request will fail if all possible /29s are in use on Google's edge. If not supplied, Google will
randomly select an unused /29 from all of link-local space.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cloud<wbr>Router<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}IPv4 address + prefix length to be configured on Cloud Router Interface for this interconnect attachment.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Creation<wbr>Timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Creation timestamp in RFC3339 text format.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Customer<wbr>Router<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}IPv4 address + prefix length to be configured on the customer router subinterface for this interconnect attachment.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}An optional description of this resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Edge<wbr>Availability<wbr>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Desired availability domain for the attachment. Only available for type PARTNER, at creation time. For improved
reliability, customers should configure a pair of attachments with one per availability domain. The selected
availability domain will be provided to the Partner via the pairing key so that the provisioned circuit will lie in the
specified domain. If not specified, the value will default to AVAILABILITY_DOMAIN_ANY.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Google<wbr>Reference<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Google reference ID, to be used when raising support tickets with Google or otherwise to debug backend connectivity
issues.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Interconnect</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}URL of the underlying Interconnect object that this attachment's traffic will traverse through. Required if type is
DEDICATED, must not be set if type is PARTNER.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and
comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression
'[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pairing<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}[Output only for type PARTNER. Not present for DEDICATED]. The opaque identifier of an PARTNER attachment used to
initiate provisioning with a selected partner. Of the form "XXXXX/region/domain"
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Partner<wbr>Asn</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}[Output only for type PARTNER. Not present for DEDICATED]. Optional BGP ASN for the router that should be supplied by a
layer 3 Partner if they configured BGP on behalf of the customer.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Private<wbr>Interconnect<wbr>Info</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interconnectattachmentprivateinterconnectinfo">Interconnect<wbr>Attachment<wbr>Private<wbr>Interconnect<wbr>Info</a></span>
    </dt>
    <dd>{{% md %}}Information specific to an InterconnectAttachment. This property is populated if the interconnect that this is attached
to is of type DEDICATED.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Region where the regional interconnect attachment resides.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Router</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}URL of the cloud router to be used for dynamic routing. This router must be in the same region as this
InterconnectAttachment. The InterconnectAttachment will automatically connect the Interconnect to the network & region
within which the Cloud Router is configured.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>State</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}[Output Only] The current state of this attachment's functionality.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The type of InterconnectAttachment you wish to create. Defaults to DEDICATED.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vlan<wbr>Tag8021q</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The IEEE 802.1Q VLAN tag for this attachment, in the range 2-4094. When using PARTNER type this will be managed
upstream.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>admin<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Whether the VLAN attachment is enabled or disabled. When using PARTNER type this will Pre-Activate the interconnect
attachment
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bandwidth</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Provisioned bandwidth capacity for the interconnect attachment. For attachments of type DEDICATED, the user can set the
bandwidth. For attachments of type PARTNER, the Google Partner that is operating the interconnect must set the
bandwidth. Output only for PARTNER type, mutable for PARTNER_PROVIDER and DEDICATED, Defaults to BPS_10G
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>candidate<wbr>Subnets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}Up to 16 candidate prefixes that can be used to restrict the allocation of cloudRouterIpAddress and
customerRouterIpAddress for this attachment. All prefixes must be within link-local address space (169.254.0.0/16) and
must be /29 or shorter (/28, /27, etc). Google will attempt to select an unused /29 from the supplied candidate
prefix(es). The request will fail if all possible /29s are in use on Google's edge. If not supplied, Google will
randomly select an unused /29 from all of link-local space.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cloud<wbr>Router<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}IPv4 address + prefix length to be configured on Cloud Router Interface for this interconnect attachment.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>creation<wbr>Timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Creation timestamp in RFC3339 text format.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>customer<wbr>Router<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}IPv4 address + prefix length to be configured on the customer router subinterface for this interconnect attachment.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}An optional description of this resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>edge<wbr>Availability<wbr>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Desired availability domain for the attachment. Only available for type PARTNER, at creation time. For improved
reliability, customers should configure a pair of attachments with one per availability domain. The selected
availability domain will be provided to the Partner via the pairing key so that the provisioned circuit will lie in the
specified domain. If not specified, the value will default to AVAILABILITY_DOMAIN_ANY.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>google<wbr>Reference<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Google reference ID, to be used when raising support tickets with Google or otherwise to debug backend connectivity
issues.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>interconnect</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}URL of the underlying Interconnect object that this attachment's traffic will traverse through. Required if type is
DEDICATED, must not be set if type is PARTNER.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and
comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression
'[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pairing<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}[Output only for type PARTNER. Not present for DEDICATED]. The opaque identifier of an PARTNER attachment used to
initiate provisioning with a selected partner. Of the form "XXXXX/region/domain"
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>partner<wbr>Asn</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}[Output only for type PARTNER. Not present for DEDICATED]. Optional BGP ASN for the router that should be supplied by a
layer 3 Partner if they configured BGP on behalf of the customer.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>private<wbr>Interconnect<wbr>Info</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interconnectattachmentprivateinterconnectinfo">Interconnect<wbr>Attachment<wbr>Private<wbr>Interconnect<wbr>Info</a></span>
    </dt>
    <dd>{{% md %}}Information specific to an InterconnectAttachment. This property is populated if the interconnect that this is attached
to is of type DEDICATED.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Region where the regional interconnect attachment resides.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>router</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}URL of the cloud router to be used for dynamic routing. This router must be in the same region as this
InterconnectAttachment. The InterconnectAttachment will automatically connect the Interconnect to the network & region
within which the Cloud Router is configured.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>state</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}[Output Only] The current state of this attachment's functionality.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The type of InterconnectAttachment you wish to create. Defaults to DEDICATED.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vlan<wbr>Tag8021q</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The IEEE 802.1Q VLAN tag for this attachment, in the range 2-4094. When using PARTNER type this will be managed
upstream.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>admin_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether the VLAN attachment is enabled or disabled. When using PARTNER type this will Pre-Activate the interconnect
attachment
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bandwidth</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Provisioned bandwidth capacity for the interconnect attachment. For attachments of type DEDICATED, the user can set the
bandwidth. For attachments of type PARTNER, the Google Partner that is operating the interconnect must set the
bandwidth. Output only for PARTNER type, mutable for PARTNER_PROVIDER and DEDICATED, Defaults to BPS_10G
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>candidate_<wbr>subnets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}Up to 16 candidate prefixes that can be used to restrict the allocation of cloudRouterIpAddress and
customerRouterIpAddress for this attachment. All prefixes must be within link-local address space (169.254.0.0/16) and
must be /29 or shorter (/28, /27, etc). Google will attempt to select an unused /29 from the supplied candidate
prefix(es). The request will fail if all possible /29s are in use on Google's edge. If not supplied, Google will
randomly select an unused /29 from all of link-local space.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cloud_<wbr>router_<wbr>ip_<wbr>address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}IPv4 address + prefix length to be configured on Cloud Router Interface for this interconnect attachment.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>creation_<wbr>timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Creation timestamp in RFC3339 text format.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>customer_<wbr>router_<wbr>ip_<wbr>address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}IPv4 address + prefix length to be configured on the customer router subinterface for this interconnect attachment.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}An optional description of this resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>edge_<wbr>availability_<wbr>domain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Desired availability domain for the attachment. Only available for type PARTNER, at creation time. For improved
reliability, customers should configure a pair of attachments with one per availability domain. The selected
availability domain will be provided to the Partner via the pairing key so that the provisioned circuit will lie in the
specified domain. If not specified, the value will default to AVAILABILITY_DOMAIN_ANY.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>google_<wbr>reference_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Google reference ID, to be used when raising support tickets with Google or otherwise to debug backend connectivity
issues.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>interconnect</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}URL of the underlying Interconnect object that this attachment's traffic will traverse through. Required if type is
DEDICATED, must not be set if type is PARTNER.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and
comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression
'[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pairing_<wbr>key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}[Output only for type PARTNER. Not present for DEDICATED]. The opaque identifier of an PARTNER attachment used to
initiate provisioning with a selected partner. Of the form "XXXXX/region/domain"
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>partner_<wbr>asn</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}[Output only for type PARTNER. Not present for DEDICATED]. Optional BGP ASN for the router that should be supplied by a
layer 3 Partner if they configured BGP on behalf of the customer.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>private_<wbr>interconnect_<wbr>info</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interconnectattachmentprivateinterconnectinfo">Dict[Interconnect<wbr>Attachment<wbr>Private<wbr>Interconnect<wbr>Info]</a></span>
    </dt>
    <dd>{{% md %}}Information specific to an InterconnectAttachment. This property is populated if the interconnect that this is attached
to is of type DEDICATED.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Region where the regional interconnect attachment resides.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>router</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}URL of the cloud router to be used for dynamic routing. This router must be in the same region as this
InterconnectAttachment. The InterconnectAttachment will automatically connect the Interconnect to the network & region
within which the Cloud Router is configured.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>self_<wbr>link</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>state</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}[Output Only] The current state of this attachment's functionality.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The type of InterconnectAttachment you wish to create. Defaults to DEDICATED.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vlan_<wbr>tag8021q</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The IEEE 802.1Q VLAN tag for this attachment, in the range 2-4094. When using PARTNER type this will be managed
upstream.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Interconnect<wbr>Attachment<wbr>Private<wbr>Interconnect<wbr>Info</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#InterconnectAttachmentPrivateInterconnectInfo">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/compute?tab=doc#InterconnectAttachmentPrivateInterconnectInfoOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Tag8021q</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Tag8021q</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>tag8021q</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>tag8021q</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

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

