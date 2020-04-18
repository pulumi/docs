
---
title: "Firewall"
block_external_search_index: true
---



Each network has its own firewall controlling access to and from the
instances.

All traffic to instances, even from other instances, is blocked by the
firewall unless firewall rules are created to allow it.

The default network has automatically created firewall rules that are
shown in default firewall rules. No manually created network has
automatically created firewall rules except for a default "allow" rule for
outgoing traffic and a default "deny" for incoming traffic. For all
networks except the default network, you must create any firewall rules
you need.


To get more information about Firewall, see:

* [API documentation](https://cloud.google.com/compute/docs/reference/v1/firewalls)
* How-to Guides
    * [Official Documentation](https://cloud.google.com/vpc/docs/firewalls)



## Create a Firewall Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/compute/#Firewall">Firewall</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/compute/#FirewallArgs">FirewallArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Firewall</span><span class="p">(resource_name, opts=None, </span>allows=None<span class="p">, </span>denies=None<span class="p">, </span>description=None<span class="p">, </span>destination_ranges=None<span class="p">, </span>direction=None<span class="p">, </span>disabled=None<span class="p">, </span>enable_logging=None<span class="p">, </span>name=None<span class="p">, </span>network=None<span class="p">, </span>priority=None<span class="p">, </span>project=None<span class="p">, </span>source_ranges=None<span class="p">, </span>source_service_accounts=None<span class="p">, </span>source_tags=None<span class="p">, </span>target_service_accounts=None<span class="p">, </span>target_tags=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewFirewall<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/compute?tab=doc#FirewallArgs">FirewallArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/compute?tab=doc#Firewall">Firewall</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Compute.Firewall.html">Firewall</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Compute.FirewallArgs.html">FirewallArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Network</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The name or self_link of the network to attach this firewall to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allows</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewallallow">List&lt;Firewall<wbr>Allow<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}The list of ALLOW rules specified by this firewall. Each rule specifies a protocol and port-range tuple that describes a
permitted connection.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Denies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewalldeny">List&lt;Firewall<wbr>Deny<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}The list of DENY rules specified by this firewall. Each rule specifies a protocol and port-range tuple that describes a
denied connection.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}An optional description of this resource. Provide this property when you create the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Destination<wbr>Ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}If destination ranges are specified, the firewall will apply only to traffic that has destination IP address in these
ranges. These ranges must be expressed in CIDR format. Only IPv4 is supported.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Direction</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Direction of traffic to which this firewall applies; default is INGRESS. Note: For INGRESS traffic, it is NOT supported
to specify destinationRanges; For EGRESS traffic, it is NOT supported to specify sourceRanges OR sourceTags.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Denotes whether the firewall rule is disabled, i.e not applied to the network it is associated with. When set to true,
the firewall rule is not enforced and the network behaves as if it did not exist. If this is unspecified, the firewall
rule will be enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Logging</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}This field denotes whether to enable logging for a particular firewall rule. If logging is enabled, logs will be
exported to Stackdriver.
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
        <span>Priority</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}Priority for this rule. This is an integer between 0 and 65535, both inclusive. When not specified, the value assumed is
1000. Relative priorities determine precedence of conflicting rules. Lower value of priority implies higher precedence
(eg, a rule with priority 0 has higher precedence than a rule with priority 1). DENY rules take precedence over ALLOW
rules having equal priority.
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
        <span>Source<wbr>Ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}If source ranges are specified, the firewall will apply only to traffic that has source IP address in these ranges.
