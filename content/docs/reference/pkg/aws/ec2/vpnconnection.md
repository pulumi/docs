
---
title: "VpnConnection"
block_external_search_index: true
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>

Manages an EC2 VPN connection. These objects can be connected to customer gateways, and allow you to establish tunnels between your network and Amazon.

> **Note:** All arguments including `tunnel1_preshared_key` and `tunnel2_preshared_key` will be stored in the raw state as plain-text.
[Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).

> **Note:** The CIDR blocks in the arguments `tunnel1_inside_cidr` and `tunnel2_inside_cidr` must have a prefix of /30 and be a part of a specific range.
[Read more about this in the AWS documentation](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_VpnTunnelOptionsSpecification.html).

## Example Usage

### EC2 Transit Gateway

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const exampleTransitGateway = new aws.ec2transitgateway.TransitGateway("example", {});
const exampleCustomerGateway = new aws.ec2.CustomerGateway("example", {
    bgpAsn: 65000,
    ipAddress: "172.0.0.1",
    type: "ipsec.1",
});
const exampleVpnConnection = new aws.ec2.VpnConnection("example", {
    customerGatewayId: exampleCustomerGateway.id,
    transitGatewayId: exampleTransitGateway.id,
    type: exampleCustomerGateway.type,
});
```

### Virtual Private Gateway

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const vpc = new aws.ec2.Vpc("vpc", {
    cidrBlock: "10.0.0.0/16",
});
const vpnGateway = new aws.ec2.VpnGateway("vpn_gateway", {
    vpcId: vpc.id,
});
const customerGateway = new aws.ec2.CustomerGateway("customer_gateway", {
    bgpAsn: 65000,
    ipAddress: "172.0.0.1",
    type: "ipsec.1",
});
const main = new aws.ec2.VpnConnection("main", {
    customerGatewayId: customerGateway.id,
    staticRoutesOnly: true,
    type: "ipsec.1",
    vpnGatewayId: vpnGateway.id,
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/vpn_connection.html.markdown.



## Create a VpnConnection Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ec2/#VpnConnection">VpnConnection</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ec2/#VpnConnectionArgs">VpnConnectionArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">VpnConnection</span><span class="p">(resource_name, opts=None, </span>customer_gateway_id=None<span class="p">, </span>static_routes_only=None<span class="p">, </span>tags=None<span class="p">, </span>transit_gateway_id=None<span class="p">, </span>tunnel1_inside_cidr=None<span class="p">, </span>tunnel1_preshared_key=None<span class="p">, </span>tunnel2_inside_cidr=None<span class="p">, </span>tunnel2_preshared_key=None<span class="p">, </span>type=None<span class="p">, </span>vpn_gateway_id=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewVpnConnection<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#VpnConnectionArgs">VpnConnectionArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#VpnConnection">VpnConnection</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.VpnConnection.html">VpnConnection</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.VpnConnectionArgs.html">VpnConnectionArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a VpnConnection resource with the given unique name, arguments, and options.

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
            <td class="align-top">Customer<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the customer gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Static<wbr>Routes<wbr>Only</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether the VPN connection uses static routes exclusively. Static routes must be used for devices that don&#39;t support BGP.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary<string, object>?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Tags to apply to the connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Transit<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the EC2 Transit Gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel1Inside<wbr>Cidr</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CIDR block of the inside IP addresses for the first VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel1Preshared<wbr>Key</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The preshared key of the first VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel2Inside<wbr>Cidr</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CIDR block of the inside IP addresses for the second VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel2Preshared<wbr>Key</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The preshared key of the second VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of VPN connection. The only type AWS supports at this time is &#34;ipsec.1&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpn<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the Virtual Private Gateway.
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
            <td class="align-top">Customer<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the customer gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Static<wbr>Routes<wbr>Only</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether the VPN connection uses static routes exclusively. Static routes must be used for devices that don&#39;t support BGP.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Tags to apply to the connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Transit<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the EC2 Transit Gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel1Inside<wbr>Cidr</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CIDR block of the inside IP addresses for the first VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel1Preshared<wbr>Key</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The preshared key of the first VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel2Inside<wbr>Cidr</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CIDR block of the inside IP addresses for the second VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel2Preshared<wbr>Key</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The preshared key of the second VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of VPN connection. The only type AWS supports at this time is &#34;ipsec.1&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpn<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the Virtual Private Gateway.
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
            <td class="align-top">customer<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the customer gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">static<wbr>Routes<wbr>Only</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether the VPN connection uses static routes exclusively. Static routes must be used for devices that don&#39;t support BGP.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Tags to apply to the connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">transit<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the EC2 Transit Gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel1Inside<wbr>Cidr</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CIDR block of the inside IP addresses for the first VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel1Preshared<wbr>Key</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The preshared key of the first VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel2Inside<wbr>Cidr</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CIDR block of the inside IP addresses for the second VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel2Preshared<wbr>Key</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The preshared key of the second VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of VPN connection. The only type AWS supports at this time is &#34;ipsec.1&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpn<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the Virtual Private Gateway.
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
            <td class="align-top">customer_<wbr>gateway_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the customer gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">static_<wbr>routes_<wbr>only</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether the VPN connection uses static routes exclusively. Static routes must be used for devices that don&#39;t support BGP.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Tags to apply to the connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">transit_<wbr>gateway_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the EC2 Transit Gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel1_<wbr>inside_<wbr>cidr</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CIDR block of the inside IP addresses for the first VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel1_<wbr>preshared_<wbr>key</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The preshared key of the first VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel2_<wbr>inside_<wbr>cidr</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CIDR block of the inside IP addresses for the second VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel2_<wbr>preshared_<wbr>key</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The preshared key of the second VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of VPN connection. The only type AWS supports at this time is &#34;ipsec.1&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpn_<wbr>gateway_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the Virtual Private Gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## VpnConnection Output Properties

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
            <td class="align-top">Customer<wbr>Gateway<wbr>Configuration</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The configuration information for the VPN connection&#39;s customer gateway (in the native XML format).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Customer<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the customer gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Routes</td>
            <td class="align-top">
                
                <code><a href="#vpnconnectionroute">List&lt;Vpn<wbr>Connection<wbr>Route&gt;</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Static<wbr>Routes<wbr>Only</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether the VPN connection uses static routes exclusively. Static routes must be used for devices that don&#39;t support BGP.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary<string, object>?</code>
            </td>
            <td class="align-top">{{% md %}} Tags to apply to the connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Transit<wbr>Gateway<wbr>Attachment<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} When associated with an EC2 Transit Gateway (`transit_gateway_id` argument), the attachment ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Transit<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the EC2 Transit Gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel1Address</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The public IP address of the first VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel1Bgp<wbr>Asn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The bgp asn number of the first VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel1Bgp<wbr>Holdtime</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The bgp holdtime of the first VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel1Cgw<wbr>Inside<wbr>Address</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The RFC 6890 link-local address of the first VPN tunnel (Customer Gateway Side).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel1Inside<wbr>Cidr</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The CIDR block of the inside IP addresses for the first VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel1Preshared<wbr>Key</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The preshared key of the first VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel1Vgw<wbr>Inside<wbr>Address</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The RFC 6890 link-local address of the first VPN tunnel (VPN Gateway Side).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel2Address</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The public IP address of the second VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel2Bgp<wbr>Asn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The bgp asn number of the second VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel2Bgp<wbr>Holdtime</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The bgp holdtime of the second VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel2Cgw<wbr>Inside<wbr>Address</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The RFC 6890 link-local address of the second VPN tunnel (Customer Gateway Side).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel2Inside<wbr>Cidr</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The CIDR block of the inside IP addresses for the second VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel2Preshared<wbr>Key</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The preshared key of the second VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel2Vgw<wbr>Inside<wbr>Address</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The RFC 6890 link-local address of the second VPN tunnel (VPN Gateway Side).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The type of VPN connection. The only type AWS supports at this time is &#34;ipsec.1&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vgw<wbr>Telemetries</td>
            <td class="align-top">
                
                <code><a href="#vpnconnectionvgwtelemetry">List&lt;Vpn<wbr>Connection<wbr>Vgw<wbr>Telemetry&gt;</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpn<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the Virtual Private Gateway.
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
            <td class="align-top">Customer<wbr>Gateway<wbr>Configuration</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The configuration information for the VPN connection&#39;s customer gateway (in the native XML format).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Customer<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the customer gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Routes</td>
            <td class="align-top">
                
                <code><a href="#vpnconnectionroute">[]Vpn<wbr>Connection<wbr>Route<wbr>Type</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Static<wbr>Routes<wbr>Only</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether the VPN connection uses static routes exclusively. Static routes must be used for devices that don&#39;t support BGP.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} Tags to apply to the connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Transit<wbr>Gateway<wbr>Attachment<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} When associated with an EC2 Transit Gateway (`transit_gateway_id` argument), the attachment ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Transit<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the EC2 Transit Gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel1Address</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The public IP address of the first VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel1Bgp<wbr>Asn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The bgp asn number of the first VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel1Bgp<wbr>Holdtime</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The bgp holdtime of the first VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel1Cgw<wbr>Inside<wbr>Address</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The RFC 6890 link-local address of the first VPN tunnel (Customer Gateway Side).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel1Inside<wbr>Cidr</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The CIDR block of the inside IP addresses for the first VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel1Preshared<wbr>Key</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The preshared key of the first VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel1Vgw<wbr>Inside<wbr>Address</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The RFC 6890 link-local address of the first VPN tunnel (VPN Gateway Side).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel2Address</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The public IP address of the second VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel2Bgp<wbr>Asn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The bgp asn number of the second VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel2Bgp<wbr>Holdtime</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The bgp holdtime of the second VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel2Cgw<wbr>Inside<wbr>Address</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The RFC 6890 link-local address of the second VPN tunnel (Customer Gateway Side).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel2Inside<wbr>Cidr</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The CIDR block of the inside IP addresses for the second VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel2Preshared<wbr>Key</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The preshared key of the second VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel2Vgw<wbr>Inside<wbr>Address</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The RFC 6890 link-local address of the second VPN tunnel (VPN Gateway Side).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The type of VPN connection. The only type AWS supports at this time is &#34;ipsec.1&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vgw<wbr>Telemetries</td>
            <td class="align-top">
                
                <code><a href="#vpnconnectionvgwtelemetry">[]Vpn<wbr>Connection<wbr>Vgw<wbr>Telemetry</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpn<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the Virtual Private Gateway.
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
            <td class="align-top">customer<wbr>Gateway<wbr>Configuration</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The configuration information for the VPN connection&#39;s customer gateway (in the native XML format).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">customer<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the customer gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">routes</td>
            <td class="align-top">
                
                <code><a href="#vpnconnectionroute">Vpn<wbr>Connection<wbr>Route[]</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">static<wbr>Routes<wbr>Only</td>
            <td class="align-top">
                
                <code>boolean</code>
            </td>
            <td class="align-top">{{% md %}} Whether the VPN connection uses static routes exclusively. Static routes must be used for devices that don&#39;t support BGP.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} Tags to apply to the connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">transit<wbr>Gateway<wbr>Attachment<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} When associated with an EC2 Transit Gateway (`transit_gateway_id` argument), the attachment ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">transit<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the EC2 Transit Gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel1Address</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The public IP address of the first VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel1Bgp<wbr>Asn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The bgp asn number of the first VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel1Bgp<wbr>Holdtime</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} The bgp holdtime of the first VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel1Cgw<wbr>Inside<wbr>Address</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The RFC 6890 link-local address of the first VPN tunnel (Customer Gateway Side).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel1Inside<wbr>Cidr</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The CIDR block of the inside IP addresses for the first VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel1Preshared<wbr>Key</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The preshared key of the first VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel1Vgw<wbr>Inside<wbr>Address</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The RFC 6890 link-local address of the first VPN tunnel (VPN Gateway Side).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel2Address</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The public IP address of the second VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel2Bgp<wbr>Asn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The bgp asn number of the second VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel2Bgp<wbr>Holdtime</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} The bgp holdtime of the second VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel2Cgw<wbr>Inside<wbr>Address</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The RFC 6890 link-local address of the second VPN tunnel (Customer Gateway Side).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel2Inside<wbr>Cidr</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The CIDR block of the inside IP addresses for the second VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel2Preshared<wbr>Key</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The preshared key of the second VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel2Vgw<wbr>Inside<wbr>Address</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The RFC 6890 link-local address of the second VPN tunnel (VPN Gateway Side).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The type of VPN connection. The only type AWS supports at this time is &#34;ipsec.1&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vgw<wbr>Telemetries</td>
            <td class="align-top">
                
                <code><a href="#vpnconnectionvgwtelemetry">Vpn<wbr>Connection<wbr>Vgw<wbr>Telemetry[]</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpn<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the Virtual Private Gateway.
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
            <td class="align-top">customer_<wbr>gateway_<wbr>configuration</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The configuration information for the VPN connection&#39;s customer gateway (in the native XML format).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">customer_<wbr>gateway_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the customer gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">routes</td>
            <td class="align-top">
                
                <code><a href="#vpnconnectionroute">List[Vpn<wbr>Connection<wbr>Route]</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">static_<wbr>routes_<wbr>only</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether the VPN connection uses static routes exclusively. Static routes must be used for devices that don&#39;t support BGP.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} Tags to apply to the connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">transit_<wbr>gateway_<wbr>attachment_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} When associated with an EC2 Transit Gateway (`transit_gateway_id` argument), the attachment ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">transit_<wbr>gateway_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the EC2 Transit Gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel1_<wbr>address</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The public IP address of the first VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel1_<wbr>bgp_<wbr>asn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The bgp asn number of the first VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel1_<wbr>bgp_<wbr>holdtime</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The bgp holdtime of the first VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel1_<wbr>cgw_<wbr>inside_<wbr>address</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The RFC 6890 link-local address of the first VPN tunnel (Customer Gateway Side).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel1_<wbr>inside_<wbr>cidr</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The CIDR block of the inside IP addresses for the first VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel1_<wbr>preshared_<wbr>key</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The preshared key of the first VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel1_<wbr>vgw_<wbr>inside_<wbr>address</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The RFC 6890 link-local address of the first VPN tunnel (VPN Gateway Side).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel2_<wbr>address</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The public IP address of the second VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel2_<wbr>bgp_<wbr>asn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The bgp asn number of the second VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel2_<wbr>bgp_<wbr>holdtime</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The bgp holdtime of the second VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel2_<wbr>cgw_<wbr>inside_<wbr>address</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The RFC 6890 link-local address of the second VPN tunnel (Customer Gateway Side).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel2_<wbr>inside_<wbr>cidr</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The CIDR block of the inside IP addresses for the second VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel2_<wbr>preshared_<wbr>key</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The preshared key of the second VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel2_<wbr>vgw_<wbr>inside_<wbr>address</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The RFC 6890 link-local address of the second VPN tunnel (VPN Gateway Side).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The type of VPN connection. The only type AWS supports at this time is &#34;ipsec.1&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vgw_<wbr>telemetries</td>
            <td class="align-top">
                
                <code><a href="#vpnconnectionvgwtelemetry">List[Vpn<wbr>Connection<wbr>Vgw<wbr>Telemetry]</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpn_<wbr>gateway_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the Virtual Private Gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing VpnConnection Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ec2/#VpnConnectionState">VpnConnectionState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ec2/#VpnConnection">VpnConnection</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>customer_gateway_configuration=None<span class="p">, </span>customer_gateway_id=None<span class="p">, </span>routes=None<span class="p">, </span>static_routes_only=None<span class="p">, </span>tags=None<span class="p">, </span>transit_gateway_attachment_id=None<span class="p">, </span>transit_gateway_id=None<span class="p">, </span>tunnel1_address=None<span class="p">, </span>tunnel1_bgp_asn=None<span class="p">, </span>tunnel1_bgp_holdtime=None<span class="p">, </span>tunnel1_cgw_inside_address=None<span class="p">, </span>tunnel1_inside_cidr=None<span class="p">, </span>tunnel1_preshared_key=None<span class="p">, </span>tunnel1_vgw_inside_address=None<span class="p">, </span>tunnel2_address=None<span class="p">, </span>tunnel2_bgp_asn=None<span class="p">, </span>tunnel2_bgp_holdtime=None<span class="p">, </span>tunnel2_cgw_inside_address=None<span class="p">, </span>tunnel2_inside_cidr=None<span class="p">, </span>tunnel2_preshared_key=None<span class="p">, </span>tunnel2_vgw_inside_address=None<span class="p">, </span>type=None<span class="p">, </span>vgw_telemetries=None<span class="p">, </span>vpn_gateway_id=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetVpnConnection<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#VpnConnectionState">VpnConnectionState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#VpnConnection">VpnConnection</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.VpnConnection.html">VpnConnection</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.VpnConnectionState.html">VpnConnectionState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Get an existing VpnConnection resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
            <td class="align-top">Customer<wbr>Gateway<wbr>Configuration</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The configuration information for the VPN connection&#39;s customer gateway (in the native XML format).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Customer<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the customer gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Routes</td>
            <td class="align-top">
                
                <code><a href="#vpnconnectionroute">List&lt;Vpn<wbr>Connection<wbr>Route<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Static<wbr>Routes<wbr>Only</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether the VPN connection uses static routes exclusively. Static routes must be used for devices that don&#39;t support BGP.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary<string, object>?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Tags to apply to the connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Transit<wbr>Gateway<wbr>Attachment<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When associated with an EC2 Transit Gateway (`transit_gateway_id` argument), the attachment ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Transit<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the EC2 Transit Gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel1Address</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The public IP address of the first VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel1Bgp<wbr>Asn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The bgp asn number of the first VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel1Bgp<wbr>Holdtime</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The bgp holdtime of the first VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel1Cgw<wbr>Inside<wbr>Address</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The RFC 6890 link-local address of the first VPN tunnel (Customer Gateway Side).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel1Inside<wbr>Cidr</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CIDR block of the inside IP addresses for the first VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel1Preshared<wbr>Key</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The preshared key of the first VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel1Vgw<wbr>Inside<wbr>Address</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The RFC 6890 link-local address of the first VPN tunnel (VPN Gateway Side).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel2Address</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The public IP address of the second VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel2Bgp<wbr>Asn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The bgp asn number of the second VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel2Bgp<wbr>Holdtime</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The bgp holdtime of the second VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel2Cgw<wbr>Inside<wbr>Address</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The RFC 6890 link-local address of the second VPN tunnel (Customer Gateway Side).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel2Inside<wbr>Cidr</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CIDR block of the inside IP addresses for the second VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel2Preshared<wbr>Key</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The preshared key of the second VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel2Vgw<wbr>Inside<wbr>Address</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The RFC 6890 link-local address of the second VPN tunnel (VPN Gateway Side).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of VPN connection. The only type AWS supports at this time is &#34;ipsec.1&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vgw<wbr>Telemetries</td>
            <td class="align-top">
                
                <code><a href="#vpnconnectionvgwtelemetry">List&lt;Vpn<wbr>Connection<wbr>Vgw<wbr>Telemetry<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpn<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the Virtual Private Gateway.
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
            <td class="align-top">Customer<wbr>Gateway<wbr>Configuration</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The configuration information for the VPN connection&#39;s customer gateway (in the native XML format).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Customer<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the customer gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Routes</td>
            <td class="align-top">
                
                <code><a href="#vpnconnectionroute">[]Vpn<wbr>Connection<wbr>Route<wbr>Type</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Static<wbr>Routes<wbr>Only</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether the VPN connection uses static routes exclusively. Static routes must be used for devices that don&#39;t support BGP.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Tags to apply to the connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Transit<wbr>Gateway<wbr>Attachment<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When associated with an EC2 Transit Gateway (`transit_gateway_id` argument), the attachment ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Transit<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the EC2 Transit Gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel1Address</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The public IP address of the first VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel1Bgp<wbr>Asn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The bgp asn number of the first VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel1Bgp<wbr>Holdtime</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The bgp holdtime of the first VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel1Cgw<wbr>Inside<wbr>Address</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The RFC 6890 link-local address of the first VPN tunnel (Customer Gateway Side).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel1Inside<wbr>Cidr</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CIDR block of the inside IP addresses for the first VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel1Preshared<wbr>Key</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The preshared key of the first VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel1Vgw<wbr>Inside<wbr>Address</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The RFC 6890 link-local address of the first VPN tunnel (VPN Gateway Side).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel2Address</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The public IP address of the second VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel2Bgp<wbr>Asn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The bgp asn number of the second VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel2Bgp<wbr>Holdtime</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The bgp holdtime of the second VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel2Cgw<wbr>Inside<wbr>Address</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The RFC 6890 link-local address of the second VPN tunnel (Customer Gateway Side).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel2Inside<wbr>Cidr</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CIDR block of the inside IP addresses for the second VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel2Preshared<wbr>Key</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The preshared key of the second VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tunnel2Vgw<wbr>Inside<wbr>Address</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The RFC 6890 link-local address of the second VPN tunnel (VPN Gateway Side).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of VPN connection. The only type AWS supports at this time is &#34;ipsec.1&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vgw<wbr>Telemetries</td>
            <td class="align-top">
                
                <code><a href="#vpnconnectionvgwtelemetry">[]Vpn<wbr>Connection<wbr>Vgw<wbr>Telemetry</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpn<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the Virtual Private Gateway.
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
            <td class="align-top">customer<wbr>Gateway<wbr>Configuration</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The configuration information for the VPN connection&#39;s customer gateway (in the native XML format).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">customer<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the customer gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">routes</td>
            <td class="align-top">
                
                <code><a href="#vpnconnectionroute">Vpn<wbr>Connection<wbr>Route[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">static<wbr>Routes<wbr>Only</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether the VPN connection uses static routes exclusively. Static routes must be used for devices that don&#39;t support BGP.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Tags to apply to the connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">transit<wbr>Gateway<wbr>Attachment<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When associated with an EC2 Transit Gateway (`transit_gateway_id` argument), the attachment ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">transit<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the EC2 Transit Gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel1Address</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The public IP address of the first VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel1Bgp<wbr>Asn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The bgp asn number of the first VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel1Bgp<wbr>Holdtime</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The bgp holdtime of the first VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel1Cgw<wbr>Inside<wbr>Address</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The RFC 6890 link-local address of the first VPN tunnel (Customer Gateway Side).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel1Inside<wbr>Cidr</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CIDR block of the inside IP addresses for the first VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel1Preshared<wbr>Key</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The preshared key of the first VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel1Vgw<wbr>Inside<wbr>Address</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The RFC 6890 link-local address of the first VPN tunnel (VPN Gateway Side).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel2Address</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The public IP address of the second VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel2Bgp<wbr>Asn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The bgp asn number of the second VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel2Bgp<wbr>Holdtime</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The bgp holdtime of the second VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel2Cgw<wbr>Inside<wbr>Address</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The RFC 6890 link-local address of the second VPN tunnel (Customer Gateway Side).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel2Inside<wbr>Cidr</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CIDR block of the inside IP addresses for the second VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel2Preshared<wbr>Key</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The preshared key of the second VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel2Vgw<wbr>Inside<wbr>Address</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The RFC 6890 link-local address of the second VPN tunnel (VPN Gateway Side).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of VPN connection. The only type AWS supports at this time is &#34;ipsec.1&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vgw<wbr>Telemetries</td>
            <td class="align-top">
                
                <code><a href="#vpnconnectionvgwtelemetry">Vpn<wbr>Connection<wbr>Vgw<wbr>Telemetry[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpn<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the Virtual Private Gateway.
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
            <td class="align-top">customer_<wbr>gateway_<wbr>configuration</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The configuration information for the VPN connection&#39;s customer gateway (in the native XML format).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">customer_<wbr>gateway_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the customer gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">routes</td>
            <td class="align-top">
                
                <code><a href="#vpnconnectionroute">List[Vpn<wbr>Connection<wbr>Route]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">static_<wbr>routes_<wbr>only</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether the VPN connection uses static routes exclusively. Static routes must be used for devices that don&#39;t support BGP.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Tags to apply to the connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">transit_<wbr>gateway_<wbr>attachment_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When associated with an EC2 Transit Gateway (`transit_gateway_id` argument), the attachment ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">transit_<wbr>gateway_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the EC2 Transit Gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel1_<wbr>address</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The public IP address of the first VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel1_<wbr>bgp_<wbr>asn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The bgp asn number of the first VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel1_<wbr>bgp_<wbr>holdtime</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The bgp holdtime of the first VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel1_<wbr>cgw_<wbr>inside_<wbr>address</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The RFC 6890 link-local address of the first VPN tunnel (Customer Gateway Side).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel1_<wbr>inside_<wbr>cidr</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CIDR block of the inside IP addresses for the first VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel1_<wbr>preshared_<wbr>key</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The preshared key of the first VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel1_<wbr>vgw_<wbr>inside_<wbr>address</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The RFC 6890 link-local address of the first VPN tunnel (VPN Gateway Side).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel2_<wbr>address</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The public IP address of the second VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel2_<wbr>bgp_<wbr>asn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The bgp asn number of the second VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel2_<wbr>bgp_<wbr>holdtime</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The bgp holdtime of the second VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel2_<wbr>cgw_<wbr>inside_<wbr>address</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The RFC 6890 link-local address of the second VPN tunnel (Customer Gateway Side).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel2_<wbr>inside_<wbr>cidr</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CIDR block of the inside IP addresses for the second VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel2_<wbr>preshared_<wbr>key</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The preshared key of the second VPN tunnel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tunnel2_<wbr>vgw_<wbr>inside_<wbr>address</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The RFC 6890 link-local address of the second VPN tunnel (VPN Gateway Side).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of VPN connection. The only type AWS supports at this time is &#34;ipsec.1&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vgw_<wbr>telemetries</td>
            <td class="align-top">
                
                <code><a href="#vpnconnectionvgwtelemetry">List[Vpn<wbr>Connection<wbr>Vgw<wbr>Telemetry]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpn_<wbr>gateway_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the Virtual Private Gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### VpnConnectionRoute
{{% lang nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#VpnConnectionRoute">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#VpnConnectionRouteTypeOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the   <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.VpnConnectionRoute.html">output</a> API doc for this type.
{{% /lang %}}



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
            <td class="align-top">Destination<wbr>Cidr<wbr>Block</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">State</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
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
            <td class="align-top">Destination<wbr>Cidr<wbr>Block</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">State</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
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
            <td class="align-top">destination<wbr>Cidr<wbr>Block</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">state</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
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
            <td class="align-top">destination_<wbr>cidr_<wbr>block</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">state</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### VpnConnectionVgwTelemetry
{{% lang nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#VpnConnectionVgwTelemetry">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#VpnConnectionVgwTelemetryOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the   <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.VpnConnectionVgwTelemetry.html">output</a> API doc for this type.
{{% /lang %}}



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
            <td class="align-top">Accepted<wbr>Route<wbr>Count</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Last<wbr>Status<wbr>Change</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Outside<wbr>Ip<wbr>Address</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Status</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Status<wbr>Message</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
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
            <td class="align-top">Accepted<wbr>Route<wbr>Count</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Last<wbr>Status<wbr>Change</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Outside<wbr>Ip<wbr>Address</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Status</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Status<wbr>Message</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
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
            <td class="align-top">accepted<wbr>Route<wbr>Count</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">last<wbr>Status<wbr>Change</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">outside<wbr>Ip<wbr>Address</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">status</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">status<wbr>Message</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
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
            <td class="align-top">accepted<wbr>Route<wbr>Count</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">last<wbr>Status<wbr>Change</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">outside<wbr>Ip<wbr>Address</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">status</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">status<wbr>Message</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







