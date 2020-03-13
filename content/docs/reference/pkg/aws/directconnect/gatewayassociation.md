
---
title: "GatewayAssociation"
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>


Associates a Direct Connect Gateway with a VGW or transit gateway.

To create a cross-account association, create an [`aws.directconnect.GatewayAssociationProposal` resource](https://www.terraform.io/docs/providers/aws/r/dx_gateway_association_proposal.html)
in the AWS account that owns the VGW or transit gateway and then accept the proposal in the AWS account that owns the Direct Connect Gateway
by creating an `aws.directconnect.GatewayAssociation` resource with the `proposal_id` and `associated_gateway_owner_account_id` attributes set.

## Example Usage

### VPN Gateway Association

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const exampleGateway = new aws.directconnect.Gateway("example", {
    amazonSideAsn: "64512",
});
const exampleVpc = new aws.ec2.Vpc("example", {
    cidrBlock: "10.255.255.0/28",
});
const exampleVpnGateway = new aws.ec2.VpnGateway("example", {
    vpcId: exampleVpc.id,
});
const exampleGatewayAssociation = new aws.directconnect.GatewayAssociation("example", {
    associatedGatewayId: exampleVpnGateway.id,
    dxGatewayId: exampleGateway.id,
});
```

### Transit Gateway Association

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const exampleGateway = new aws.directconnect.Gateway("example", {
    amazonSideAsn: "64512",
});
const exampleTransitGateway = new aws.ec2transitgateway.TransitGateway("example", {});
const exampleGatewayAssociation = new aws.directconnect.GatewayAssociation("example", {
    allowedPrefixes: [
        "10.255.255.0/30",
        "10.255.255.8/30",
    ],
    associatedGatewayId: exampleTransitGateway.id,
    dxGatewayId: exampleGateway.id,
});
```

### Allowed Prefixes

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const exampleGateway = new aws.directconnect.Gateway("example", {
    amazonSideAsn: "64512",
});
const exampleVpc = new aws.ec2.Vpc("example", {
    cidrBlock: "10.255.255.0/28",
});
const exampleVpnGateway = new aws.ec2.VpnGateway("example", {
    vpcId: exampleVpc.id,
});
const exampleGatewayAssociation = new aws.directconnect.GatewayAssociation("example", {
    allowedPrefixes: [
        "210.52.109.0/24",
        "175.45.176.0/22",
    ],
    associatedGatewayId: exampleVpnGateway.id,
    dxGatewayId: exampleGateway.id,
});
```

A full example of how to create a VPN Gateway in one AWS account, create a Direct Connect Gateway in a second AWS account, and associate the VPN Gateway with the Direct Connect Gateway via the `aws.directconnect.GatewayAssociationProposal` and `aws.directconnect.GatewayAssociation` resources can be found in [the `./examples/dx-gateway-cross-account-vgw-association` directory within the Github Repository](https://github.com/providers/provider-aws/tree/master/examples/dx-gateway-cross-account-vgw-association).

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/dx_gateway_association.html.markdown.



## Create a GatewayAssociation Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/directconnect/#GatewayAssociation">GatewayAssociation</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/directconnect/#GatewayAssociationArgs">GatewayAssociationArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">GatewayAssociation</span><span class="p">(resource_name, id, opts=None, </span>allowed_prefixes=None<span class="p">, </span>associated_gateway_id=None<span class="p">, </span>associated_gateway_owner_account_id=None<span class="p">, </span>dx_gateway_id=None<span class="p">, </span>proposal_id=None<span class="p">, </span>vpn_gateway_id=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewGatewayAssociation<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/directconnect?tab=doc#GatewayAssociationArgs">GatewayAssociationArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/directconnect?tab=doc#GatewayAssociation">GatewayAssociation</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Directconnect.GatewayAssociation.html">GatewayAssociation</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Directconnect.GatewayAssociationArgs.html">GatewayAssociationArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a GatewayAssociation resource with the given unique name, arguments, and options.

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
            <td class="align-top">Allowed<wbr>Prefixes</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
VPC prefixes (CIDRs) to advertise to the Direct Connect gateway. Defaults to the CIDR block of the VPC associated with the Virtual Gateway. To enable drift detection, must be configured.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Associated<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the VGW or transit gateway with which to associate the Direct Connect gateway.
Used for single account Direct Connect gateway associations.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Associated<wbr>Gateway<wbr>Owner<wbr>Account<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the AWS account that owns the VGW or transit gateway with which to associate the Direct Connect gateway.
Used for cross-account Direct Connect gateway associations.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dx<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the Direct Connect gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Proposal<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the Direct Connect gateway association proposal.
Used for cross-account Direct Connect gateway associations.
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
*Deprecated:* Use `associated_gateway_id` instead. The ID of the VGW with which to associate the gateway.
Used for single account Direct Connect gateway associations.
 {{% /md %}}

            use &#39;associated_gateway_id&#39; argument instead
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
            <td class="align-top">Allowed<wbr>Prefixes</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
VPC prefixes (CIDRs) to advertise to the Direct Connect gateway. Defaults to the CIDR block of the VPC associated with the Virtual Gateway. To enable drift detection, must be configured.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Associated<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the VGW or transit gateway with which to associate the Direct Connect gateway.
Used for single account Direct Connect gateway associations.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Associated<wbr>Gateway<wbr>Owner<wbr>Account<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the AWS account that owns the VGW or transit gateway with which to associate the Direct Connect gateway.
Used for cross-account Direct Connect gateway associations.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dx<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the Direct Connect gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Proposal<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the Direct Connect gateway association proposal.
Used for cross-account Direct Connect gateway associations.
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
*Deprecated:* Use `associated_gateway_id` instead. The ID of the VGW with which to associate the gateway.
Used for single account Direct Connect gateway associations.
 {{% /md %}}

            use &#39;associated_gateway_id&#39; argument instead
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
            <td class="align-top">allowed<wbr>Prefixes</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
VPC prefixes (CIDRs) to advertise to the Direct Connect gateway. Defaults to the CIDR block of the VPC associated with the Virtual Gateway. To enable drift detection, must be configured.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">associated<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the VGW or transit gateway with which to associate the Direct Connect gateway.
Used for single account Direct Connect gateway associations.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">associated<wbr>Gateway<wbr>Owner<wbr>Account<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the AWS account that owns the VGW or transit gateway with which to associate the Direct Connect gateway.
Used for cross-account Direct Connect gateway associations.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dx<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the Direct Connect gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">proposal<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the Direct Connect gateway association proposal.
Used for cross-account Direct Connect gateway associations.
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
*Deprecated:* Use `associated_gateway_id` instead. The ID of the VGW with which to associate the gateway.
Used for single account Direct Connect gateway associations.
 {{% /md %}}

            use &#39;associated_gateway_id&#39; argument instead
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
            <td class="align-top">allowed_<wbr>prefixes</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
VPC prefixes (CIDRs) to advertise to the Direct Connect gateway. Defaults to the CIDR block of the VPC associated with the Virtual Gateway. To enable drift detection, must be configured.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">associated_<wbr>gateway_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the VGW or transit gateway with which to associate the Direct Connect gateway.
Used for single account Direct Connect gateway associations.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">associated_<wbr>gateway_<wbr>owner_<wbr>account_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the AWS account that owns the VGW or transit gateway with which to associate the Direct Connect gateway.
Used for cross-account Direct Connect gateway associations.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dx_<wbr>gateway_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the Direct Connect gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">proposal_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the Direct Connect gateway association proposal.
Used for cross-account Direct Connect gateway associations.
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
*Deprecated:* Use `associated_gateway_id` instead. The ID of the VGW with which to associate the gateway.
Used for single account Direct Connect gateway associations.
 {{% /md %}}

            use &#39;associated_gateway_id&#39; argument instead
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## GatewayAssociation Output Properties

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
            <td class="align-top">Allowed<wbr>Prefixes</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} VPC prefixes (CIDRs) to advertise to the Direct Connect gateway. Defaults to the CIDR block of the VPC associated with the Virtual Gateway. To enable drift detection, must be configured.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Associated<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the VGW or transit gateway with which to associate the Direct Connect gateway.
Used for single account Direct Connect gateway associations.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Associated<wbr>Gateway<wbr>Owner<wbr>Account<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the AWS account that owns the VGW or transit gateway with which to associate the Direct Connect gateway.
Used for cross-account Direct Connect gateway associations.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Associated<wbr>Gateway<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The type of the associated gateway, `transitGateway` or `virtualPrivateGateway`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dx<wbr>Gateway<wbr>Association<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the Direct Connect gateway association.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dx<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the Direct Connect gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dx<wbr>Gateway<wbr>Owner<wbr>Account<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the AWS account that owns the Direct Connect gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Proposal<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the Direct Connect gateway association proposal.
Used for cross-account Direct Connect gateway associations.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpn<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} *Deprecated:* Use `associated_gateway_id` instead. The ID of the VGW with which to associate the gateway.
Used for single account Direct Connect gateway associations.
 {{% /md %}}

            use &#39;associated_gateway_id&#39; argument instead
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
            <td class="align-top">Allowed<wbr>Prefixes</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} VPC prefixes (CIDRs) to advertise to the Direct Connect gateway. Defaults to the CIDR block of the VPC associated with the Virtual Gateway. To enable drift detection, must be configured.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Associated<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the VGW or transit gateway with which to associate the Direct Connect gateway.
Used for single account Direct Connect gateway associations.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Associated<wbr>Gateway<wbr>Owner<wbr>Account<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the AWS account that owns the VGW or transit gateway with which to associate the Direct Connect gateway.
Used for cross-account Direct Connect gateway associations.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Associated<wbr>Gateway<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The type of the associated gateway, `transitGateway` or `virtualPrivateGateway`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dx<wbr>Gateway<wbr>Association<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the Direct Connect gateway association.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dx<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the Direct Connect gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dx<wbr>Gateway<wbr>Owner<wbr>Account<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the AWS account that owns the Direct Connect gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Proposal<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the Direct Connect gateway association proposal.
Used for cross-account Direct Connect gateway associations.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpn<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} *Deprecated:* Use `associated_gateway_id` instead. The ID of the VGW with which to associate the gateway.
Used for single account Direct Connect gateway associations.
 {{% /md %}}

            use &#39;associated_gateway_id&#39; argument instead
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
            <td class="align-top">allowed<wbr>Prefixes</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} VPC prefixes (CIDRs) to advertise to the Direct Connect gateway. Defaults to the CIDR block of the VPC associated with the Virtual Gateway. To enable drift detection, must be configured.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">associated<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the VGW or transit gateway with which to associate the Direct Connect gateway.
Used for single account Direct Connect gateway associations.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">associated<wbr>Gateway<wbr>Owner<wbr>Account<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the AWS account that owns the VGW or transit gateway with which to associate the Direct Connect gateway.
Used for cross-account Direct Connect gateway associations.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">associated<wbr>Gateway<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The type of the associated gateway, `transitGateway` or `virtualPrivateGateway`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dx<wbr>Gateway<wbr>Association<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the Direct Connect gateway association.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dx<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the Direct Connect gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dx<wbr>Gateway<wbr>Owner<wbr>Account<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the AWS account that owns the Direct Connect gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">proposal<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the Direct Connect gateway association proposal.
Used for cross-account Direct Connect gateway associations.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpn<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} *Deprecated:* Use `associated_gateway_id` instead. The ID of the VGW with which to associate the gateway.
Used for single account Direct Connect gateway associations.
 {{% /md %}}

            use &#39;associated_gateway_id&#39; argument instead
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
            <td class="align-top">allowed_<wbr>prefixes</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} VPC prefixes (CIDRs) to advertise to the Direct Connect gateway. Defaults to the CIDR block of the VPC associated with the Virtual Gateway. To enable drift detection, must be configured.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">associated_<wbr>gateway_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the VGW or transit gateway with which to associate the Direct Connect gateway.
Used for single account Direct Connect gateway associations.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">associated_<wbr>gateway_<wbr>owner_<wbr>account_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the AWS account that owns the VGW or transit gateway with which to associate the Direct Connect gateway.
Used for cross-account Direct Connect gateway associations.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">associated_<wbr>gateway_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The type of the associated gateway, `transitGateway` or `virtualPrivateGateway`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dx_<wbr>gateway_<wbr>association_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the Direct Connect gateway association.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dx_<wbr>gateway_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the Direct Connect gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dx_<wbr>gateway_<wbr>owner_<wbr>account_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the AWS account that owns the Direct Connect gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">proposal_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the Direct Connect gateway association proposal.
Used for cross-account Direct Connect gateway associations.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpn_<wbr>gateway_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} *Deprecated:* Use `associated_gateway_id` instead. The ID of the VGW with which to associate the gateway.
Used for single account Direct Connect gateway associations.
 {{% /md %}}

            use &#39;associated_gateway_id&#39; argument instead
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing GatewayAssociation Resource

{{< langchoose csharp nojavascript >}}

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: GatewayAssociationState, opts?: pulumi.CustomResourceOptions): GatewayAssociation;
```

```python
def get(resource_name, id, opts=None, allowed_<wbr>prefixes=None, associated_<wbr>gateway_<wbr>id=None, associated_<wbr>gateway_<wbr>owner_<wbr>account_<wbr>id=None, associated_<wbr>gateway_<wbr>type=None, dx_<wbr>gateway_<wbr>association_<wbr>id=None, dx_<wbr>gateway_<wbr>id=None, dx_<wbr>gateway_<wbr>owner_<wbr>account_<wbr>id=None, proposal_<wbr>id=None, vpn_<wbr>gateway_<wbr>id=None)
```

```go
func GetGatewayAssociation(ctx *pulumi.Context, name string, id pulumi.IDInput, state *GatewayAssociationState, opts ...pulumi.ResourceOption) (*Bucket, error)
```

```csharp
public static GatewayAssociation Get(string name, Input<string> id, GatewayAssociationState? state = null, CustomResourceOptions? options = null);
```

Get an existing GatewayAssociation resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
            <td class="align-top">Allowed<wbr>Prefixes</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
VPC prefixes (CIDRs) to advertise to the Direct Connect gateway. Defaults to the CIDR block of the VPC associated with the Virtual Gateway. To enable drift detection, must be configured.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Associated<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the VGW or transit gateway with which to associate the Direct Connect gateway.
Used for single account Direct Connect gateway associations.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Associated<wbr>Gateway<wbr>Owner<wbr>Account<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the AWS account that owns the VGW or transit gateway with which to associate the Direct Connect gateway.
Used for cross-account Direct Connect gateway associations.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Associated<wbr>Gateway<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of the associated gateway, `transitGateway` or `virtualPrivateGateway`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dx<wbr>Gateway<wbr>Association<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the Direct Connect gateway association.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dx<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the Direct Connect gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dx<wbr>Gateway<wbr>Owner<wbr>Account<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the AWS account that owns the Direct Connect gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Proposal<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the Direct Connect gateway association proposal.
Used for cross-account Direct Connect gateway associations.
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
*Deprecated:* Use `associated_gateway_id` instead. The ID of the VGW with which to associate the gateway.
Used for single account Direct Connect gateway associations.
 {{% /md %}}

            use &#39;associated_gateway_id&#39; argument instead
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
            <td class="align-top">Allowed<wbr>Prefixes</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
VPC prefixes (CIDRs) to advertise to the Direct Connect gateway. Defaults to the CIDR block of the VPC associated with the Virtual Gateway. To enable drift detection, must be configured.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Associated<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the VGW or transit gateway with which to associate the Direct Connect gateway.
Used for single account Direct Connect gateway associations.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Associated<wbr>Gateway<wbr>Owner<wbr>Account<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the AWS account that owns the VGW or transit gateway with which to associate the Direct Connect gateway.
Used for cross-account Direct Connect gateway associations.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Associated<wbr>Gateway<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of the associated gateway, `transitGateway` or `virtualPrivateGateway`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dx<wbr>Gateway<wbr>Association<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the Direct Connect gateway association.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dx<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the Direct Connect gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dx<wbr>Gateway<wbr>Owner<wbr>Account<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the AWS account that owns the Direct Connect gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Proposal<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the Direct Connect gateway association proposal.
Used for cross-account Direct Connect gateway associations.
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
*Deprecated:* Use `associated_gateway_id` instead. The ID of the VGW with which to associate the gateway.
Used for single account Direct Connect gateway associations.
 {{% /md %}}

            use &#39;associated_gateway_id&#39; argument instead
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
            <td class="align-top">allowed<wbr>Prefixes</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
VPC prefixes (CIDRs) to advertise to the Direct Connect gateway. Defaults to the CIDR block of the VPC associated with the Virtual Gateway. To enable drift detection, must be configured.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">associated<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the VGW or transit gateway with which to associate the Direct Connect gateway.
Used for single account Direct Connect gateway associations.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">associated<wbr>Gateway<wbr>Owner<wbr>Account<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the AWS account that owns the VGW or transit gateway with which to associate the Direct Connect gateway.
Used for cross-account Direct Connect gateway associations.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">associated<wbr>Gateway<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of the associated gateway, `transitGateway` or `virtualPrivateGateway`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dx<wbr>Gateway<wbr>Association<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the Direct Connect gateway association.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dx<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the Direct Connect gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dx<wbr>Gateway<wbr>Owner<wbr>Account<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the AWS account that owns the Direct Connect gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">proposal<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the Direct Connect gateway association proposal.
Used for cross-account Direct Connect gateway associations.
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
*Deprecated:* Use `associated_gateway_id` instead. The ID of the VGW with which to associate the gateway.
Used for single account Direct Connect gateway associations.
 {{% /md %}}

            use &#39;associated_gateway_id&#39; argument instead
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
            <td class="align-top">allowed_<wbr>prefixes</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
VPC prefixes (CIDRs) to advertise to the Direct Connect gateway. Defaults to the CIDR block of the VPC associated with the Virtual Gateway. To enable drift detection, must be configured.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">associated_<wbr>gateway_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the VGW or transit gateway with which to associate the Direct Connect gateway.
Used for single account Direct Connect gateway associations.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">associated_<wbr>gateway_<wbr>owner_<wbr>account_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the AWS account that owns the VGW or transit gateway with which to associate the Direct Connect gateway.
Used for cross-account Direct Connect gateway associations.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">associated_<wbr>gateway_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of the associated gateway, `transitGateway` or `virtualPrivateGateway`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dx_<wbr>gateway_<wbr>association_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the Direct Connect gateway association.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dx_<wbr>gateway_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the Direct Connect gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dx_<wbr>gateway_<wbr>owner_<wbr>account_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the AWS account that owns the Direct Connect gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">proposal_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the Direct Connect gateway association proposal.
Used for cross-account Direct Connect gateway associations.
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
*Deprecated:* Use `associated_gateway_id` instead. The ID of the VGW with which to associate the gateway.
Used for single account Direct Connect gateway associations.
 {{% /md %}}

            use &#39;associated_gateway_id&#39; argument instead
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}