These ranges must be expressed in CIDR format. One or both of sourceRanges and sourceTags may be set. If both properties
are set, the firewall will apply to traffic that has source IP address within sourceRanges OR the source IP that belongs
to a tag listed in the sourceTags property. The connection does not need to match both properties for the firewall to
apply. Only IPv4 is supported.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Service<wbr>Accounts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}If source service accounts are specified, the firewall will apply only to traffic originating from an instance with a
service account in this list. Source service accounts cannot be used to control traffic to an instance's external IP
address because service accounts are associated with an instance, not an IP address. sourceRanges can be set at the same
time as sourceServiceAccounts. If both are set, the firewall will apply to traffic that has source IP address within
sourceRanges OR the source IP belongs to an instance with service account listed in sourceServiceAccount. The connection
does not need to match both properties for the firewall to apply. sourceServiceAccounts cannot be used at the same time
as sourceTags or targetTags.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}If source tags are specified, the firewall will apply only to traffic with source IP that belongs to a tag listed in
source tags. Source tags cannot be used to control traffic to an instance's external IP address. Because tags are
associated with an instance, not an IP address. One or both of sourceRanges and sourceTags may be set. If both
properties are set, the firewall will apply to traffic that has source IP address within sourceRanges OR the source IP
that belongs to a tag listed in the sourceTags property. The connection does not need to match both properties for the
firewall to apply.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>Service<wbr>Accounts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}A list of service accounts indicating sets of instances located in the network that may make network connections as
specified in allowed[]. targetServiceAccounts cannot be used at the same time as targetTags or sourceTags. If neither
targetServiceAccounts nor targetTags are specified, the firewall rule applies to all instances on the specified network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}A list of instance tags indicating sets of instances located in the network that may make network connections as
specified in allowed[]. If no targetTags are specified, the firewall rule applies to all instances on the specified
network.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Network</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The name or self_link of the network to attach this firewall to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allows</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewallallow">[]Firewall<wbr>Allow</a></span>
    </dt>
    <dd>{{% md %}}The list of ALLOW rules specified by this firewall. Each rule specifies a protocol and port-range tuple that describes a
permitted connection.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Denies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewalldeny">[]Firewall<wbr>Deny</a></span>
    </dt>
    <dd>{{% md %}}The list of DENY rules specified by this firewall. Each rule specifies a protocol and port-range tuple that describes a
denied connection.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}An optional description of this resource. Provide this property when you create the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Destination<wbr>Ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}If destination ranges are specified, the firewall will apply only to traffic that has destination IP address in these
ranges. These ranges must be expressed in CIDR format. Only IPv4 is supported.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Direction</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Direction of traffic to which this firewall applies; default is INGRESS. Note: For INGRESS traffic, it is NOT supported
to specify destinationRanges; For EGRESS traffic, it is NOT supported to specify sourceRanges OR sourceTags.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Denotes whether the firewall rule is disabled, i.e not applied to the network it is associated with. When set to true,
the firewall rule is not enforced and the network behaves as if it did not exist. If this is unspecified, the firewall
rule will be enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Logging</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}This field denotes whether to enable logging for a particular firewall rule. If logging is enabled, logs will be
exported to Stackdriver.
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
        <span>Priority</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}Priority for this rule. This is an integer between 0 and 65535, both inclusive. When not specified, the value assumed is
1000. Relative priorities determine precedence of conflicting rules. Lower value of priority implies higher precedence
(eg, a rule with priority 0 has higher precedence than a rule with priority 1). DENY rules take precedence over ALLOW
rules having equal priority.
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
        <span>Source<wbr>Ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}If source ranges are specified, the firewall will apply only to traffic that has source IP address in these ranges.
These ranges must be expressed in CIDR format. One or both of sourceRanges and sourceTags may be set. If both properties
are set, the firewall will apply to traffic that has source IP address within sourceRanges OR the source IP that belongs
to a tag listed in the sourceTags property. The connection does not need to match both properties for the firewall to
apply. Only IPv4 is supported.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Service<wbr>Accounts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}If source service accounts are specified, the firewall will apply only to traffic originating from an instance with a
service account in this list. Source service accounts cannot be used to control traffic to an instance's external IP
address because service accounts are associated with an instance, not an IP address. sourceRanges can be set at the same
time as sourceServiceAccounts. If both are set, the firewall will apply to traffic that has source IP address within
sourceRanges OR the source IP belongs to an instance with service account listed in sourceServiceAccount. The connection
does not need to match both properties for the firewall to apply. sourceServiceAccounts cannot be used at the same time
as sourceTags or targetTags.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}If source tags are specified, the firewall will apply only to traffic with source IP that belongs to a tag listed in
source tags. Source tags cannot be used to control traffic to an instance's external IP address. Because tags are
associated with an instance, not an IP address. One or both of sourceRanges and sourceTags may be set. If both
properties are set, the firewall will apply to traffic that has source IP address within sourceRanges OR the source IP
that belongs to a tag listed in the sourceTags property. The connection does not need to match both properties for the
firewall to apply.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>Service<wbr>Accounts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}A list of service accounts indicating sets of instances located in the network that may make network connections as
specified in allowed[]. targetServiceAccounts cannot be used at the same time as targetTags or sourceTags. If neither
targetServiceAccounts nor targetTags are specified, the firewall rule applies to all instances on the specified network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}A list of instance tags indicating sets of instances located in the network that may make network connections as
specified in allowed[]. If no targetTags are specified, the firewall rule applies to all instances on the specified
network.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>network</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The name or self_link of the network to attach this firewall to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allows</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewallallow">Firewall<wbr>Allow[]</a></span>
    </dt>
    <dd>{{% md %}}The list of ALLOW rules specified by this firewall. Each rule specifies a protocol and port-range tuple that describes a
