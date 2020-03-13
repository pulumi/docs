
---
title: "NetworkAclRule"
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>


Creates an entry (a rule) in a network ACL with the specified rule number.

> **NOTE on Network ACLs and Network ACL Rules:** This provider currently
provides both a standalone Network ACL Rule resource and a Network ACL resource with rules
defined in-line. At this time you cannot use a Network ACL with in-line rules
in conjunction with any Network ACL Rule resources. Doing so will cause
a conflict of rule settings and will overwrite rules.

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/network_acl_rule.html.markdown.



## Create a NetworkAclRule Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ec2/#NetworkAclRule">NetworkAclRule</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ec2/#NetworkAclRuleArgs">NetworkAclRuleArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">NetworkAclRule</span><span class="p">(resource_name, id, opts=None, </span>cidr_block=None<span class="p">, </span>egress=None<span class="p">, </span>from_port=None<span class="p">, </span>icmp_code=None<span class="p">, </span>icmp_type=None<span class="p">, </span>ipv6_cidr_block=None<span class="p">, </span>network_acl_id=None<span class="p">, </span>protocol=None<span class="p">, </span>rule_action=None<span class="p">, </span>rule_number=None<span class="p">, </span>to_port=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewNetworkAclRule<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#NetworkAclRuleArgs">NetworkAclRuleArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#NetworkAclRule">NetworkAclRule</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.NetworkAclRule.html">NetworkAclRule</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.NetworkAclRuleArgs.html">NetworkAclRuleArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a NetworkAclRule resource with the given unique name, arguments, and options.

