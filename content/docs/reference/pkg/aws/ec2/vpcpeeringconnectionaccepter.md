
---
title: "VpcPeeringConnectionAccepter"
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>


Provides a resource to manage the accepter's side of a VPC Peering Connection.

When a cross-account (requester's AWS account differs from the accepter's AWS account) or an inter-region
VPC Peering Connection is created, a VPC Peering Connection resource is automatically created in the
accepter's account.
The requester can use the `aws.ec2.VpcPeeringConnection` resource to manage its side of the connection
and the accepter can use the `aws.ec2.VpcPeeringConnectionAccepter` resource to "adopt" its side of the
connection into management.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const peer = new aws.Provider("peer", {
    region: "us-west-2",
});
const main = new aws.ec2.Vpc("main", {
    cidrBlock: "10.0.0.0/16",
});
const peerVpc = new aws.ec2.Vpc("peer", {
    cidrBlock: "10.1.0.0/16",
}, {provider: peer});
const peerCallerIdentity = aws.getCallerIdentity({provider: peer});
// Requester's side of the connection.
const peerVpcPeeringConnection = new aws.ec2.VpcPeeringConnection("peer", {
    autoAccept: false,
    peerOwnerId: peerCallerIdentity.accountId,
    peerRegion: "us-west-2",
    peerVpcId: peerVpc.id,
    tags: {
        Side: "Requester",
    },
    vpcId: main.id,
});
// Accepter's side of the connection.
const peerVpcPeeringConnectionAccepter = new aws.ec2.VpcPeeringConnectionAccepter("peer", {
    autoAccept: true,
    tags: {
        Side: "Accepter",
    },
    vpcPeeringConnectionId: peerVpcPeeringConnection.id,
}, {provider: peer});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/vpc_peering_connection_accepter.html.markdown.