permitted connection.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>denies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewalldeny">Firewall<wbr>Deny[]</a></span>
    </dt>
    <dd>{{% md %}}The list of DENY rules specified by this firewall. Each rule specifies a protocol and port-range tuple that describes a
denied connection.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}An optional description of this resource. Provide this property when you create the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>destination<wbr>Ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}If destination ranges are specified, the firewall will apply only to traffic that has destination IP address in these
ranges. These ranges must be expressed in CIDR format. Only IPv4 is supported.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>direction</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Direction of traffic to which this firewall applies; default is INGRESS. Note: For INGRESS traffic, it is NOT supported
to specify destinationRanges; For EGRESS traffic, it is NOT supported to specify sourceRanges OR sourceTags.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Denotes whether the firewall rule is disabled, i.e not applied to the network it is associated with. When set to true,
the firewall rule is not enforced and the network behaves as if it did not exist. If this is unspecified, the firewall
rule will be enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Logging</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}This field denotes whether to enable logging for a particular firewall rule. If logging is enabled, logs will be
exported to Stackdriver.
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
        <span>priority</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}Priority for this rule. This is an integer between 0 and 65535, both inclusive. When not specified, the value assumed is
1000. Relative priorities determine precedence of conflicting rules. Lower value of priority implies higher precedence
(eg, a rule with priority 0 has higher precedence than a rule with priority 1). DENY rules take precedence over ALLOW
rules having equal priority.
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
        <span>source<wbr>Ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}If source ranges are specified, the firewall will apply only to traffic that has source IP address in these ranges.
These ranges must be expressed in CIDR format. One or both of sourceRanges and sourceTags may be set. If both properties
are set, the firewall will apply to traffic that has source IP address within sourceRanges OR the source IP that belongs
to a tag listed in the sourceTags property. The connection does not need to match both properties for the firewall to
apply. Only IPv4 is supported.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source<wbr>Service<wbr>Accounts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}If source service accounts are specified, the firewall will apply only to traffic originating from an instance with a
service account in this list. Source service accounts cannot be used to control traffic to an instance's external IP
address because service accounts are associated with an instance, not an IP address. sourceRanges can be set at the same
time as sourceServiceAccounts. If both are set, the firewall will apply to traffic that has source IP address within
sourceRanges OR the source IP belongs to an instance with service account listed in sourceServiceAccount. The connection
does not need to match both properties for the firewall to apply. sourceServiceAccounts cannot be used at the same time
as sourceTags or targetTags.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source<wbr>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}If source tags are specified, the firewall will apply only to traffic with source IP that belongs to a tag listed in
source tags. Source tags cannot be used to control traffic to an instance's external IP address. Because tags are
associated with an instance, not an IP address. One or both of sourceRanges and sourceTags may be set. If both
properties are set, the firewall will apply to traffic that has source IP address within sourceRanges OR the source IP
that belongs to a tag listed in the sourceTags property. The connection does not need to match both properties for the
firewall to apply.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target<wbr>Service<wbr>Accounts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}A list of service accounts indicating sets of instances located in the network that may make network connections as
specified in allowed[]. targetServiceAccounts cannot be used at the same time as targetTags or sourceTags. If neither
targetServiceAccounts nor targetTags are specified, the firewall rule applies to all instances on the specified network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target<wbr>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}A list of instance tags indicating sets of instances located in the network that may make network connections as
specified in allowed[]. If no targetTags are specified, the firewall rule applies to all instances on the specified
network.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>network</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The name or self_link of the network to attach this firewall to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allows</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewallallow">List[Firewall<wbr>Allow]</a></span>
    </dt>
    <dd>{{% md %}}The list of ALLOW rules specified by this firewall. Each rule specifies a protocol and port-range tuple that describes a