{{% lang nodejs %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>args</strong> &ndash;  (Optional)  The arguments to use to populate this resource's properties.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

{{% lang go %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>args</strong> &ndash;  (Optional)  The arguments to use to populate this resource's properties.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

{{% lang csharp %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>args</strong> &ndash;  (Optional)  The arguments to use to populate this resource's properties.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

The following arguments are supported:


{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Cidr<wbr>Block</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The network range to allow or deny, in CIDR notation (for example 172.16.0.0/24 ).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Egress</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether this is an egress rule (rule is applied to traffic leaving the subnet). Default `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">From<wbr>Port</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The from port to match.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Icmp<wbr>Code</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
ICMP protocol: The ICMP code. Required if specifying ICMP for the protocol. e.g. -1
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Icmp<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
ICMP protocol: The ICMP type. Required if specifying ICMP for the protocol. e.g. -1
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ipv6Cidr<wbr>Block</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The IPv6 CIDR block to allow or deny.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Network<wbr>Acl<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the network ACL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Protocol</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The protocol. A value of -1 means all protocols.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rule<wbr>Action</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Indicates whether to allow or deny the traffic that matches the rule. Accepted values: `allow` | `deny`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rule<wbr>Number</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The rule number for the entry (for example, 100). ACL entries are processed in ascending order by rule number.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">To<wbr>Port</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The to port to match.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Cidr<wbr>Block</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The network range to allow or deny, in CIDR notation (for example 172.16.0.0/24 ).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Egress</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether this is an egress rule (rule is applied to traffic leaving the subnet). Default `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">From<wbr>Port</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The from port to match.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Icmp<wbr>Code</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
ICMP protocol: The ICMP code. Required if specifying ICMP for the protocol. e.g. -1
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Icmp<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
ICMP protocol: The ICMP type. Required if specifying ICMP for the protocol. e.g. -1
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ipv6Cidr<wbr>Block</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The IPv6 CIDR block to allow or deny.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Network<wbr>Acl<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the network ACL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Protocol</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The protocol. A value of -1 means all protocols.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rule<wbr>Action</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Indicates whether to allow or deny the traffic that matches the rule. Accepted values: `allow` | `deny`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rule<wbr>Number</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The rule number for the entry (for example, 100). ACL entries are processed in ascending order by rule number.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">To<wbr>Port</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The to port to match.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">cidr<wbr>Block</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The network range to allow or deny, in CIDR notation (for example 172.16.0.0/24 ).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">egress</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether this is an egress rule (rule is applied to traffic leaving the subnet). Default `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">from<wbr>Port</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The from port to match.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">icmp<wbr>Code</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
ICMP protocol: The ICMP code. Required if specifying ICMP for the protocol. e.g. -1
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">icmp<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
ICMP protocol: The ICMP type. Required if specifying ICMP for the protocol. e.g. -1
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ipv6Cidr<wbr>Block</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The IPv6 CIDR block to allow or deny.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">network<wbr>Acl<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the network ACL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">protocol</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The protocol. A value of -1 means all protocols.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rule<wbr>Action</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Indicates whether to allow or deny the traffic that matches the rule. Accepted values: `allow` | `deny`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rule<wbr>Number</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The rule number for the entry (for example, 100). ACL entries are processed in ascending order by rule number.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">to<wbr>Port</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The to port to match.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">cidr_<wbr>block</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The network range to allow or deny, in CIDR notation (for example 172.16.0.0/24 ).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">egress</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether this is an egress rule (rule is applied to traffic leaving the subnet). Default `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">from_<wbr>port</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The from port to match.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">icmp_<wbr>code</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
ICMP protocol: The ICMP code. Required if specifying ICMP for the protocol. e.g. -1
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">icmp_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
ICMP protocol: The ICMP type. Required if specifying ICMP for the protocol. e.g. -1
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ipv6_<wbr>cidr_<wbr>block</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The IPv6 CIDR block to allow or deny.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">network_<wbr>acl_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the network ACL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">protocol</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The protocol. A value of -1 means all protocols.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rule_<wbr>action</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Indicates whether to allow or deny the traffic that matches the rule. Accepted values: `allow` | `deny`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rule_<wbr>number</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The rule number for the entry (for example, 100). ACL entries are processed in ascending order by rule number.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">to_<wbr>port</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The to port to match.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## NetworkAclRule Output Properties

The following output properties are available:



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Cidr<wbr>Block</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The network range to allow or deny, in CIDR notation (for example 172.16.0.0/24 ).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Egress</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} Indicates whether this is an egress rule (rule is applied to traffic leaving the subnet). Default `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">From<wbr>Port</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} The from port to match.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Icmp<wbr>Code</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} ICMP protocol: The ICMP code. Required if specifying ICMP for the protocol. e.g. -1
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Icmp<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} ICMP protocol: The ICMP type. Required if specifying ICMP for the protocol. e.g. -1
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ipv6Cidr<wbr>Block</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The IPv6 CIDR block to allow or deny.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Network<wbr>Acl<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the network ACL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Protocol</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The protocol. A value of -1 means all protocols.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rule<wbr>Action</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Indicates whether to allow or deny the traffic that matches the rule. Accepted values: `allow` | `deny`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rule<wbr>Number</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The rule number for the entry (for example, 100). ACL entries are processed in ascending order by rule number.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">To<wbr>Port</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} The to port to match.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Cidr<wbr>Block</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The network range to allow or deny, in CIDR notation (for example 172.16.0.0/24 ).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Egress</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} Indicates whether this is an egress rule (rule is applied to traffic leaving the subnet). Default `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">From<wbr>Port</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} The from port to match.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Icmp<wbr>Code</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} ICMP protocol: The ICMP code. Required if specifying ICMP for the protocol. e.g. -1
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Icmp<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} ICMP protocol: The ICMP type. Required if specifying ICMP for the protocol. e.g. -1
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ipv6Cidr<wbr>Block</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The IPv6 CIDR block to allow or deny.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Network<wbr>Acl<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the network ACL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Protocol</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The protocol. A value of -1 means all protocols.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rule<wbr>Action</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Indicates whether to allow or deny the traffic that matches the rule. Accepted values: `allow` | `deny`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rule<wbr>Number</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The rule number for the entry (for example, 100). ACL entries are processed in ascending order by rule number.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">To<wbr>Port</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} The to port to match.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">cidr<wbr>Block</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The network range to allow or deny, in CIDR notation (for example 172.16.0.0/24 ).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">egress</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} Indicates whether this is an egress rule (rule is applied to traffic leaving the subnet). Default `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">from<wbr>Port</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} The from port to match.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">icmp<wbr>Code</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} ICMP protocol: The ICMP code. Required if specifying ICMP for the protocol. e.g. -1
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">icmp<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} ICMP protocol: The ICMP type. Required if specifying ICMP for the protocol. e.g. -1
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ipv6Cidr<wbr>Block</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The IPv6 CIDR block to allow or deny.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">network<wbr>Acl<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the network ACL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">protocol</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The protocol. A value of -1 means all protocols.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rule<wbr>Action</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Indicates whether to allow or deny the traffic that matches the rule. Accepted values: `allow` | `deny`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rule<wbr>Number</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} The rule number for the entry (for example, 100). ACL entries are processed in ascending order by rule number.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">to<wbr>Port</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} The to port to match.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">cidr_<wbr>block</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The network range to allow or deny, in CIDR notation (for example 172.16.0.0/24 ).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">egress</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Indicates whether this is an egress rule (rule is applied to traffic leaving the subnet). Default `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">from_<wbr>port</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The from port to match.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">icmp_<wbr>code</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} ICMP protocol: The ICMP code. Required if specifying ICMP for the protocol. e.g. -1
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">icmp_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} ICMP protocol: The ICMP type. Required if specifying ICMP for the protocol. e.g. -1
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ipv6_<wbr>cidr_<wbr>block</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The IPv6 CIDR block to allow or deny.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">network_<wbr>acl_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the network ACL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">protocol</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The protocol. A value of -1 means all protocols.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rule_<wbr>action</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Indicates whether to allow or deny the traffic that matches the rule. Accepted values: `allow` | `deny`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rule_<wbr>number</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The rule number for the entry (for example, 100). ACL entries are processed in ascending order by rule number.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">to_<wbr>port</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The to port to match.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing NetworkAclRule Resource

{{< langchoose csharp nojavascript >}}

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: NetworkAclRuleState, opts?: pulumi.CustomResourceOptions): NetworkAclRule;
```

```python
def get(resource_name, id, opts=None, cidr_<wbr>block=None, egress=None, from_<wbr>port=None, icmp_<wbr>code=None, icmp_<wbr>type=None, ipv6_<wbr>cidr_<wbr>block=None, network_<wbr>acl_<wbr>id=None, protocol=None, rule_<wbr>action=None, rule_<wbr>number=None, to_<wbr>port=None)
```

```go
func GetNetworkAclRule(ctx *pulumi.Context, name string, id pulumi.IDInput, state *NetworkAclRuleState, opts ...pulumi.ResourceOption) (*Bucket, error)
```

```csharp
public static NetworkAclRule Get(string name, Input<string> id, NetworkAclRuleState? state = null, CustomResourceOptions? options = null);
```

Get an existing NetworkAclRule resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{% lang nodejs %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>id</strong> &ndash; (Required) The _unique_ provider ID of the resource to lookup.</li>
    <li><strong>state</strong> &ndash; (Optional) Any extra arguments used during the lookup.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

{{% lang go %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>id</strong> &ndash; (Required) The _unique_ provider ID of the resource to lookup.</li>
    <li><strong>state</strong> &ndash; (Optional) Any extra arguments used during the lookup.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

{{% lang csharp %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>id</strong> &ndash; (Required) The _unique_ provider ID of the resource to lookup.</li>
    <li><strong>state</strong> &ndash; (Optional) Any extra arguments used during the lookup.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

The following state arguments are supported:


{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Cidr<wbr>Block</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The network range to allow or deny, in CIDR notation (for example 172.16.0.0/24 ).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Egress</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether this is an egress rule (rule is applied to traffic leaving the subnet). Default `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">From<wbr>Port</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The from port to match.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Icmp<wbr>Code</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
ICMP protocol: The ICMP code. Required if specifying ICMP for the protocol. e.g. -1
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Icmp<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
ICMP protocol: The ICMP type. Required if specifying ICMP for the protocol. e.g. -1
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ipv6Cidr<wbr>Block</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The IPv6 CIDR block to allow or deny.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Network<wbr>Acl<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the network ACL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Protocol</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The protocol. A value of -1 means all protocols.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rule<wbr>Action</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether to allow or deny the traffic that matches the rule. Accepted values: `allow` | `deny`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rule<wbr>Number</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The rule number for the entry (for example, 100). ACL entries are processed in ascending order by rule number.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">To<wbr>Port</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The to port to match.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Cidr<wbr>Block</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The network range to allow or deny, in CIDR notation (for example 172.16.0.0/24 ).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Egress</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether this is an egress rule (rule is applied to traffic leaving the subnet). Default `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">From<wbr>Port</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The from port to match.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Icmp<wbr>Code</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
ICMP protocol: The ICMP code. Required if specifying ICMP for the protocol. e.g. -1
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Icmp<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
ICMP protocol: The ICMP type. Required if specifying ICMP for the protocol. e.g. -1
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ipv6Cidr<wbr>Block</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The IPv6 CIDR block to allow or deny.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Network<wbr>Acl<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the network ACL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Protocol</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The protocol. A value of -1 means all protocols.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rule<wbr>Action</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether to allow or deny the traffic that matches the rule. Accepted values: `allow` | `deny`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rule<wbr>Number</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The rule number for the entry (for example, 100). ACL entries are processed in ascending order by rule number.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">To<wbr>Port</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The to port to match.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">cidr<wbr>Block</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The network range to allow or deny, in CIDR notation (for example 172.16.0.0/24 ).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">egress</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether this is an egress rule (rule is applied to traffic leaving the subnet). Default `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">from<wbr>Port</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The from port to match.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">icmp<wbr>Code</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
ICMP protocol: The ICMP code. Required if specifying ICMP for the protocol. e.g. -1
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">icmp<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
ICMP protocol: The ICMP type. Required if specifying ICMP for the protocol. e.g. -1
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ipv6Cidr<wbr>Block</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The IPv6 CIDR block to allow or deny.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">network<wbr>Acl<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the network ACL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">protocol</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The protocol. A value of -1 means all protocols.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rule<wbr>Action</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether to allow or deny the traffic that matches the rule. Accepted values: `allow` | `deny`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rule<wbr>Number</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The rule number for the entry (for example, 100). ACL entries are processed in ascending order by rule number.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">to<wbr>Port</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The to port to match.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">cidr_<wbr>block</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The network range to allow or deny, in CIDR notation (for example 172.16.0.0/24 ).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">egress</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether this is an egress rule (rule is applied to traffic leaving the subnet). Default `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">from_<wbr>port</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The from port to match.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">icmp_<wbr>code</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
ICMP protocol: The ICMP code. Required if specifying ICMP for the protocol. e.g. -1
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">icmp_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
ICMP protocol: The ICMP type. Required if specifying ICMP for the protocol. e.g. -1
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ipv6_<wbr>cidr_<wbr>block</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The IPv6 CIDR block to allow or deny.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">network_<wbr>acl_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the network ACL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">protocol</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The protocol. A value of -1 means all protocols.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rule_<wbr>action</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether to allow or deny the traffic that matches the rule. Accepted values: `allow` | `deny`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rule_<wbr>number</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The rule number for the entry (for example, 100). ACL entries are processed in ascending order by rule number.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">to_<wbr>port</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The to port to match.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}









