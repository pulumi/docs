
---
title: "VpcPeeringConnection"
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>


Provides a resource to manage a VPC peering connection.

> **NOTE on VPC Peering Connections and VPC Peering Connection Options:** This provider provides
both a standalone VPC Peering Connection Options and a VPC Peering Connection
resource with `accepter` and `requester` attributes. Do not manage options for the same VPC peering
connection in both a VPC Peering Connection resource and a VPC Peering Connection Options resource.
Doing so will cause a conflict of options and will overwrite the options.
Using a VPC Peering Connection Options resource decouples management of the connection options from
management of the VPC Peering Connection and allows options to be set correctly in cross-account scenarios.

> **Note:** For cross-account (requester's AWS account differs from the accepter's AWS account) or inter-region
VPC Peering Connections use the `aws.ec2.VpcPeeringConnection` resource to manage the requester's side of the
connection and use the `aws.ec2.VpcPeeringConnectionAccepter` resource to manage the accepter's side of the connection.

## Notes

If both VPCs are not in the same AWS account do not enable the `auto_accept` attribute.
The accepter can manage its side of the connection using the `aws.ec2.VpcPeeringConnectionAccepter` resource
or accept the connection manually using the AWS Management Console, AWS CLI, through SDKs, etc.

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/vpc_peering_connection.html.markdown.