permitted connection.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>denies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewalldeny">List[Firewall<wbr>Deny]</a></span>
    </dt>
    <dd>{{% md %}}The list of DENY rules specified by this firewall. Each rule specifies a protocol and port-range tuple that describes a
denied connection.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}An optional description of this resource. Provide this property when you create the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>destination_<wbr>ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}If destination ranges are specified, the firewall will apply only to traffic that has destination IP address in these
ranges. These ranges must be expressed in CIDR format. Only IPv4 is supported.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>direction</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Direction of traffic to which this firewall applies; default is INGRESS. Note: For INGRESS traffic, it is NOT supported
to specify destinationRanges; For EGRESS traffic, it is NOT supported to specify sourceRanges OR sourceTags.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Denotes whether the firewall rule is disabled, i.e not applied to the network it is associated with. When set to true,
the firewall rule is not enforced and the network behaves as if it did not exist. If this is unspecified, the firewall
rule will be enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>logging</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}This field denotes whether to enable logging for a particular firewall rule. If logging is enabled, logs will be
exported to Stackdriver.
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
        <span>priority</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}Priority for this rule. This is an integer between 0 and 65535, both inclusive. When not specified, the value assumed is
1000. Relative priorities determine precedence of conflicting rules. Lower value of priority implies higher precedence
(eg, a rule with priority 0 has higher precedence than a rule with priority 1). DENY rules take precedence over ALLOW
rules having equal priority.
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
        <span>source_<wbr>ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}If source ranges are specified, the firewall will apply only to traffic that has source IP address in these ranges.
These ranges must be expressed in CIDR format. One or both of sourceRanges and sourceTags may be set. If both properties
are set, the firewall will apply to traffic that has source IP address within sourceRanges OR the source IP that belongs
to a tag listed in the sourceTags property. The connection does not need to match both properties for the firewall to
apply. Only IPv4 is supported.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source_<wbr>service_<wbr>accounts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}If source service accounts are specified, the firewall will apply only to traffic originating from an instance with a
service account in this list. Source service accounts cannot be used to control traffic to an instance's external IP
address because service accounts are associated with an instance, not an IP address. sourceRanges can be set at the same
time as sourceServiceAccounts. If both are set, the firewall will apply to traffic that has source IP address within
sourceRanges OR the source IP belongs to an instance with service account listed in sourceServiceAccount. The connection
does not need to match both properties for the firewall to apply. sourceServiceAccounts cannot be used at the same time
as sourceTags or targetTags.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source_<wbr>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}If source tags are specified, the firewall will apply only to traffic with source IP that belongs to a tag listed in
source tags. Source tags cannot be used to control traffic to an instance's external IP address. Because tags are
associated with an instance, not an IP address. One or both of sourceRanges and sourceTags may be set. If both
properties are set, the firewall will apply to traffic that has source IP address within sourceRanges OR the source IP
that belongs to a tag listed in the sourceTags property. The connection does not need to match both properties for the
firewall to apply.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target_<wbr>service_<wbr>accounts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}A list of service accounts indicating sets of instances located in the network that may make network connections as
specified in allowed[]. targetServiceAccounts cannot be used at the same time as targetTags or sourceTags. If neither
targetServiceAccounts nor targetTags are specified, the firewall rule applies to all instances on the specified network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target_<wbr>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}A list of instance tags indicating sets of instances located in the network that may make network connections as
specified in allowed[]. If no targetTags are specified, the firewall rule applies to all instances on the specified
network.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## Firewall Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

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
        <span>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

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
        <span>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

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
        <span>self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

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
        <span>self_<wbr>link</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing Firewall Resource

