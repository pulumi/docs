
---
title: "GatewayAssociationProposal"
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>


Manages a Direct Connect Gateway Association Proposal, typically for enabling cross-account associations. For single account associations, see the [`aws.directconnect.GatewayAssociation` resource](https://www.terraform.io/docs/providers/aws/r/dx_gateway_association.html).

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const example = new aws.directconnect.GatewayAssociationProposal("example", {
    associatedGatewayId: aws_vpn_gateway_example.id,
    dxGatewayId: aws_dx_gateway_example.id,
    dxGatewayOwnerAccountId: aws_dx_gateway_example.ownerAccountId,
});
```

A full example of how to create a VPN Gateway in one AWS account, create a Direct Connect Gateway in a second AWS account, and associate the VPN Gateway with the Direct Connect Gateway via the `aws.directconnect.GatewayAssociationProposal` and `aws.directconnect.GatewayAssociation` resources can be found in [the `./examples/dx-gateway-cross-account-vgw-association` directory within the Github Repository](https://github.com/providers/provider-aws/tree/master/examples/dx-gateway-cross-account-vgw-association).

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/dx_gateway_association_proposal.html.markdown.



## Create a GatewayAssociationProposal Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/directconnect/#GatewayAssociationProposal">GatewayAssociationProposal</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/directconnect/#GatewayAssociationProposalArgs">GatewayAssociationProposalArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">GatewayAssociationProposal</span><span class="p">(resource_name, id, opts=None, </span>allowed_prefixes=None<span class="p">, </span>associated_gateway_id=None<span class="p">, </span>dx_gateway_id=None<span class="p">, </span>dx_gateway_owner_account_id=None<span class="p">, </span>vpn_gateway_id=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewGatewayAssociationProposal<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/directconnect?tab=doc#GatewayAssociationProposalArgs">GatewayAssociationProposalArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/directconnect?tab=doc#GatewayAssociationProposal">GatewayAssociationProposal</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Directconnect.GatewayAssociationProposal.html">GatewayAssociationProposal</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Directconnect.GatewayAssociationProposalArgs.html">GatewayAssociationProposalArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a GatewayAssociationProposal resource with the given unique name, arguments, and options.

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
Direct Connect Gateway identifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dx<wbr>Gateway<wbr>Owner<wbr>Account<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
AWS Account identifier of the Direct Connect Gateway&#39;s owner.
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
*Deprecated:* Use `associated_gateway_id` instead. Virtual Gateway identifier to associate with the Direct Connect Gateway.
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
Direct Connect Gateway identifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dx<wbr>Gateway<wbr>Owner<wbr>Account<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
AWS Account identifier of the Direct Connect Gateway&#39;s owner.
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
*Deprecated:* Use `associated_gateway_id` instead. Virtual Gateway identifier to associate with the Direct Connect Gateway.
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
Direct Connect Gateway identifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dx<wbr>Gateway<wbr>Owner<wbr>Account<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
AWS Account identifier of the Direct Connect Gateway&#39;s owner.
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
*Deprecated:* Use `associated_gateway_id` instead. Virtual Gateway identifier to associate with the Direct Connect Gateway.
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
Direct Connect Gateway identifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dx_<wbr>gateway_<wbr>owner_<wbr>account_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
AWS Account identifier of the Direct Connect Gateway&#39;s owner.
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
*Deprecated:* Use `associated_gateway_id` instead. Virtual Gateway identifier to associate with the Direct Connect Gateway.
 {{% /md %}}

            use &#39;associated_gateway_id&#39; argument instead
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## GatewayAssociationProposal Output Properties

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
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the VGW or transit gateway with which to associate the Direct Connect gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Associated<wbr>Gateway<wbr>Owner<wbr>Account<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the AWS account that owns the VGW or transit gateway with which to associate the Direct Connect gateway.
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
            <td class="align-top">Dx<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Direct Connect Gateway identifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dx<wbr>Gateway<wbr>Owner<wbr>Account<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} AWS Account identifier of the Direct Connect Gateway&#39;s owner.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpn<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} *Deprecated:* Use `associated_gateway_id` instead. Virtual Gateway identifier to associate with the Direct Connect Gateway.
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
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the VGW or transit gateway with which to associate the Direct Connect gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Associated<wbr>Gateway<wbr>Owner<wbr>Account<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the AWS account that owns the VGW or transit gateway with which to associate the Direct Connect gateway.
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
            <td class="align-top">Dx<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Direct Connect Gateway identifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dx<wbr>Gateway<wbr>Owner<wbr>Account<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} AWS Account identifier of the Direct Connect Gateway&#39;s owner.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpn<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} *Deprecated:* Use `associated_gateway_id` instead. Virtual Gateway identifier to associate with the Direct Connect Gateway.
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
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the VGW or transit gateway with which to associate the Direct Connect gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">associated<wbr>Gateway<wbr>Owner<wbr>Account<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the AWS account that owns the VGW or transit gateway with which to associate the Direct Connect gateway.
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
            <td class="align-top">dx<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Direct Connect Gateway identifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dx<wbr>Gateway<wbr>Owner<wbr>Account<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} AWS Account identifier of the Direct Connect Gateway&#39;s owner.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpn<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} *Deprecated:* Use `associated_gateway_id` instead. Virtual Gateway identifier to associate with the Direct Connect Gateway.
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
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">associated_<wbr>gateway_<wbr>owner_<wbr>account_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the AWS account that owns the VGW or transit gateway with which to associate the Direct Connect gateway.
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
            <td class="align-top">dx_<wbr>gateway_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Direct Connect Gateway identifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dx_<wbr>gateway_<wbr>owner_<wbr>account_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} AWS Account identifier of the Direct Connect Gateway&#39;s owner.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpn_<wbr>gateway_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} *Deprecated:* Use `associated_gateway_id` instead. Virtual Gateway identifier to associate with the Direct Connect Gateway.
 {{% /md %}}

            use &#39;associated_gateway_id&#39; argument instead
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing GatewayAssociationProposal Resource

{{< langchoose csharp nojavascript >}}

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: GatewayAssociationProposalState, opts?: pulumi.CustomResourceOptions): GatewayAssociationProposal;
```

```python
def get(resource_name, id, opts=None, allowed_<wbr>prefixes=None, associated_<wbr>gateway_<wbr>id=None, associated_<wbr>gateway_<wbr>owner_<wbr>account_<wbr>id=None, associated_<wbr>gateway_<wbr>type=None, dx_<wbr>gateway_<wbr>id=None, dx_<wbr>gateway_<wbr>owner_<wbr>account_<wbr>id=None, vpn_<wbr>gateway_<wbr>id=None)
```

```go
func GetGatewayAssociationProposal(ctx *pulumi.Context, name string, id pulumi.IDInput, state *GatewayAssociationProposalState, opts ...pulumi.ResourceOption) (*Bucket, error)
```

```csharp
public static GatewayAssociationProposal Get(string name, Input<string> id, GatewayAssociationProposalState? state = null, CustomResourceOptions? options = null);
```

Get an existing GatewayAssociationProposal resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
            <td class="align-top">Dx<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Direct Connect Gateway identifier.
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
AWS Account identifier of the Direct Connect Gateway&#39;s owner.
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
*Deprecated:* Use `associated_gateway_id` instead. Virtual Gateway identifier to associate with the Direct Connect Gateway.
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
            <td class="align-top">Dx<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Direct Connect Gateway identifier.
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
AWS Account identifier of the Direct Connect Gateway&#39;s owner.
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
*Deprecated:* Use `associated_gateway_id` instead. Virtual Gateway identifier to associate with the Direct Connect Gateway.
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
            <td class="align-top">dx<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Direct Connect Gateway identifier.
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
AWS Account identifier of the Direct Connect Gateway&#39;s owner.
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
*Deprecated:* Use `associated_gateway_id` instead. Virtual Gateway identifier to associate with the Direct Connect Gateway.
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
            <td class="align-top">dx_<wbr>gateway_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Direct Connect Gateway identifier.
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
AWS Account identifier of the Direct Connect Gateway&#39;s owner.
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
*Deprecated:* Use `associated_gateway_id` instead. Virtual Gateway identifier to associate with the Direct Connect Gateway.
 {{% /md %}}

            use &#39;associated_gateway_id&#39; argument instead
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}