## Create a VpcPeeringConnectionAccepter Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ec2/#VpcPeeringConnectionAccepter">VpcPeeringConnectionAccepter</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ec2/#VpcPeeringConnectionAccepterArgs">VpcPeeringConnectionAccepterArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">VpcPeeringConnectionAccepter</span><span class="p">(resource_name, opts=None, </span>accepter=None<span class="p">, </span>auto_accept=None<span class="p">, </span>requester=None<span class="p">, </span>tags=None<span class="p">, </span>vpc_peering_connection_id=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewVpcPeeringConnectionAccepter<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#VpcPeeringConnectionAccepterArgs">VpcPeeringConnectionAccepterArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#VpcPeeringConnectionAccepter">VpcPeeringConnectionAccepter</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.VpcPeeringConnectionAccepter.html">VpcPeeringConnectionAccepter</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.VpcPeeringConnectionAccepterArgs.html">VpcPeeringConnectionAccepterArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a VpcPeeringConnectionAccepter resource with the given unique name, arguments, and options.

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
                
                <code><a href="#vpcpeeringconnectionaccepteraccepter">Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Vpc<wbr>Peering<wbr>Connection<wbr>Accepter<wbr>Accepter<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A configuration block that describes [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options set for the accepter VPC.
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
Whether or not to accept the peering request. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Requester</td>
            <td class="align-top">
                
                <code><a href="#vpcpeeringconnectionaccepterrequester">Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Vpc<wbr>Peering<wbr>Connection<wbr>Accepter<wbr>Requester<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A configuration block that describes [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options set for the requester VPC.
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
            <td class="align-top">Vpc<wbr>Peering<wbr>Connection<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The VPC Peering Connection ID to manage.
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
                
                <code><a href="#vpcpeeringconnectionaccepteraccepter">*ec2.<wbr>Vpc<wbr>Peering<wbr>Connection<wbr>Accepter<wbr>Accepter</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A configuration block that describes [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options set for the accepter VPC.
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
Whether or not to accept the peering request. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Requester</td>
            <td class="align-top">
                
                <code><a href="#vpcpeeringconnectionaccepterrequester">*ec2.<wbr>Vpc<wbr>Peering<wbr>Connection<wbr>Accepter<wbr>Requester</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A configuration block that describes [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options set for the requester VPC.
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
            <td class="align-top">Vpc<wbr>Peering<wbr>Connection<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The VPC Peering Connection ID to manage.
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
                
                <code><a href="#vpcpeeringconnectionaccepteraccepter">ec2.<wbr>Vpc<wbr>Peering<wbr>Connection<wbr>Accepter<wbr>Accepter?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A configuration block that describes [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options set for the accepter VPC.
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
Whether or not to accept the peering request. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">requester</td>
            <td class="align-top">
                
                <code><a href="#vpcpeeringconnectionaccepterrequester">ec2.<wbr>Vpc<wbr>Peering<wbr>Connection<wbr>Accepter<wbr>Requester?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A configuration block that describes [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options set for the requester VPC.
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
            <td class="align-top">vpc<wbr>Peering<wbr>Connection<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The VPC Peering Connection ID to manage.
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
                
                <code><a href="#vpcpeeringconnectionaccepteraccepter">Dict[vpc_<wbr>peering_<wbr>connection_<wbr>accepter_<wbr>accepter]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A configuration block that describes [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options set for the accepter VPC.
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
Whether or not to accept the peering request. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">requester</td>
            <td class="align-top">
                
                <code><a href="#vpcpeeringconnectionaccepterrequester">Dict[vpc_<wbr>peering_<wbr>connection_<wbr>accepter_<wbr>requester]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A configuration block that describes [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options set for the requester VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[Any, Any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc_<wbr>peering_<wbr>connection_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The VPC Peering Connection ID to manage.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## VpcPeeringConnectionAccepter Output Properties

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
                
                <code><a href="#vpcpeeringconnectionaccepteraccepter">Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Vpc<wbr>Peering<wbr>Connection<wbr>Accepter<wbr>Accepter</a></code>
            </td>
            <td class="align-top">{{% md %}} A configuration block that describes [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options set for the accepter VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Auto<wbr>Accept</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} Whether or not to accept the peering request. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Peer<wbr>Owner<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The AWS account ID of the owner of the requester VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Peer<wbr>Region</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The region of the accepter VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Peer<wbr>Vpc<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the requester VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Requester</td>
            <td class="align-top">
                
                <code><a href="#vpcpeeringconnectionaccepterrequester">Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Vpc<wbr>Peering<wbr>Connection<wbr>Accepter<wbr>Requester</a></code>
            </td>
            <td class="align-top">{{% md %}} A configuration block that describes [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options set for the requester VPC.
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
            <td class="align-top">{{% md %}} The ID of the accepter VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Peering<wbr>Connection<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The VPC Peering Connection ID to manage.
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
                
                <code><a href="#vpcpeeringconnectionaccepteraccepter">ec2.<wbr>Vpc<wbr>Peering<wbr>Connection<wbr>Accepter<wbr>Accepter</a></code>
            </td>
            <td class="align-top">{{% md %}} A configuration block that describes [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options set for the accepter VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Auto<wbr>Accept</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether or not to accept the peering request. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Peer<wbr>Owner<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The AWS account ID of the owner of the requester VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Peer<wbr>Region</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The region of the accepter VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Peer<wbr>Vpc<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the requester VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Requester</td>
            <td class="align-top">
                
                <code><a href="#vpcpeeringconnectionaccepterrequester">ec2.<wbr>Vpc<wbr>Peering<wbr>Connection<wbr>Accepter<wbr>Requester</a></code>
            </td>
            <td class="align-top">{{% md %}} A configuration block that describes [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options set for the requester VPC.
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
            <td class="align-top">{{% md %}} The ID of the accepter VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Peering<wbr>Connection<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The VPC Peering Connection ID to manage.
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
                
                <code><a href="#vpcpeeringconnectionaccepteraccepter">ec2.<wbr>Vpc<wbr>Peering<wbr>Connection<wbr>Accepter<wbr>Accepter</a></code>
            </td>
            <td class="align-top">{{% md %}} A configuration block that describes [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options set for the accepter VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">auto<wbr>Accept</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} Whether or not to accept the peering request. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">peer<wbr>Owner<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The AWS account ID of the owner of the requester VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">peer<wbr>Region</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The region of the accepter VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">peer<wbr>Vpc<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the requester VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">requester</td>
            <td class="align-top">
                
                <code><a href="#vpcpeeringconnectionaccepterrequester">ec2.<wbr>Vpc<wbr>Peering<wbr>Connection<wbr>Accepter<wbr>Requester</a></code>
            </td>
            <td class="align-top">{{% md %}} A configuration block that describes [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options set for the requester VPC.
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
            <td class="align-top">{{% md %}} The ID of the accepter VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc<wbr>Peering<wbr>Connection<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The VPC Peering Connection ID to manage.
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
                
                <code><a href="#vpcpeeringconnectionaccepteraccepter">Dict[vpc_<wbr>peering_<wbr>connection_<wbr>accepter_<wbr>accepter]</a></code>
            </td>
            <td class="align-top">{{% md %}} A configuration block that describes [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options set for the accepter VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">auto_<wbr>accept</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether or not to accept the peering request. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">peer_<wbr>owner_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The AWS account ID of the owner of the requester VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">peer_<wbr>region</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The region of the accepter VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">peer_<wbr>vpc_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the requester VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">requester</td>
            <td class="align-top">
                
                <code><a href="#vpcpeeringconnectionaccepterrequester">Dict[vpc_<wbr>peering_<wbr>connection_<wbr>accepter_<wbr>requester]</a></code>
            </td>
            <td class="align-top">{{% md %}} A configuration block that describes [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options set for the requester VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[Any, Any]</code>
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
            <td class="align-top">{{% md %}} The ID of the accepter VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc_<wbr>peering_<wbr>connection_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The VPC Peering Connection ID to manage.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing VpcPeeringConnectionAccepter Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ec2/#VpcPeeringConnectionAccepterState">VpcPeeringConnectionAccepterState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ec2/#VpcPeeringConnectionAccepter">VpcPeeringConnectionAccepter</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>accept_status=None<span class="p">, </span>accepter=None<span class="p">, </span>auto_accept=None<span class="p">, </span>peer_owner_id=None<span class="p">, </span>peer_region=None<span class="p">, </span>peer_vpc_id=None<span class="p">, </span>requester=None<span class="p">, </span>tags=None<span class="p">, </span>vpc_id=None<span class="p">, </span>vpc_peering_connection_id=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetVpcPeeringConnectionAccepter<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#VpcPeeringConnectionAccepterState">VpcPeeringConnectionAccepterState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#VpcPeeringConnectionAccepter">VpcPeeringConnectionAccepter</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.VpcPeeringConnectionAccepter.html">VpcPeeringConnectionAccepter</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.VpcPeeringConnectionAccepterState.html">VpcPeeringConnectionAccepterState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Get an existing VpcPeeringConnectionAccepter resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
                
                <code><a href="#vpcpeeringconnectionaccepteraccepter">Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Vpc<wbr>Peering<wbr>Connection<wbr>Accepter<wbr>Accepter<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A configuration block that describes [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options set for the accepter VPC.
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
Whether or not to accept the peering request. Defaults to `false`.
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
The AWS account ID of the owner of the requester VPC.
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
The region of the accepter VPC.
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
The ID of the requester VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Requester</td>
            <td class="align-top">
                
                <code><a href="#vpcpeeringconnectionaccepterrequester">Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Vpc<wbr>Peering<wbr>Connection<wbr>Accepter<wbr>Requester<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A configuration block that describes [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options set for the requester VPC.
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
The ID of the accepter VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Peering<wbr>Connection<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The VPC Peering Connection ID to manage.
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
                
                <code><a href="#vpcpeeringconnectionaccepteraccepter">*ec2.<wbr>Vpc<wbr>Peering<wbr>Connection<wbr>Accepter<wbr>Accepter</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A configuration block that describes [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options set for the accepter VPC.
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
Whether or not to accept the peering request. Defaults to `false`.
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
The AWS account ID of the owner of the requester VPC.
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
The region of the accepter VPC.
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
The ID of the requester VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Requester</td>
            <td class="align-top">
                
                <code><a href="#vpcpeeringconnectionaccepterrequester">*ec2.<wbr>Vpc<wbr>Peering<wbr>Connection<wbr>Accepter<wbr>Requester</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A configuration block that describes [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options set for the requester VPC.
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
The ID of the accepter VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Peering<wbr>Connection<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The VPC Peering Connection ID to manage.
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
                
                <code><a href="#vpcpeeringconnectionaccepteraccepter">ec2.<wbr>Vpc<wbr>Peering<wbr>Connection<wbr>Accepter<wbr>Accepter?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A configuration block that describes [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options set for the accepter VPC.
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
Whether or not to accept the peering request. Defaults to `false`.
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
The AWS account ID of the owner of the requester VPC.
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
The region of the accepter VPC.
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
The ID of the requester VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">requester</td>
            <td class="align-top">
                
                <code><a href="#vpcpeeringconnectionaccepterrequester">ec2.<wbr>Vpc<wbr>Peering<wbr>Connection<wbr>Accepter<wbr>Requester?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A configuration block that describes [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options set for the requester VPC.
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
The ID of the accepter VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc<wbr>Peering<wbr>Connection<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The VPC Peering Connection ID to manage.
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
                
                <code><a href="#vpcpeeringconnectionaccepteraccepter">Dict[vpc_<wbr>peering_<wbr>connection_<wbr>accepter_<wbr>accepter]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A configuration block that describes [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options set for the accepter VPC.
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
Whether or not to accept the peering request. Defaults to `false`.
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
The AWS account ID of the owner of the requester VPC.
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
The region of the accepter VPC.
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
The ID of the requester VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">requester</td>
            <td class="align-top">
                
                <code><a href="#vpcpeeringconnectionaccepterrequester">Dict[vpc_<wbr>peering_<wbr>connection_<wbr>accepter_<wbr>requester]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A configuration block that describes [VPC Peering Connection]
(http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide) options set for the requester VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[Any, Any]</code>
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
The ID of the accepter VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc_<wbr>peering_<wbr>connection_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The VPC Peering Connection ID to manage.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### VpcPeeringConnectionAccepterAccepter
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#VpcPeeringConnectionAccepterAccepter">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#VpcPeeringConnectionAccepterAccepter">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#VpcPeeringConnectionAccepterAccepterArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#VpcPeeringConnectionAccepterAccepterOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.VpcPeeringConnectionAccepterAccepterArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.VpcPeeringConnectionAccepterAccepter.html">output</a> API doc for this type.
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
Indicates whether a local ClassicLink connection can communicate
with the peer VPC over the VPC Peering Connection.
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
Indicates whether a local VPC can resolve public DNS hostnames to
private IP addresses when queried from instances in a peer VPC.
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
Indicates whether a local VPC can communicate with a ClassicLink
connection in the peer VPC over the VPC Peering Connection.
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
Indicates whether a local ClassicLink connection can communicate
with the peer VPC over the VPC Peering Connection.
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
Indicates whether a local VPC can resolve public DNS hostnames to
private IP addresses when queried from instances in a peer VPC.
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
Indicates whether a local VPC can communicate with a ClassicLink
connection in the peer VPC over the VPC Peering Connection.
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
Indicates whether a local ClassicLink connection can communicate
with the peer VPC over the VPC Peering Connection.
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
Indicates whether a local VPC can resolve public DNS hostnames to
private IP addresses when queried from instances in a peer VPC.
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
Indicates whether a local VPC can communicate with a ClassicLink
connection in the peer VPC over the VPC Peering Connection.
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
Indicates whether a local ClassicLink connection can communicate
with the peer VPC over the VPC Peering Connection.
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
Indicates whether a local VPC can resolve public DNS hostnames to
private IP addresses when queried from instances in a peer VPC.
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
Indicates whether a local VPC can communicate with a ClassicLink
connection in the peer VPC over the VPC Peering Connection.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### VpcPeeringConnectionAccepterRequester
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#VpcPeeringConnectionAccepterRequester">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#VpcPeeringConnectionAccepterRequester">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#VpcPeeringConnectionAccepterRequesterArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#VpcPeeringConnectionAccepterRequesterOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.VpcPeeringConnectionAccepterRequesterArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.VpcPeeringConnectionAccepterRequester.html">output</a> API doc for this type.
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
Indicates whether a local ClassicLink connection can communicate
with the peer VPC over the VPC Peering Connection.
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
Indicates whether a local VPC can resolve public DNS hostnames to
private IP addresses when queried from instances in a peer VPC.
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
Indicates whether a local VPC can communicate with a ClassicLink
connection in the peer VPC over the VPC Peering Connection.
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
Indicates whether a local ClassicLink connection can communicate
with the peer VPC over the VPC Peering Connection.
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
Indicates whether a local VPC can resolve public DNS hostnames to
private IP addresses when queried from instances in a peer VPC.
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
Indicates whether a local VPC can communicate with a ClassicLink
connection in the peer VPC over the VPC Peering Connection.
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
Indicates whether a local ClassicLink connection can communicate
with the peer VPC over the VPC Peering Connection.
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
Indicates whether a local VPC can resolve public DNS hostnames to
private IP addresses when queried from instances in a peer VPC.
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
Indicates whether a local VPC can communicate with a ClassicLink
connection in the peer VPC over the VPC Peering Connection.
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
Indicates whether a local ClassicLink connection can communicate
with the peer VPC over the VPC Peering Connection.
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
Indicates whether a local VPC can resolve public DNS hostnames to
private IP addresses when queried from instances in a peer VPC.
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
Indicates whether a local VPC can communicate with a ClassicLink
connection in the peer VPC over the VPC Peering Connection.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