Get an existing Firewall resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/compute/#FirewallState">FirewallState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/compute/#Firewall">Firewall</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>allows=None<span class="p">, </span>creation_timestamp=None<span class="p">, </span>denies=None<span class="p">, </span>description=None<span class="p">, </span>destination_ranges=None<span class="p">, </span>direction=None<span class="p">, </span>disabled=None<span class="p">, </span>enable_logging=None<span class="p">, </span>name=None<span class="p">, </span>network=None<span class="p">, </span>priority=None<span class="p">, </span>project=None<span class="p">, </span>self_link=None<span class="p">, </span>source_ranges=None<span class="p">, </span>source_service_accounts=None<span class="p">, </span>source_tags=None<span class="p">, </span>target_service_accounts=None<span class="p">, </span>target_tags=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetFirewall<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/compute?tab=doc#FirewallState">FirewallState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/compute?tab=doc#Firewall">Firewall</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Compute.Firewall.html">Firewall</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Compute.FirewallState.html">FirewallState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Allows</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewallallow">List&lt;Firewall<wbr>Allow<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}The list of ALLOW rules specified by this firewall. Each rule specifies a protocol and port-range tuple that describes a
permitted connection.
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
        <span>Denies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewalldeny">List&lt;Firewall<wbr>Deny<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}The list of DENY rules specified by this firewall. Each rule specifies a protocol and port-range tuple that describes a
denied connection.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}An optional description of this resource. Provide this property when you create the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Destination<wbr>Ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}If destination ranges are specified, the firewall will apply only to traffic that has destination IP address in these
ranges. These ranges must be expressed in CIDR format. Only IPv4 is supported.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Direction</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Direction of traffic to which this firewall applies; default is INGRESS. Note: For INGRESS traffic, it is NOT supported
to specify destinationRanges; For EGRESS traffic, it is NOT supported to specify sourceRanges OR sourceTags.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Denotes whether the firewall rule is disabled, i.e not applied to the network it is associated with. When set to true,
the firewall rule is not enforced and the network behaves as if it did not exist. If this is unspecified, the firewall
rule will be enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Logging</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}This field denotes whether to enable logging for a particular firewall rule. If logging is enabled, logs will be
exported to Stackdriver.
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
        <span>Network</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The name or self_link of the network to attach this firewall to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Priority</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}Priority for this rule. This is an integer between 0 and 65535, both inclusive. When not specified, the value assumed is
1000. Relative priorities determine precedence of conflicting rules. Lower value of priority implies higher precedence
(eg, a rule with priority 0 has higher precedence than a rule with priority 1). DENY rules take precedence over ALLOW
rules having equal priority.
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
        <span>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}If source ranges are specified, the firewall will apply only to traffic that has source IP address in these ranges.
These ranges must be expressed in CIDR format. One or both of sourceRanges and sourceTags may be set. If both properties
are set, the firewall will apply to traffic that has source IP address within sourceRanges OR the source IP that belongs
to a tag listed in the sourceTags property. The connection does not need to match both properties for the firewall to
apply. Only IPv4 is supported.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Service<wbr>Accounts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}If source service accounts are specified, the firewall will apply only to traffic originating from an instance with a
service account in this list. Source service accounts cannot be used to control traffic to an instance's external IP
address because service accounts are associated with an instance, not an IP address. sourceRanges can be set at the same
time as sourceServiceAccounts. If both are set, the firewall will apply to traffic that has source IP address within
sourceRanges OR the source IP belongs to an instance with service account listed in sourceServiceAccount. The connection
does not need to match both properties for the firewall to apply. sourceServiceAccounts cannot be used at the same time
as sourceTags or targetTags.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}If source tags are specified, the firewall will apply only to traffic with source IP that belongs to a tag listed in
source tags. Source tags cannot be used to control traffic to an instance's external IP address. Because tags are
associated with an instance, not an IP address. One or both of sourceRanges and sourceTags may be set. If both
properties are set, the firewall will apply to traffic that has source IP address within sourceRanges OR the source IP
that belongs to a tag listed in the sourceTags property. The connection does not need to match both properties for the
firewall to apply.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>Service<wbr>Accounts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}A list of service accounts indicating sets of instances located in the network that may make network connections as
specified in allowed[]. targetServiceAccounts cannot be used at the same time as targetTags or sourceTags. If neither
targetServiceAccounts nor targetTags are specified, the firewall rule applies to all instances on the specified network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}A list of instance tags indicating sets of instances located in the network that may make network connections as
specified in allowed[]. If no targetTags are specified, the firewall rule applies to all instances on the specified
network.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Allows</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewallallow">[]Firewall<wbr>Allow</a></span>
    </dt>
    <dd>{{% md %}}The list of ALLOW rules specified by this firewall. Each rule specifies a protocol and port-range tuple that describes a
