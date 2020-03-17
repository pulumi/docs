
---
title: "NetworkAcl"
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>


Provides an network ACL resource. You might set up network ACLs with rules similar
to your security groups in order to add an additional layer of security to your VPC.

> **NOTE on Network ACLs and Network ACL Rules:** This provider currently
provides both a standalone Network ACL Rule resource and a Network ACL resource with rules
defined in-line. At this time you cannot use a Network ACL with in-line rules
in conjunction with any Network ACL Rule resources. Doing so will cause
a conflict of rule settings and will overwrite rules.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const main = new aws.ec2.NetworkAcl("main", {
    egress: [{
        action: "allow",
        cidrBlock: "10.3.0.0/18",
        fromPort: 443,
        protocol: "tcp",
        ruleNo: 200,
        toPort: 443,
    }],
    ingress: [{
        action: "allow",
        cidrBlock: "10.3.0.0/18",
        fromPort: 80,
        protocol: "tcp",
        ruleNo: 100,
        toPort: 80,
    }],
    tags: {
        Name: "main",
    },
    vpcId: aws_vpc_main.id,
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/network_acl.html.markdown.



## Create a NetworkAcl Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ec2/#NetworkAcl">NetworkAcl</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ec2/#NetworkAclArgs">NetworkAclArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">NetworkAcl</span><span class="p">(resource_name, opts=None, </span>egress=None<span class="p">, </span>ingress=None<span class="p">, </span>subnet_ids=None<span class="p">, </span>tags=None<span class="p">, </span>vpc_id=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewNetworkAcl<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#NetworkAclArgs">NetworkAclArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#NetworkAcl">NetworkAcl</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.NetworkAcl.html">NetworkAcl</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.NetworkAclArgs.html">NetworkAclArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a NetworkAcl resource with the given unique name, arguments, and options.

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
            <td class="align-top">Egress</td>
            <td class="align-top">
                
                <code><a href="#networkaclegress">List&lt;Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Network<wbr>Acl<wbr>Egress<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies an egress rule. Parameters defined below.
This argument is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ingress</td>
            <td class="align-top">
                
                <code><a href="#networkaclingress">List&lt;Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Network<wbr>Acl<wbr>Ingress<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies an ingress rule. Parameters defined below.
This argument is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Subnet<wbr>Ids</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of Subnet IDs to apply the ACL to
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
The ID of the associated VPC.
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
            <td class="align-top">Egress</td>
            <td class="align-top">
                
                <code><a href="#networkaclegress">[]ec2.<wbr>Network<wbr>Acl<wbr>Egress</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies an egress rule. Parameters defined below.
This argument is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ingress</td>
            <td class="align-top">
                
                <code><a href="#networkaclingress">[]ec2.<wbr>Network<wbr>Acl<wbr>Ingress</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies an ingress rule. Parameters defined below.
This argument is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Subnet<wbr>Ids</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of Subnet IDs to apply the ACL to
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
The ID of the associated VPC.
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
            <td class="align-top">egress</td>
            <td class="align-top">
                
                <code><a href="#networkaclegress">ec2.<wbr>Network<wbr>Acl<wbr>Egress[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies an egress rule. Parameters defined below.
This argument is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ingress</td>
            <td class="align-top">
                
                <code><a href="#networkaclingress">ec2.<wbr>Network<wbr>Acl<wbr>Ingress[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies an ingress rule. Parameters defined below.
This argument is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">subnet<wbr>Ids</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of Subnet IDs to apply the ACL to
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
The ID of the associated VPC.
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
            <td class="align-top">egress</td>
            <td class="align-top">
                
                <code><a href="#networkaclegress">List[network_<wbr>acl_<wbr>egress]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies an egress rule. Parameters defined below.
This argument is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ingress</td>
            <td class="align-top">
                
                <code><a href="#networkaclingress">List[network_<wbr>acl_<wbr>ingress]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies an ingress rule. Parameters defined below.
This argument is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">subnet_<wbr>ids</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of Subnet IDs to apply the ACL to
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
 (Required)
The ID of the associated VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## NetworkAcl Output Properties

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
            <td class="align-top">Egress</td>
            <td class="align-top">
                
                <code><a href="#networkaclegress">List&lt;Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Network<wbr>Acl<wbr>Egress&gt;</a></code>
            </td>
            <td class="align-top">{{% md %}} Specifies an egress rule. Parameters defined below.
This argument is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ingress</td>
            <td class="align-top">
                
                <code><a href="#networkaclingress">List&lt;Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Network<wbr>Acl<wbr>Ingress&gt;</a></code>
            </td>
            <td class="align-top">{{% md %}} Specifies an ingress rule. Parameters defined below.
This argument is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Owner<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the AWS account that owns the network ACL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Subnet<wbr>Ids</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} A list of Subnet IDs to apply the ACL to
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
            <td class="align-top">{{% md %}} The ID of the associated VPC.
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
            <td class="align-top">Egress</td>
            <td class="align-top">
                
                <code><a href="#networkaclegress">[]ec2.<wbr>Network<wbr>Acl<wbr>Egress</a></code>
            </td>
            <td class="align-top">{{% md %}} Specifies an egress rule. Parameters defined below.
This argument is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ingress</td>
            <td class="align-top">
                
                <code><a href="#networkaclingress">[]ec2.<wbr>Network<wbr>Acl<wbr>Ingress</a></code>
            </td>
            <td class="align-top">{{% md %}} Specifies an ingress rule. Parameters defined below.
This argument is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Owner<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the AWS account that owns the network ACL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Subnet<wbr>Ids</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} A list of Subnet IDs to apply the ACL to
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
            <td class="align-top">{{% md %}} The ID of the associated VPC.
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
            <td class="align-top">egress</td>
            <td class="align-top">
                
                <code><a href="#networkaclegress">ec2.<wbr>Network<wbr>Acl<wbr>Egress[]</a></code>
            </td>
            <td class="align-top">{{% md %}} Specifies an egress rule. Parameters defined below.
This argument is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ingress</td>
            <td class="align-top">
                
                <code><a href="#networkaclingress">ec2.<wbr>Network<wbr>Acl<wbr>Ingress[]</a></code>
            </td>
            <td class="align-top">{{% md %}} Specifies an ingress rule. Parameters defined below.
This argument is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">owner<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the AWS account that owns the network ACL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">subnet<wbr>Ids</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} A list of Subnet IDs to apply the ACL to
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
            <td class="align-top">{{% md %}} The ID of the associated VPC.
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
            <td class="align-top">egress</td>
            <td class="align-top">
                
                <code><a href="#networkaclegress">List[network_<wbr>acl_<wbr>egress]</a></code>
            </td>
            <td class="align-top">{{% md %}} Specifies an egress rule. Parameters defined below.
This argument is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ingress</td>
            <td class="align-top">
                
                <code><a href="#networkaclingress">List[network_<wbr>acl_<wbr>ingress]</a></code>
            </td>
            <td class="align-top">{{% md %}} Specifies an ingress rule. Parameters defined below.
This argument is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">owner_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the AWS account that owns the network ACL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">subnet_<wbr>ids</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} A list of Subnet IDs to apply the ACL to
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
            <td class="align-top">{{% md %}} The ID of the associated VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing NetworkAcl Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ec2/#NetworkAclState">NetworkAclState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ec2/#NetworkAcl">NetworkAcl</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>egress=None<span class="p">, </span>ingress=None<span class="p">, </span>owner_id=None<span class="p">, </span>subnet_ids=None<span class="p">, </span>tags=None<span class="p">, </span>vpc_id=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetNetworkAcl<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#NetworkAclState">NetworkAclState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#NetworkAcl">NetworkAcl</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.NetworkAcl.html">NetworkAcl</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.NetworkAclState.html">NetworkAclState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Get an existing NetworkAcl resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
            <td class="align-top">Egress</td>
            <td class="align-top">
                
                <code><a href="#networkaclegress">List&lt;Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Network<wbr>Acl<wbr>Egress<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies an egress rule. Parameters defined below.