## Create a VpcPeeringConnection Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ec2/#VpcPeeringConnection">VpcPeeringConnection</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ec2/#VpcPeeringConnectionArgs">VpcPeeringConnectionArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">VpcPeeringConnection</span><span class="p">(resource_name, opts=None, </span>accepter=None<span class="p">, </span>auto_accept=None<span class="p">, </span>peer_owner_id=None<span class="p">, </span>peer_region=None<span class="p">, </span>peer_vpc_id=None<span class="p">, </span>requester=None<span class="p">, </span>tags=None<span class="p">, </span>vpc_id=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewVpcPeeringConnection<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#VpcPeeringConnectionArgs">VpcPeeringConnectionArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#VpcPeeringConnection">VpcPeeringConnection</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.VpcPeeringConnection.html">VpcPeeringConnection</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.VpcPeeringConnectionArgs.html">VpcPeeringConnectionArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a VpcPeeringConnection resource with the given unique name, arguments, and options.

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
            <td class="align-top">Accepter</td>
            <td class="align-top">
                
                <code><a href="#vpcpeeringconnectionaccepter">Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Vpc<wbr>Peering<wbr>Connection<wbr>Accepter<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An optional configuration block that allows for [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options to be set for the VPC that accepts
the peering connection (a maximum of one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Auto<wbr>Accept</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Accept the peering (both VPCs need to be in the same AWS account).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Peer<wbr>Owner<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS account ID of the owner of the peer VPC.
Defaults to the account ID the [AWS provider][1] is currently connected to.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Peer<wbr>Region</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The region of the accepter VPC of the [VPC Peering Connection]. `auto_accept` must be `false`,
and use the `aws.ec2.VpcPeeringConnectionAccepter` to manage the accepter side.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Peer<wbr>Vpc<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the VPC with which you are creating the VPC Peering Connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Requester</td>
            <td class="align-top">
                
                <code><a href="#vpcpeeringconnectionrequester">Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Vpc<wbr>Peering<wbr>Connection<wbr>Requester<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A optional configuration block that allows for [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options to be set for the VPC that requests
the peering connection (a maximum of one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the requester VPC.
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
            <td class="align-top">Accepter</td>
            <td class="align-top">
                
                <code><a href="#vpcpeeringconnectionaccepter">*ec2.<wbr>Vpc<wbr>Peering<wbr>Connection<wbr>Accepter</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An optional configuration block that allows for [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options to be set for the VPC that accepts
the peering connection (a maximum of one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Auto<wbr>Accept</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Accept the peering (both VPCs need to be in the same AWS account).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Peer<wbr>Owner<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS account ID of the owner of the peer VPC.
Defaults to the account ID the [AWS provider][1] is currently connected to.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Peer<wbr>Region</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The region of the accepter VPC of the [VPC Peering Connection]. `auto_accept` must be `false`,
and use the `aws.ec2.VpcPeeringConnectionAccepter` to manage the accepter side.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Peer<wbr>Vpc<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the VPC with which you are creating the VPC Peering Connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Requester</td>
            <td class="align-top">
                
                <code><a href="#vpcpeeringconnectionrequester">*ec2.<wbr>Vpc<wbr>Peering<wbr>Connection<wbr>Requester</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A optional configuration block that allows for [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options to be set for the VPC that requests
the peering connection (a maximum of one).
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
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the requester VPC.
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
            <td class="align-top">accepter</td>
            <td class="align-top">
                
                <code><a href="#vpcpeeringconnectionaccepter">ec2.<wbr>Vpc<wbr>Peering<wbr>Connection<wbr>Accepter?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An optional configuration block that allows for [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options to be set for the VPC that accepts
the peering connection (a maximum of one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">auto<wbr>Accept</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Accept the peering (both VPCs need to be in the same AWS account).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">peer<wbr>Owner<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS account ID of the owner of the peer VPC.
Defaults to the account ID the [AWS provider][1] is currently connected to.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">peer<wbr>Region</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The region of the accepter VPC of the [VPC Peering Connection]. `auto_accept` must be `false`,
and use the `aws.ec2.VpcPeeringConnectionAccepter` to manage the accepter side.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">peer<wbr>Vpc<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the VPC with which you are creating the VPC Peering Connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">requester</td>
            <td class="align-top">
                
                <code><a href="#vpcpeeringconnectionrequester">ec2.<wbr>Vpc<wbr>Peering<wbr>Connection<wbr>Requester?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A optional configuration block that allows for [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options to be set for the VPC that requests
the peering connection (a maximum of one).
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
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the requester VPC.
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
            <td class="align-top">accepter</td>
            <td class="align-top">
                
                <code><a href="#vpcpeeringconnectionaccepter">dict{vpc_<wbr>peering_<wbr>connection_<wbr>accepter}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An optional configuration block that allows for [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options to be set for the VPC that accepts
the peering connection (a maximum of one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">auto_<wbr>accept</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Accept the peering (both VPCs need to be in the same AWS account).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">peer_<wbr>owner_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS account ID of the owner of the peer VPC.
Defaults to the account ID the [AWS provider][1] is currently connected to.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">peer_<wbr>region</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The region of the accepter VPC of the [VPC Peering Connection]. `auto_accept` must be `false`,
and use the `aws.ec2.VpcPeeringConnectionAccepter` to manage the accepter side.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">peer_<wbr>vpc_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the VPC with which you are creating the VPC Peering Connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">requester</td>
            <td class="align-top">
                
                <code><a href="#vpcpeeringconnectionrequester">dict{vpc_<wbr>peering_<wbr>connection_<wbr>requester}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A optional configuration block that allows for [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options to be set for the VPC that requests
the peering connection (a maximum of one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>dict{any}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the requester VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## VpcPeeringConnection Output Properties

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
            <td class="align-top">Accept<wbr>Status</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The status of the VPC Peering Connection request.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Accepter</td>
            <td class="align-top">
                
                <code><a href="#vpcpeeringconnectionaccepter">Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Vpc<wbr>Peering<wbr>Connection<wbr>Accepter</a></code>
            </td>
            <td class="align-top">{{% md %}} An optional configuration block that allows for [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options to be set for the VPC that accepts
the peering connection (a maximum of one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Auto<wbr>Accept</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} Accept the peering (both VPCs need to be in the same AWS account).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Peer<wbr>Owner<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The AWS account ID of the owner of the peer VPC.
Defaults to the account ID the [AWS provider][1] is currently connected to.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Peer<wbr>Region</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The region of the accepter VPC of the [VPC Peering Connection]. `auto_accept` must be `false`,
and use the `aws.ec2.VpcPeeringConnectionAccepter` to manage the accepter side.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Peer<wbr>Vpc<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the VPC with which you are creating the VPC Peering Connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Requester</td>
            <td class="align-top">
                
                <code><a href="#vpcpeeringconnectionrequester">Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Vpc<wbr>Peering<wbr>Connection<wbr>Requester</a></code>
            </td>
            <td class="align-top">{{% md %}} A optional configuration block that allows for [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options to be set for the VPC that requests
the peering connection (a maximum of one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the requester VPC.
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
            <td class="align-top">Accept<wbr>Status</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The status of the VPC Peering Connection request.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Accepter</td>
            <td class="align-top">
                
                <code><a href="#vpcpeeringconnectionaccepter">ec2.<wbr>Vpc<wbr>Peering<wbr>Connection<wbr>Accepter</a></code>
            </td>
            <td class="align-top">{{% md %}} An optional configuration block that allows for [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options to be set for the VPC that accepts
the peering connection (a maximum of one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Auto<wbr>Accept</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} Accept the peering (both VPCs need to be in the same AWS account).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Peer<wbr>Owner<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The AWS account ID of the owner of the peer VPC.
Defaults to the account ID the [AWS provider][1] is currently connected to.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Peer<wbr>Region</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The region of the accepter VPC of the [VPC Peering Connection]. `auto_accept` must be `false`,
and use the `aws.ec2.VpcPeeringConnectionAccepter` to manage the accepter side.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Peer<wbr>Vpc<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the VPC with which you are creating the VPC Peering Connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Requester</td>
            <td class="align-top">
                
                <code><a href="#vpcpeeringconnectionrequester">ec2.<wbr>Vpc<wbr>Peering<wbr>Connection<wbr>Requester</a></code>
            </td>
            <td class="align-top">{{% md %}} A optional configuration block that allows for [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options to be set for the VPC that requests
the peering connection (a maximum of one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the requester VPC.
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
            <td class="align-top">accept<wbr>Status</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The status of the VPC Peering Connection request.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">accepter</td>
            <td class="align-top">
                
                <code><a href="#vpcpeeringconnectionaccepter">ec2.<wbr>Vpc<wbr>Peering<wbr>Connection<wbr>Accepter</a></code>
            </td>
            <td class="align-top">{{% md %}} An optional configuration block that allows for [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options to be set for the VPC that accepts
the peering connection (a maximum of one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">auto<wbr>Accept</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} Accept the peering (both VPCs need to be in the same AWS account).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">peer<wbr>Owner<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The AWS account ID of the owner of the peer VPC.
Defaults to the account ID the [AWS provider][1] is currently connected to.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">peer<wbr>Region</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The region of the accepter VPC of the [VPC Peering Connection]. `auto_accept` must be `false`,
and use the `aws.ec2.VpcPeeringConnectionAccepter` to manage the accepter side.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">peer<wbr>Vpc<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the VPC with which you are creating the VPC Peering Connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">requester</td>
            <td class="align-top">
                
                <code><a href="#vpcpeeringconnectionrequester">ec2.<wbr>Vpc<wbr>Peering<wbr>Connection<wbr>Requester</a></code>
            </td>
            <td class="align-top">{{% md %}} A optional configuration block that allows for [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options to be set for the VPC that requests
the peering connection (a maximum of one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the requester VPC.
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
            <td class="align-top">accept_<wbr>status</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The status of the VPC Peering Connection request.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">accepter</td>
            <td class="align-top">
                
                <code><a href="#vpcpeeringconnectionaccepter">dict{vpc_<wbr>peering_<wbr>connection_<wbr>accepter}</a></code>
            </td>
            <td class="align-top">{{% md %}} An optional configuration block that allows for [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options to be set for the VPC that accepts
the peering connection (a maximum of one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">auto_<wbr>accept</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Accept the peering (both VPCs need to be in the same AWS account).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">peer_<wbr>owner_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The AWS account ID of the owner of the peer VPC.
Defaults to the account ID the [AWS provider][1] is currently connected to.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">peer_<wbr>region</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The region of the accepter VPC of the [VPC Peering Connection]. `auto_accept` must be `false`,
and use the `aws.ec2.VpcPeeringConnectionAccepter` to manage the accepter side.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">peer_<wbr>vpc_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the VPC with which you are creating the VPC Peering Connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">requester</td>
            <td class="align-top">
                
                <code><a href="#vpcpeeringconnectionrequester">dict{vpc_<wbr>peering_<wbr>connection_<wbr>requester}</a></code>
            </td>
            <td class="align-top">{{% md %}} A optional configuration block that allows for [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options to be set for the VPC that requests
the peering connection (a maximum of one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>dict{any}</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the requester VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing VpcPeeringConnection Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ec2/#VpcPeeringConnectionState">VpcPeeringConnectionState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ec2/#VpcPeeringConnection">VpcPeeringConnection</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>accept_status=None<span class="p">, </span>accepter=None<span class="p">, </span>auto_accept=None<span class="p">, </span>peer_owner_id=None<span class="p">, </span>peer_region=None<span class="p">, </span>peer_vpc_id=None<span class="p">, </span>requester=None<span class="p">, </span>tags=None<span class="p">, </span>vpc_id=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetVpcPeeringConnection<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#VpcPeeringConnectionState">VpcPeeringConnectionState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#VpcPeeringConnection">VpcPeeringConnection</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.VpcPeeringConnection.html">VpcPeeringConnection</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.VpcPeeringConnectionState.html">VpcPeeringConnectionState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Get an existing VpcPeeringConnection resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
            <td class="align-top">Accept<wbr>Status</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The status of the VPC Peering Connection request.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Accepter</td>
            <td class="align-top">
                
                <code><a href="#vpcpeeringconnectionaccepter">Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Vpc<wbr>Peering<wbr>Connection<wbr>Accepter<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An optional configuration block that allows for [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options to be set for the VPC that accepts
the peering connection (a maximum of one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Auto<wbr>Accept</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Accept the peering (both VPCs need to be in the same AWS account).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Peer<wbr>Owner<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS account ID of the owner of the peer VPC.
Defaults to the account ID the [AWS provider][1] is currently connected to.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Peer<wbr>Region</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The region of the accepter VPC of the [VPC Peering Connection]. `auto_accept` must be `false`,
and use the `aws.ec2.VpcPeeringConnectionAccepter` to manage the accepter side.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Peer<wbr>Vpc<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the VPC with which you are creating the VPC Peering Connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Requester</td>
            <td class="align-top">
                
                <code><a href="#vpcpeeringconnectionrequester">Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Vpc<wbr>Peering<wbr>Connection<wbr>Requester<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A optional configuration block that allows for [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options to be set for the VPC that requests
the peering connection (a maximum of one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the requester VPC.
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
            <td class="align-top">Accept<wbr>Status</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The status of the VPC Peering Connection request.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Accepter</td>
            <td class="align-top">
                
                <code><a href="#vpcpeeringconnectionaccepter">*ec2.<wbr>Vpc<wbr>Peering<wbr>Connection<wbr>Accepter</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An optional configuration block that allows for [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options to be set for the VPC that accepts
the peering connection (a maximum of one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Auto<wbr>Accept</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Accept the peering (both VPCs need to be in the same AWS account).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Peer<wbr>Owner<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS account ID of the owner of the peer VPC.
Defaults to the account ID the [AWS provider][1] is currently connected to.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Peer<wbr>Region</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The region of the accepter VPC of the [VPC Peering Connection]. `auto_accept` must be `false`,
and use the `aws.ec2.VpcPeeringConnectionAccepter` to manage the accepter side.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Peer<wbr>Vpc<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the VPC with which you are creating the VPC Peering Connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Requester</td>
            <td class="align-top">
                
                <code><a href="#vpcpeeringconnectionrequester">*ec2.<wbr>Vpc<wbr>Peering<wbr>Connection<wbr>Requester</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A optional configuration block that allows for [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options to be set for the VPC that requests
the peering connection (a maximum of one).
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
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the requester VPC.
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
            <td class="align-top">accept<wbr>Status</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The status of the VPC Peering Connection request.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">accepter</td>
            <td class="align-top">
                
                <code><a href="#vpcpeeringconnectionaccepter">ec2.<wbr>Vpc<wbr>Peering<wbr>Connection<wbr>Accepter?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An optional configuration block that allows for [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options to be set for the VPC that accepts
the peering connection (a maximum of one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">auto<wbr>Accept</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Accept the peering (both VPCs need to be in the same AWS account).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">peer<wbr>Owner<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS account ID of the owner of the peer VPC.
Defaults to the account ID the [AWS provider][1] is currently connected to.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">peer<wbr>Region</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The region of the accepter VPC of the [VPC Peering Connection]. `auto_accept` must be `false`,
and use the `aws.ec2.VpcPeeringConnectionAccepter` to manage the accepter side.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">peer<wbr>Vpc<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the VPC with which you are creating the VPC Peering Connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">requester</td>
            <td class="align-top">
                
                <code><a href="#vpcpeeringconnectionrequester">ec2.<wbr>Vpc<wbr>Peering<wbr>Connection<wbr>Requester?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A optional configuration block that allows for [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options to be set for the VPC that requests
the peering connection (a maximum of one).
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
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the requester VPC.
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
            <td class="align-top">accept_<wbr>status</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The status of the VPC Peering Connection request.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">accepter</td>
            <td class="align-top">
                
                <code><a href="#vpcpeeringconnectionaccepter">dict{vpc_<wbr>peering_<wbr>connection_<wbr>accepter}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An optional configuration block that allows for [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options to be set for the VPC that accepts
the peering connection (a maximum of one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">auto_<wbr>accept</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Accept the peering (both VPCs need to be in the same AWS account).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">peer_<wbr>owner_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS account ID of the owner of the peer VPC.
Defaults to the account ID the [AWS provider][1] is currently connected to.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">peer_<wbr>region</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The region of the accepter VPC of the [VPC Peering Connection]. `auto_accept` must be `false`,
and use the `aws.ec2.VpcPeeringConnectionAccepter` to manage the accepter side.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">peer_<wbr>vpc_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the VPC with which you are creating the VPC Peering Connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">requester</td>
            <td class="align-top">
                
                <code><a href="#vpcpeeringconnectionrequester">dict{vpc_<wbr>peering_<wbr>connection_<wbr>requester}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A optional configuration block that allows for [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options to be set for the VPC that requests
the peering connection (a maximum of one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>dict{any}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the requester VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### VpcPeeringConnectionAccepter
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#VpcPeeringConnectionAccepter">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#VpcPeeringConnectionAccepter">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#VpcPeeringConnectionAccepterArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#VpcPeeringConnectionAccepterOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.VpcPeeringConnectionAccepterArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.VpcPeeringConnectionAccepter.html">output</a> API doc for this type.
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
            <td class="align-top">Allow<wbr>Classic<wbr>Link<wbr>To<wbr>Remote<wbr>Vpc</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Allow a local linked EC2-Classic instance to communicate
with instances in a peer VPC. This enables an outbound communication from the local ClassicLink connection
to the remote VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Allow<wbr>Remote<wbr>Vpc<wbr>Dns<wbr>Resolution</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Allow a local VPC to resolve public DNS hostnames to
private IP addresses when queried from instances in the peer VPC. This is
[not supported](https://docs.aws.amazon.com/vpc/latest/peering/modify-peering-connections.html) for
inter-region VPC peering.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Allow<wbr>Vpc<wbr>To<wbr>Remote<wbr>Classic<wbr>Link</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Allow a local VPC to communicate with a linked EC2-Classic
instance in a peer VPC. This enables an outbound communication from the local VPC to the remote ClassicLink
connection.
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
            <td class="align-top">Allow<wbr>Classic<wbr>Link<wbr>To<wbr>Remote<wbr>Vpc</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Allow a local linked EC2-Classic instance to communicate
with instances in a peer VPC. This enables an outbound communication from the local ClassicLink connection
to the remote VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Allow<wbr>Remote<wbr>Vpc<wbr>Dns<wbr>Resolution</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Allow a local VPC to resolve public DNS hostnames to
private IP addresses when queried from instances in the peer VPC. This is
[not supported](https://docs.aws.amazon.com/vpc/latest/peering/modify-peering-connections.html) for
inter-region VPC peering.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Allow<wbr>Vpc<wbr>To<wbr>Remote<wbr>Classic<wbr>Link</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Allow a local VPC to communicate with a linked EC2-Classic
instance in a peer VPC. This enables an outbound communication from the local VPC to the remote ClassicLink
connection.
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
            <td class="align-top">allow<wbr>Classic<wbr>Link<wbr>To<wbr>Remote<wbr>Vpc</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Allow a local linked EC2-Classic instance to communicate
with instances in a peer VPC. This enables an outbound communication from the local ClassicLink connection
to the remote VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">allow<wbr>Remote<wbr>Vpc<wbr>Dns<wbr>Resolution</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Allow a local VPC to resolve public DNS hostnames to
private IP addresses when queried from instances in the peer VPC. This is
[not supported](https://docs.aws.amazon.com/vpc/latest/peering/modify-peering-connections.html) for
inter-region VPC peering.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">allow<wbr>Vpc<wbr>To<wbr>Remote<wbr>Classic<wbr>Link</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Allow a local VPC to communicate with a linked EC2-Classic
instance in a peer VPC. This enables an outbound communication from the local VPC to the remote ClassicLink
connection.
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
            <td class="align-top">allow_<wbr>classic_<wbr>link_<wbr>to_<wbr>remote_<wbr>vpc</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Allow a local linked EC2-Classic instance to communicate
with instances in a peer VPC. This enables an outbound communication from the local ClassicLink connection
to the remote VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">allow_<wbr>remote_<wbr>vpc_<wbr>dns_<wbr>resolution</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Allow a local VPC to resolve public DNS hostnames to
private IP addresses when queried from instances in the peer VPC. This is
[not supported](https://docs.aws.amazon.com/vpc/latest/peering/modify-peering-connections.html) for
inter-region VPC peering.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">allow_<wbr>vpc_<wbr>to_<wbr>remote_<wbr>classic_<wbr>link</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Allow a local VPC to communicate with a linked EC2-Classic
instance in a peer VPC. This enables an outbound communication from the local VPC to the remote ClassicLink
connection.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### VpcPeeringConnectionRequester
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#VpcPeeringConnectionRequester">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#VpcPeeringConnectionRequester">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#VpcPeeringConnectionRequesterArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#VpcPeeringConnectionRequesterOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.VpcPeeringConnectionRequesterArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.VpcPeeringConnectionRequester.html">output</a> API doc for this type.
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
            <td class="align-top">Allow<wbr>Classic<wbr>Link<wbr>To<wbr>Remote<wbr>Vpc</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Allow a local linked EC2-Classic instance to communicate
with instances in a peer VPC. This enables an outbound communication from the local ClassicLink connection
to the remote VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Allow<wbr>Remote<wbr>Vpc<wbr>Dns<wbr>Resolution</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Allow a local VPC to resolve public DNS hostnames to
private IP addresses when queried from instances in the peer VPC. This is
[not supported](https://docs.aws.amazon.com/vpc/latest/peering/modify-peering-connections.html) for
inter-region VPC peering.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Allow<wbr>Vpc<wbr>To<wbr>Remote<wbr>Classic<wbr>Link</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Allow a local VPC to communicate with a linked EC2-Classic
instance in a peer VPC. This enables an outbound communication from the local VPC to the remote ClassicLink
connection.
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
            <td class="align-top">Allow<wbr>Classic<wbr>Link<wbr>To<wbr>Remote<wbr>Vpc</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Allow a local linked EC2-Classic instance to communicate
with instances in a peer VPC. This enables an outbound communication from the local ClassicLink connection
to the remote VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Allow<wbr>Remote<wbr>Vpc<wbr>Dns<wbr>Resolution</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Allow a local VPC to resolve public DNS hostnames to
private IP addresses when queried from instances in the peer VPC. This is
[not supported](https://docs.aws.amazon.com/vpc/latest/peering/modify-peering-connections.html) for
inter-region VPC peering.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Allow<wbr>Vpc<wbr>To<wbr>Remote<wbr>Classic<wbr>Link</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Allow a local VPC to communicate with a linked EC2-Classic
instance in a peer VPC. This enables an outbound communication from the local VPC to the remote ClassicLink
connection.
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
            <td class="align-top">allow<wbr>Classic<wbr>Link<wbr>To<wbr>Remote<wbr>Vpc</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Allow a local linked EC2-Classic instance to communicate
with instances in a peer VPC. This enables an outbound communication from the local ClassicLink connection
to the remote VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">allow<wbr>Remote<wbr>Vpc<wbr>Dns<wbr>Resolution</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Allow a local VPC to resolve public DNS hostnames to
private IP addresses when queried from instances in the peer VPC. This is
[not supported](https://docs.aws.amazon.com/vpc/latest/peering/modify-peering-connections.html) for
inter-region VPC peering.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">allow<wbr>Vpc<wbr>To<wbr>Remote<wbr>Classic<wbr>Link</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Allow a local VPC to communicate with a linked EC2-Classic
instance in a peer VPC. This enables an outbound communication from the local VPC to the remote ClassicLink
connection.
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
            <td class="align-top">allow_<wbr>classic_<wbr>link_<wbr>to_<wbr>remote_<wbr>vpc</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Allow a local linked EC2-Classic instance to communicate
with instances in a peer VPC. This enables an outbound communication from the local ClassicLink connection
to the remote VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">allow_<wbr>remote_<wbr>vpc_<wbr>dns_<wbr>resolution</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Allow a local VPC to resolve public DNS hostnames to
private IP addresses when queried from instances in the peer VPC. This is
[not supported](https://docs.aws.amazon.com/vpc/latest/peering/modify-peering-connections.html) for
inter-region VPC peering.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">allow_<wbr>vpc_<wbr>to_<wbr>remote_<wbr>classic_<wbr>link</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Allow a local VPC to communicate with a linked EC2-Classic
instance in a peer VPC. This enables an outbound communication from the local VPC to the remote ClassicLink
connection.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