permitted connection.
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
        <span>Denies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewalldeny">[]Firewall<wbr>Deny</a></span>
    </dt>
    <dd>{{% md %}}The list of DENY rules specified by this firewall. Each rule specifies a protocol and port-range tuple that describes a
denied connection.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}An optional description of this resource. Provide this property when you create the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Destination<wbr>Ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}If destination ranges are specified, the firewall will apply only to traffic that has destination IP address in these
ranges. These ranges must be expressed in CIDR format. Only IPv4 is supported.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Direction</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Direction of traffic to which this firewall applies; default is INGRESS. Note: For INGRESS traffic, it is NOT supported
to specify destinationRanges; For EGRESS traffic, it is NOT supported to specify sourceRanges OR sourceTags.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Denotes whether the firewall rule is disabled, i.e not applied to the network it is associated with. When set to true,
the firewall rule is not enforced and the network behaves as if it did not exist. If this is unspecified, the firewall
rule will be enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Logging</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}This field denotes whether to enable logging for a particular firewall rule. If logging is enabled, logs will be
exported to Stackdriver.
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
        <span>Network</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The name or self_link of the network to attach this firewall to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Priority</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}Priority for this rule. This is an integer between 0 and 65535, both inclusive. When not specified, the value assumed is
1000. Relative priorities determine precedence of conflicting rules. Lower value of priority implies higher precedence
(eg, a rule with priority 0 has higher precedence than a rule with priority 1). DENY rules take precedence over ALLOW
rules having equal priority.
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
        <span>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}If source ranges are specified, the firewall will apply only to traffic that has source IP address in these ranges.
These ranges must be expressed in CIDR format. One or both of sourceRanges and sourceTags may be set. If both properties
are set, the firewall will apply to traffic that has source IP address within sourceRanges OR the source IP that belongs
to a tag listed in the sourceTags property. The connection does not need to match both properties for the firewall to
apply. Only IPv4 is supported.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Service<wbr>Accounts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}If source service accounts are specified, the firewall will apply only to traffic originating from an instance with a
service account in this list. Source service accounts cannot be used to control traffic to an instance's external IP
address because service accounts are associated with an instance, not an IP address. sourceRanges can be set at the same
time as sourceServiceAccounts. If both are set, the firewall will apply to traffic that has source IP address within
sourceRanges OR the source IP belongs to an instance with service account listed in sourceServiceAccount. The connection
does not need to match both properties for the firewall to apply. sourceServiceAccounts cannot be used at the same time
as sourceTags or targetTags.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}If source tags are specified, the firewall will apply only to traffic with source IP that belongs to a tag listed in
source tags. Source tags cannot be used to control traffic to an instance's external IP address. Because tags are
associated with an instance, not an IP address. One or both of sourceRanges and sourceTags may be set. If both
properties are set, the firewall will apply to traffic that has source IP address within sourceRanges OR the source IP
that belongs to a tag listed in the sourceTags property. The connection does not need to match both properties for the
firewall to apply.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>Service<wbr>Accounts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}A list of service accounts indicating sets of instances located in the network that may make network connections as
specified in allowed[]. targetServiceAccounts cannot be used at the same time as targetTags or sourceTags. If neither
targetServiceAccounts nor targetTags are specified, the firewall rule applies to all instances on the specified network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}A list of instance tags indicating sets of instances located in the network that may make network connections as
specified in allowed[]. If no targetTags are specified, the firewall rule applies to all instances on the specified
network.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>allows</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewallallow">Firewall<wbr>Allow[]</a></span>
    </dt>
    <dd>{{% md %}}The list of ALLOW rules specified by this firewall. Each rule specifies a protocol and port-range tuple that describes a