This argument is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ingress</td>
            <td class="align-top">
                
                <code><a href="#networkaclingress">List&lt;Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Network<wbr>Acl<wbr>Ingress<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies an ingress rule. Parameters defined below.
This argument is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Owner<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the AWS account that owns the network ACL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Subnet<wbr>Ids</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of Subnet IDs to apply the ACL to
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
The ID of the associated VPC.
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
            <td class="align-top">Egress</td>
            <td class="align-top">
                
                <code><a href="#networkaclegress">[]ec2.<wbr>Network<wbr>Acl<wbr>Egress</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies an egress rule. Parameters defined below.
This argument is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ingress</td>
            <td class="align-top">
                
                <code><a href="#networkaclingress">[]ec2.<wbr>Network<wbr>Acl<wbr>Ingress</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies an ingress rule. Parameters defined below.
This argument is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Owner<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the AWS account that owns the network ACL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Subnet<wbr>Ids</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of Subnet IDs to apply the ACL to
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
The ID of the associated VPC.
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
            <td class="align-top">egress</td>
            <td class="align-top">
                
                <code><a href="#networkaclegress">ec2.<wbr>Network<wbr>Acl<wbr>Egress[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies an egress rule. Parameters defined below.
This argument is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ingress</td>
            <td class="align-top">
                
                <code><a href="#networkaclingress">ec2.<wbr>Network<wbr>Acl<wbr>Ingress[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies an ingress rule. Parameters defined below.
This argument is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">owner<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the AWS account that owns the network ACL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">subnet<wbr>Ids</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of Subnet IDs to apply the ACL to
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
The ID of the associated VPC.
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
            <td class="align-top">egress</td>
            <td class="align-top">
                
                <code><a href="#networkaclegress">List[network_<wbr>acl_<wbr>egress]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies an egress rule. Parameters defined below.
This argument is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ingress</td>
            <td class="align-top">
                
                <code><a href="#networkaclingress">List[network_<wbr>acl_<wbr>ingress]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies an ingress rule. Parameters defined below.
This argument is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">owner_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the AWS account that owns the network ACL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">subnet_<wbr>ids</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of Subnet IDs to apply the ACL to
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
The ID of the associated VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### NetworkAclEgress
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#NetworkAclEgress">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#NetworkAclEgress">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#NetworkAclEgressArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#NetworkAclEgressOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.NetworkAclEgressArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.NetworkAclEgress.html">output</a> API doc for this type.
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
            <td class="align-top">Action</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The action to take.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cidr<wbr>Block</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CIDR block to match. This must be a
valid network mask.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">From<wbr>Port</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The from port to match.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Icmp<wbr>Code</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ICMP type code to be used. Default 0.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Icmp<wbr>Type</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ICMP type to be used. Default 0.
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
The IPv6 CIDR block.
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
The protocol to match. If using the -1 &#39;all&#39;
protocol, you must specify a from and to port of 0.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rule<wbr>No</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The rule number. Used for ordering.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">To<wbr>Port</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
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
            <td class="align-top">Action</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The action to take.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cidr<wbr>Block</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CIDR block to match. This must be a
valid network mask.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">From<wbr>Port</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The from port to match.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Icmp<wbr>Code</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ICMP type code to be used. Default 0.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Icmp<wbr>Type</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ICMP type to be used. Default 0.
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
The IPv6 CIDR block.
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
The protocol to match. If using the -1 &#39;all&#39;
protocol, you must specify a from and to port of 0.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rule<wbr>No</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The rule number. Used for ordering.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">To<wbr>Port</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
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
            <td class="align-top">action</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The action to take.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cidr<wbr>Block</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CIDR block to match. This must be a
valid network mask.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">from<wbr>Port</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The from port to match.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">icmp<wbr>Code</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ICMP type code to be used. Default 0.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">icmp<wbr>Type</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ICMP type to be used. Default 0.
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
The IPv6 CIDR block.
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
The protocol to match. If using the -1 &#39;all&#39;
protocol, you must specify a from and to port of 0.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rule<wbr>No</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The rule number. Used for ordering.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">to<wbr>Port</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
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
            <td class="align-top">action</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The action to take.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cidr_<wbr>block</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CIDR block to match. This must be a
valid network mask.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">from_<wbr>port</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The from port to match.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">icmp_<wbr>code</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ICMP type code to be used. Default 0.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">icmp_<wbr>type</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ICMP type to be used. Default 0.
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
The IPv6 CIDR block.
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
The protocol to match. If using the -1 &#39;all&#39;
protocol, you must specify a from and to port of 0.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rule_<wbr>no</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The rule number. Used for ordering.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">to_<wbr>port</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The to port to match.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### NetworkAclIngress
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#NetworkAclIngress">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#NetworkAclIngress">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#NetworkAclIngressArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#NetworkAclIngressOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.NetworkAclIngressArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.NetworkAclIngress.html">output</a> API doc for this type.
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
            <td class="align-top">Action</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The action to take.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cidr<wbr>Block</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CIDR block to match. This must be a
valid network mask.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">From<wbr>Port</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The from port to match.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Icmp<wbr>Code</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ICMP type code to be used. Default 0.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Icmp<wbr>Type</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ICMP type to be used. Default 0.
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
The IPv6 CIDR block.
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
The protocol to match. If using the -1 &#39;all&#39;
protocol, you must specify a from and to port of 0.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rule<wbr>No</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The rule number. Used for ordering.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">To<wbr>Port</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
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
            <td class="align-top">Action</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The action to take.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cidr<wbr>Block</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CIDR block to match. This must be a
valid network mask.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">From<wbr>Port</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The from port to match.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Icmp<wbr>Code</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ICMP type code to be used. Default 0.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Icmp<wbr>Type</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ICMP type to be used. Default 0.
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
The IPv6 CIDR block.
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
The protocol to match. If using the -1 &#39;all&#39;
protocol, you must specify a from and to port of 0.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rule<wbr>No</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The rule number. Used for ordering.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">To<wbr>Port</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
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
            <td class="align-top">action</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The action to take.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cidr<wbr>Block</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CIDR block to match. This must be a
valid network mask.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">from<wbr>Port</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The from port to match.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">icmp<wbr>Code</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ICMP type code to be used. Default 0.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">icmp<wbr>Type</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ICMP type to be used. Default 0.
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
The IPv6 CIDR block.
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
The protocol to match. If using the -1 &#39;all&#39;
protocol, you must specify a from and to port of 0.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rule<wbr>No</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The rule number. Used for ordering.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">to<wbr>Port</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
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
            <td class="align-top">action</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The action to take.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cidr_<wbr>block</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CIDR block to match. This must be a
valid network mask.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">from_<wbr>port</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The from port to match.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">icmp_<wbr>code</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ICMP type code to be used. Default 0.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">icmp_<wbr>type</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ICMP type to be used. Default 0.
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
The IPv6 CIDR block.
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
The protocol to match. If using the -1 &#39;all&#39;
protocol, you must specify a from and to port of 0.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rule_<wbr>no</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The rule number. Used for ordering.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">to_<wbr>port</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The to port to match.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







