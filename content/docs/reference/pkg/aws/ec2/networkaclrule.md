
---
title: "NetworkAclRule"
block_external_search_index: true
---

Creates an entry (a rule) in a network ACL with the specified rule number.

> **NOTE on Network ACLs and Network ACL Rules:** This provider currently
provides both a standalone Network ACL Rule resource and a Network ACL resource with rules
defined in-line. At this time you cannot use a Network ACL with in-line rules
in conjunction with any Network ACL Rule resources. Doing so will cause
a conflict of rule settings and will overwrite rules.

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/network_acl_rule.html.markdown.



## Create a NetworkAclRule Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ec2/#NetworkAclRule">NetworkAclRule</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ec2/#NetworkAclRuleArgs">NetworkAclRuleArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">NetworkAclRule</span><span class="p">(resource_name, opts=None, </span>cidr_block=None<span class="p">, </span>egress=None<span class="p">, </span>from_port=None<span class="p">, </span>icmp_code=None<span class="p">, </span>icmp_type=None<span class="p">, </span>ipv6_cidr_block=None<span class="p">, </span>network_acl_id=None<span class="p">, </span>protocol=None<span class="p">, </span>rule_action=None<span class="p">, </span>rule_number=None<span class="p">, </span>to_port=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewNetworkAclRule<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#NetworkAclRuleArgs">NetworkAclRuleArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#NetworkAclRule">NetworkAclRule</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.NetworkAclRule.html">NetworkAclRule</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.NetworkAclRuleArgs.html">NetworkAclRuleArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Cidr<wbr>Block</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The network range to allow or deny, in CIDR notation (for example 172.16.0.0/24 ).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Egress</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Indicates whether this is an egress rule (rule is applied to traffic leaving the subnet). Default `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>From<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The from port to match.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Icmp<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}ICMP protocol: The ICMP code. Required if specifying ICMP for the protocol. e.g. -1
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Icmp<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}ICMP protocol: The ICMP type. Required if specifying ICMP for the protocol. e.g. -1
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ipv6Cidr<wbr>Block</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The IPv6 CIDR block to allow or deny.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Network<wbr>Acl<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the network ACL.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The protocol. A value of -1 means all protocols.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Rule<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Indicates whether to allow or deny the traffic that matches the rule. Accepted values: `allow` | `deny`
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Rule<wbr>Number</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The rule number for the entry (for example, 100). ACL entries are processed in ascending order by rule number.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>To<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The to port to match.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Cidr<wbr>Block</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The network range to allow or deny, in CIDR notation (for example 172.16.0.0/24 ).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Egress</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Indicates whether this is an egress rule (rule is applied to traffic leaving the subnet). Default `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>From<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The from port to match.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Icmp<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}ICMP protocol: The ICMP code. Required if specifying ICMP for the protocol. e.g. -1
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Icmp<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}ICMP protocol: The ICMP type. Required if specifying ICMP for the protocol. e.g. -1
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ipv6Cidr<wbr>Block</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The IPv6 CIDR block to allow or deny.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Network<wbr>Acl<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the network ACL.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The protocol. A value of -1 means all protocols.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Rule<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Indicates whether to allow or deny the traffic that matches the rule. Accepted values: `allow` | `deny`
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Rule<wbr>Number</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The rule number for the entry (for example, 100). ACL entries are processed in ascending order by rule number.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>To<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The to port to match.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>cidr<wbr>Block</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The network range to allow or deny, in CIDR notation (for example 172.16.0.0/24 ).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>egress</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Indicates whether this is an egress rule (rule is applied to traffic leaving the subnet). Default `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>from<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The from port to match.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>icmp<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}ICMP protocol: The ICMP code. Required if specifying ICMP for the protocol. e.g. -1
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>icmp<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}ICMP protocol: The ICMP type. Required if specifying ICMP for the protocol. e.g. -1
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ipv6Cidr<wbr>Block</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The IPv6 CIDR block to allow or deny.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>network<wbr>Acl<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the network ACL.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The protocol. A value of -1 means all protocols.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>rule<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Indicates whether to allow or deny the traffic that matches the rule. Accepted values: `allow` | `deny`
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>rule<wbr>Number</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The rule number for the entry (for example, 100). ACL entries are processed in ascending order by rule number.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>to<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The to port to match.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>cidr_<wbr>block</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The network range to allow or deny, in CIDR notation (for example 172.16.0.0/24 ).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>egress</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Indicates whether this is an egress rule (rule is applied to traffic leaving the subnet). Default `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>from_<wbr>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The from port to match.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>icmp_<wbr>code</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}ICMP protocol: The ICMP code. Required if specifying ICMP for the protocol. e.g. -1
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>icmp_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}ICMP protocol: The ICMP type. Required if specifying ICMP for the protocol. e.g. -1
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ipv6_<wbr>cidr_<wbr>block</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The IPv6 CIDR block to allow or deny.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>network_<wbr>acl_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the network ACL.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The protocol. A value of -1 means all protocols.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>rule_<wbr>action</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Indicates whether to allow or deny the traffic that matches the rule. Accepted values: `allow` | `deny`
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>rule_<wbr>number</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The rule number for the entry (for example, 100). ACL entries are processed in ascending order by rule number.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>to_<wbr>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The to port to match.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## NetworkAclRule Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Cidr<wbr>Block</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The network range to allow or deny, in CIDR notation (for example 172.16.0.0/24 ).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Egress</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Indicates whether this is an egress rule (rule is applied to traffic leaving the subnet). Default `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>From<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The from port to match.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Icmp<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}ICMP protocol: The ICMP code. Required if specifying ICMP for the protocol. e.g. -1
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Icmp<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}ICMP protocol: The ICMP type. Required if specifying ICMP for the protocol. e.g. -1
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ipv6Cidr<wbr>Block</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The IPv6 CIDR block to allow or deny.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Network<wbr>Acl<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the network ACL.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The protocol. A value of -1 means all protocols.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Rule<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Indicates whether to allow or deny the traffic that matches the rule. Accepted values: `allow` | `deny`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Rule<wbr>Number</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The rule number for the entry (for example, 100). ACL entries are processed in ascending order by rule number.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>To<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The to port to match.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Cidr<wbr>Block</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The network range to allow or deny, in CIDR notation (for example 172.16.0.0/24 ).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Egress</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Indicates whether this is an egress rule (rule is applied to traffic leaving the subnet). Default `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>From<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The from port to match.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Icmp<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}ICMP protocol: The ICMP code. Required if specifying ICMP for the protocol. e.g. -1
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Icmp<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}ICMP protocol: The ICMP type. Required if specifying ICMP for the protocol. e.g. -1
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ipv6Cidr<wbr>Block</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The IPv6 CIDR block to allow or deny.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Network<wbr>Acl<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the network ACL.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The protocol. A value of -1 means all protocols.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Rule<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Indicates whether to allow or deny the traffic that matches the rule. Accepted values: `allow` | `deny`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Rule<wbr>Number</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The rule number for the entry (for example, 100). ACL entries are processed in ascending order by rule number.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>To<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The to port to match.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>cidr<wbr>Block</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The network range to allow or deny, in CIDR notation (for example 172.16.0.0/24 ).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>egress</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Indicates whether this is an egress rule (rule is applied to traffic leaving the subnet). Default `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>from<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The from port to match.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>icmp<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}ICMP protocol: The ICMP code. Required if specifying ICMP for the protocol. e.g. -1
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>icmp<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}ICMP protocol: The ICMP type. Required if specifying ICMP for the protocol. e.g. -1
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ipv6Cidr<wbr>Block</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The IPv6 CIDR block to allow or deny.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>network<wbr>Acl<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the network ACL.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The protocol. A value of -1 means all protocols.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>rule<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Indicates whether to allow or deny the traffic that matches the rule. Accepted values: `allow` | `deny`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>rule<wbr>Number</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The rule number for the entry (for example, 100). ACL entries are processed in ascending order by rule number.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>to<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The to port to match.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>cidr_<wbr>block</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The network range to allow or deny, in CIDR notation (for example 172.16.0.0/24 ).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>egress</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Indicates whether this is an egress rule (rule is applied to traffic leaving the subnet). Default `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>from_<wbr>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The from port to match.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>icmp_<wbr>code</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}ICMP protocol: The ICMP code. Required if specifying ICMP for the protocol. e.g. -1
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>icmp_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}ICMP protocol: The ICMP type. Required if specifying ICMP for the protocol. e.g. -1
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ipv6_<wbr>cidr_<wbr>block</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The IPv6 CIDR block to allow or deny.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>network_<wbr>acl_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the network ACL.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The protocol. A value of -1 means all protocols.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>rule_<wbr>action</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Indicates whether to allow or deny the traffic that matches the rule. Accepted values: `allow` | `deny`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>rule_<wbr>number</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The rule number for the entry (for example, 100). ACL entries are processed in ascending order by rule number.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>to_<wbr>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The to port to match.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing NetworkAclRule Resource

Get an existing NetworkAclRule resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ec2/#NetworkAclRuleState">NetworkAclRuleState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ec2/#NetworkAclRule">NetworkAclRule</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>cidr_block=None<span class="p">, </span>egress=None<span class="p">, </span>from_port=None<span class="p">, </span>icmp_code=None<span class="p">, </span>icmp_type=None<span class="p">, </span>ipv6_cidr_block=None<span class="p">, </span>network_acl_id=None<span class="p">, </span>protocol=None<span class="p">, </span>rule_action=None<span class="p">, </span>rule_number=None<span class="p">, </span>to_port=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetNetworkAclRule<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#NetworkAclRuleState">NetworkAclRuleState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#NetworkAclRule">NetworkAclRule</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.NetworkAclRule.html">NetworkAclRule</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.NetworkAclRuleState.html">NetworkAclRuleState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Cidr<wbr>Block</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The network range to allow or deny, in CIDR notation (for example 172.16.0.0/24 ).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Egress</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Indicates whether this is an egress rule (rule is applied to traffic leaving the subnet). Default `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>From<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The from port to match.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Icmp<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}ICMP protocol: The ICMP code. Required if specifying ICMP for the protocol. e.g. -1
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Icmp<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}ICMP protocol: The ICMP type. Required if specifying ICMP for the protocol. e.g. -1
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ipv6Cidr<wbr>Block</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The IPv6 CIDR block to allow or deny.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network<wbr>Acl<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the network ACL.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The protocol. A value of -1 means all protocols.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Rule<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Indicates whether to allow or deny the traffic that matches the rule. Accepted values: `allow` | `deny`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Rule<wbr>Number</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The rule number for the entry (for example, 100). ACL entries are processed in ascending order by rule number.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>To<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The to port to match.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Cidr<wbr>Block</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The network range to allow or deny, in CIDR notation (for example 172.16.0.0/24 ).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Egress</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Indicates whether this is an egress rule (rule is applied to traffic leaving the subnet). Default `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>From<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The from port to match.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Icmp<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}ICMP protocol: The ICMP code. Required if specifying ICMP for the protocol. e.g. -1
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Icmp<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}ICMP protocol: The ICMP type. Required if specifying ICMP for the protocol. e.g. -1
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ipv6Cidr<wbr>Block</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The IPv6 CIDR block to allow or deny.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network<wbr>Acl<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the network ACL.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The protocol. A value of -1 means all protocols.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Rule<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Indicates whether to allow or deny the traffic that matches the rule. Accepted values: `allow` | `deny`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Rule<wbr>Number</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The rule number for the entry (for example, 100). ACL entries are processed in ascending order by rule number.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>To<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The to port to match.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>cidr<wbr>Block</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The network range to allow or deny, in CIDR notation (for example 172.16.0.0/24 ).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>egress</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Indicates whether this is an egress rule (rule is applied to traffic leaving the subnet). Default `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>from<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The from port to match.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>icmp<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}ICMP protocol: The ICMP code. Required if specifying ICMP for the protocol. e.g. -1
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>icmp<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}ICMP protocol: The ICMP type. Required if specifying ICMP for the protocol. e.g. -1
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ipv6Cidr<wbr>Block</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The IPv6 CIDR block to allow or deny.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network<wbr>Acl<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the network ACL.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The protocol. A value of -1 means all protocols.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>rule<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Indicates whether to allow or deny the traffic that matches the rule. Accepted values: `allow` | `deny`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>rule<wbr>Number</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The rule number for the entry (for example, 100). ACL entries are processed in ascending order by rule number.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>to<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The to port to match.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>cidr_<wbr>block</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The network range to allow or deny, in CIDR notation (for example 172.16.0.0/24 ).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>egress</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Indicates whether this is an egress rule (rule is applied to traffic leaving the subnet). Default `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>from_<wbr>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The from port to match.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>icmp_<wbr>code</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}ICMP protocol: The ICMP code. Required if specifying ICMP for the protocol. e.g. -1
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>icmp_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}ICMP protocol: The ICMP type. Required if specifying ICMP for the protocol. e.g. -1
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ipv6_<wbr>cidr_<wbr>block</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The IPv6 CIDR block to allow or deny.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network_<wbr>acl_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the network ACL.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The protocol. A value of -1 means all protocols.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>rule_<wbr>action</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Indicates whether to allow or deny the traffic that matches the rule. Accepted values: `allow` | `deny`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>rule_<wbr>number</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The rule number for the entry (for example, 100). ACL entries are processed in ascending order by rule number.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>to_<wbr>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The to port to match.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-aws">https://github.com/pulumi/pulumi-aws</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd></dl>