permitted connection.
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
        <span>denies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewalldeny">Firewall<wbr>Deny[]</a></span>
    </dt>
    <dd>{{% md %}}The list of DENY rules specified by this firewall. Each rule specifies a protocol and port-range tuple that describes a
denied connection.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}An optional description of this resource. Provide this property when you create the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>destination<wbr>Ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}If destination ranges are specified, the firewall will apply only to traffic that has destination IP address in these
ranges. These ranges must be expressed in CIDR format. Only IPv4 is supported.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>direction</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Direction of traffic to which this firewall applies; default is INGRESS. Note: For INGRESS traffic, it is NOT supported
to specify destinationRanges; For EGRESS traffic, it is NOT supported to specify sourceRanges OR sourceTags.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Denotes whether the firewall rule is disabled, i.e not applied to the network it is associated with. When set to true,
the firewall rule is not enforced and the network behaves as if it did not exist. If this is unspecified, the firewall
rule will be enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Logging</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}This field denotes whether to enable logging for a particular firewall rule. If logging is enabled, logs will be
exported to Stackdriver.
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
        <span>network</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The name or self_link of the network to attach this firewall to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>priority</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}Priority for this rule. This is an integer between 0 and 65535, both inclusive. When not specified, the value assumed is
1000. Relative priorities determine precedence of conflicting rules. Lower value of priority implies higher precedence
(eg, a rule with priority 0 has higher precedence than a rule with priority 1). DENY rules take precedence over ALLOW
rules having equal priority.
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
        <span>self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source<wbr>Ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}If source ranges are specified, the firewall will apply only to traffic that has source IP address in these ranges.
These ranges must be expressed in CIDR format. One or both of sourceRanges and sourceTags may be set. If both properties
are set, the firewall will apply to traffic that has source IP address within sourceRanges OR the source IP that belongs
to a tag listed in the sourceTags property. The connection does not need to match both properties for the firewall to
apply. Only IPv4 is supported.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source<wbr>Service<wbr>Accounts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}If source service accounts are specified, the firewall will apply only to traffic originating from an instance with a
service account in this list. Source service accounts cannot be used to control traffic to an instance's external IP
address because service accounts are associated with an instance, not an IP address. sourceRanges can be set at the same
time as sourceServiceAccounts. If both are set, the firewall will apply to traffic that has source IP address within
sourceRanges OR the source IP belongs to an instance with service account listed in sourceServiceAccount. The connection
does not need to match both properties for the firewall to apply. sourceServiceAccounts cannot be used at the same time
as sourceTags or targetTags.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source<wbr>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}If source tags are specified, the firewall will apply only to traffic with source IP that belongs to a tag listed in
source tags. Source tags cannot be used to control traffic to an instance's external IP address. Because tags are
associated with an instance, not an IP address. One or both of sourceRanges and sourceTags may be set. If both
properties are set, the firewall will apply to traffic that has source IP address within sourceRanges OR the source IP
that belongs to a tag listed in the sourceTags property. The connection does not need to match both properties for the
firewall to apply.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target<wbr>Service<wbr>Accounts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}A list of service accounts indicating sets of instances located in the network that may make network connections as
specified in allowed[]. targetServiceAccounts cannot be used at the same time as targetTags or sourceTags. If neither
targetServiceAccounts nor targetTags are specified, the firewall rule applies to all instances on the specified network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target<wbr>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}A list of instance tags indicating sets of instances located in the network that may make network connections as
specified in allowed[]. If no targetTags are specified, the firewall rule applies to all instances on the specified
network.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>allows</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewallallow">List[Firewall<wbr>Allow]</a></span>
    </dt>
    <dd>{{% md %}}The list of ALLOW rules specified by this firewall. Each rule specifies a protocol and port-range tuple that describes a
permitted connection.
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
        <span>denies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewalldeny">List[Firewall<wbr>Deny]</a></span>
    </dt>
    <dd>{{% md %}}The list of DENY rules specified by this firewall. Each rule specifies a protocol and port-range tuple that describes a
denied connection.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}An optional description of this resource. Provide this property when you create the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>destination_<wbr>ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}If destination ranges are specified, the firewall will apply only to traffic that has destination IP address in these
ranges. These ranges must be expressed in CIDR format. Only IPv4 is supported.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>direction</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Direction of traffic to which this firewall applies; default is INGRESS. Note: For INGRESS traffic, it is NOT supported
to specify destinationRanges; For EGRESS traffic, it is NOT supported to specify sourceRanges OR sourceTags.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Denotes whether the firewall rule is disabled, i.e not applied to the network it is associated with. When set to true,
the firewall rule is not enforced and the network behaves as if it did not exist. If this is unspecified, the firewall
rule will be enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>logging</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}This field denotes whether to enable logging for a particular firewall rule. If logging is enabled, logs will be
exported to Stackdriver.
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
        <span>network</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The name or self_link of the network to attach this firewall to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>priority</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}Priority for this rule. This is an integer between 0 and 65535, both inclusive. When not specified, the value assumed is
1000. Relative priorities determine precedence of conflicting rules. Lower value of priority implies higher precedence
(eg, a rule with priority 0 has higher precedence than a rule with priority 1). DENY rules take precedence over ALLOW
rules having equal priority.
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
        <span>self_<wbr>link</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source_<wbr>ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}If source ranges are specified, the firewall will apply only to traffic that has source IP address in these ranges.
These ranges must be expressed in CIDR format. One or both of sourceRanges and sourceTags may be set. If both properties
are set, the firewall will apply to traffic that has source IP address within sourceRanges OR the source IP that belongs
to a tag listed in the sourceTags property. The connection does not need to match both properties for the firewall to
apply. Only IPv4 is supported.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source_<wbr>service_<wbr>accounts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}If source service accounts are specified, the firewall will apply only to traffic originating from an instance with a
service account in this list. Source service accounts cannot be used to control traffic to an instance's external IP
address because service accounts are associated with an instance, not an IP address. sourceRanges can be set at the same
time as sourceServiceAccounts. If both are set, the firewall will apply to traffic that has source IP address within
sourceRanges OR the source IP belongs to an instance with service account listed in sourceServiceAccount. The connection
does not need to match both properties for the firewall to apply. sourceServiceAccounts cannot be used at the same time
as sourceTags or targetTags.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source_<wbr>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}If source tags are specified, the firewall will apply only to traffic with source IP that belongs to a tag listed in
source tags. Source tags cannot be used to control traffic to an instance's external IP address. Because tags are
associated with an instance, not an IP address. One or both of sourceRanges and sourceTags may be set. If both
properties are set, the firewall will apply to traffic that has source IP address within sourceRanges OR the source IP
that belongs to a tag listed in the sourceTags property. The connection does not need to match both properties for the
firewall to apply.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target_<wbr>service_<wbr>accounts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}A list of service accounts indicating sets of instances located in the network that may make network connections as
specified in allowed[]. targetServiceAccounts cannot be used at the same time as targetTags or sourceTags. If neither
targetServiceAccounts nor targetTags are specified, the firewall rule applies to all instances on the specified network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target_<wbr>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}A list of instance tags indicating sets of instances located in the network that may make network connections as
specified in allowed[]. If no targetTags are specified, the firewall rule applies to all instances on the specified
network.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Firewall<wbr>Allow</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#FirewallAllow">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#FirewallAllow">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/compute?tab=doc#FirewallAllowArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/compute?tab=doc#FirewallAllowOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ports</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ports</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ports</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ports</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Firewall<wbr>Deny</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#FirewallDeny">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#FirewallDeny">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/compute?tab=doc#FirewallDenyArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/compute?tab=doc#FirewallDenyOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ports</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ports</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ports</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ports</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
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

