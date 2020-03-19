
---
title: "Vpc"
block_external_search_index: true
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>

Provides a VPC resource.

## Example Usage

Basic usage:

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const main = new aws.ec2.Vpc("main", {
    cidrBlock: "10.0.0.0/16",
});
```

Basic usage with tags:

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const main = new aws.ec2.Vpc("main", {
    cidrBlock: "10.0.0.0/16",
    instanceTenancy: "dedicated",
    tags: {
        Name: "main",
    },
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/vpc.html.markdown.



## Create a Vpc Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ec2/#Vpc">Vpc</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ec2/#VpcArgs">VpcArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Vpc</span><span class="p">(resource_name, opts=None, </span>assign_generated_ipv6_cidr_block=None<span class="p">, </span>cidr_block=None<span class="p">, </span>enable_classiclink=None<span class="p">, </span>enable_classiclink_dns_support=None<span class="p">, </span>enable_dns_hostnames=None<span class="p">, </span>enable_dns_support=None<span class="p">, </span>instance_tenancy=None<span class="p">, </span>tags=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewVpc<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#VpcArgs">VpcArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#Vpc">Vpc</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.Vpc.html">Vpc</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.VpcArgs.html">VpcArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a Vpc resource with the given unique name, arguments, and options.

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
            <td class="align-top">Assign<wbr>Generated<wbr>Ipv6Cidr<wbr>Block</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Requests an Amazon-provided IPv6 CIDR
block with a /56 prefix length for the VPC. You cannot specify the range of IP addresses, or
the size of the CIDR block. Default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cidr<wbr>Block</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The CIDR block for the VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enable<wbr>Classiclink</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A boolean flag to enable/disable ClassicLink
for the VPC. Only valid in regions and accounts that support EC2 Classic.
See the [ClassicLink documentation][1] for more information. Defaults false.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enable<wbr>Classiclink<wbr>Dns<wbr>Support</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A boolean flag to enable/disable ClassicLink DNS Support for the VPC.
Only valid in regions and accounts that support EC2 Classic.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enable<wbr>Dns<wbr>Hostnames</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A boolean flag to enable/disable DNS hostnames in the VPC. Defaults false.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enable<wbr>Dns<wbr>Support</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A boolean flag to enable/disable DNS support in the VPC. Defaults true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Tenancy</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A tenancy option for instances launched into the VPC
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
            <td class="align-top">Assign<wbr>Generated<wbr>Ipv6Cidr<wbr>Block</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Requests an Amazon-provided IPv6 CIDR
block with a /56 prefix length for the VPC. You cannot specify the range of IP addresses, or
the size of the CIDR block. Default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cidr<wbr>Block</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The CIDR block for the VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enable<wbr>Classiclink</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A boolean flag to enable/disable ClassicLink
for the VPC. Only valid in regions and accounts that support EC2 Classic.
See the [ClassicLink documentation][1] for more information. Defaults false.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enable<wbr>Classiclink<wbr>Dns<wbr>Support</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A boolean flag to enable/disable ClassicLink DNS Support for the VPC.
Only valid in regions and accounts that support EC2 Classic.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enable<wbr>Dns<wbr>Hostnames</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A boolean flag to enable/disable DNS hostnames in the VPC. Defaults false.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enable<wbr>Dns<wbr>Support</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A boolean flag to enable/disable DNS support in the VPC. Defaults true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Tenancy</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A tenancy option for instances launched into the VPC
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
            <td class="align-top">assign<wbr>Generated<wbr>Ipv6Cidr<wbr>Block</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Requests an Amazon-provided IPv6 CIDR
block with a /56 prefix length for the VPC. You cannot specify the range of IP addresses, or
the size of the CIDR block. Default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cidr<wbr>Block</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The CIDR block for the VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enable<wbr>Classiclink</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A boolean flag to enable/disable ClassicLink
for the VPC. Only valid in regions and accounts that support EC2 Classic.
See the [ClassicLink documentation][1] for more information. Defaults false.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enable<wbr>Classiclink<wbr>Dns<wbr>Support</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A boolean flag to enable/disable ClassicLink DNS Support for the VPC.
Only valid in regions and accounts that support EC2 Classic.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enable<wbr>Dns<wbr>Hostnames</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A boolean flag to enable/disable DNS hostnames in the VPC. Defaults false.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enable<wbr>Dns<wbr>Support</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A boolean flag to enable/disable DNS support in the VPC. Defaults true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance<wbr>Tenancy</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A tenancy option for instances launched into the VPC
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
            <td class="align-top">assign_<wbr>generated_<wbr>ipv6_<wbr>cidr_<wbr>block</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Requests an Amazon-provided IPv6 CIDR
block with a /56 prefix length for the VPC. You cannot specify the range of IP addresses, or
the size of the CIDR block. Default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cidr_<wbr>block</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The CIDR block for the VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enable_<wbr>classiclink</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A boolean flag to enable/disable ClassicLink
for the VPC. Only valid in regions and accounts that support EC2 Classic.
See the [ClassicLink documentation][1] for more information. Defaults false.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enable_<wbr>classiclink_<wbr>dns_<wbr>support</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A boolean flag to enable/disable ClassicLink DNS Support for the VPC.
Only valid in regions and accounts that support EC2 Classic.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enable_<wbr>dns_<wbr>hostnames</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A boolean flag to enable/disable DNS hostnames in the VPC. Defaults false.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enable_<wbr>dns_<wbr>support</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A boolean flag to enable/disable DNS support in the VPC. Defaults true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance_<wbr>tenancy</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A tenancy option for instances launched into the VPC
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
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## Vpc Output Properties

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
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) of VPC
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Assign<wbr>Generated<wbr>Ipv6Cidr<wbr>Block</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} Requests an Amazon-provided IPv6 CIDR
block with a /56 prefix length for the VPC. You cannot specify the range of IP addresses, or
the size of the CIDR block. Default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cidr<wbr>Block</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The CIDR block for the VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Network<wbr>Acl<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the network ACL created by default on VPC creation
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Route<wbr>Table<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the route table created by default on VPC creation
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Security<wbr>Group<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the security group created by default on VPC creation
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dhcp<wbr>Options<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enable<wbr>Classiclink</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} A boolean flag to enable/disable ClassicLink
for the VPC. Only valid in regions and accounts that support EC2 Classic.
See the [ClassicLink documentation][1] for more information. Defaults false.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enable<wbr>Classiclink<wbr>Dns<wbr>Support</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} A boolean flag to enable/disable ClassicLink DNS Support for the VPC.
Only valid in regions and accounts that support EC2 Classic.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enable<wbr>Dns<wbr>Hostnames</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} A boolean flag to enable/disable DNS hostnames in the VPC. Defaults false.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enable<wbr>Dns<wbr>Support</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} A boolean flag to enable/disable DNS support in the VPC. Defaults true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Tenancy</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} A tenancy option for instances launched into the VPC
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ipv6Association<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The association ID for the IPv6 CIDR block.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ipv6Cidr<wbr>Block</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The IPv6 CIDR block.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Main<wbr>Route<wbr>Table<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the main route table associated with
this VPC. Note that you can change a VPC&#39;s main route table by using an
[`aws.ec2.MainRouteTableAssociation`](https://www.terraform.io/docs/providers/aws/r/main_route_table_association.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Owner<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the AWS account that owns the VPC.
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
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) of VPC
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Assign<wbr>Generated<wbr>Ipv6Cidr<wbr>Block</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} Requests an Amazon-provided IPv6 CIDR
block with a /56 prefix length for the VPC. You cannot specify the range of IP addresses, or
the size of the CIDR block. Default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cidr<wbr>Block</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The CIDR block for the VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Network<wbr>Acl<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the network ACL created by default on VPC creation
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Route<wbr>Table<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the route table created by default on VPC creation
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Security<wbr>Group<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the security group created by default on VPC creation
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dhcp<wbr>Options<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enable<wbr>Classiclink</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} A boolean flag to enable/disable ClassicLink
for the VPC. Only valid in regions and accounts that support EC2 Classic.
See the [ClassicLink documentation][1] for more information. Defaults false.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enable<wbr>Classiclink<wbr>Dns<wbr>Support</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} A boolean flag to enable/disable ClassicLink DNS Support for the VPC.
Only valid in regions and accounts that support EC2 Classic.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enable<wbr>Dns<wbr>Hostnames</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} A boolean flag to enable/disable DNS hostnames in the VPC. Defaults false.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enable<wbr>Dns<wbr>Support</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} A boolean flag to enable/disable DNS support in the VPC. Defaults true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Tenancy</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} A tenancy option for instances launched into the VPC
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ipv6Association<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The association ID for the IPv6 CIDR block.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ipv6Cidr<wbr>Block</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The IPv6 CIDR block.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Main<wbr>Route<wbr>Table<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the main route table associated with
this VPC. Note that you can change a VPC&#39;s main route table by using an
[`aws.ec2.MainRouteTableAssociation`](https://www.terraform.io/docs/providers/aws/r/main_route_table_association.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Owner<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the AWS account that owns the VPC.
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
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) of VPC
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">assign<wbr>Generated<wbr>Ipv6Cidr<wbr>Block</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} Requests an Amazon-provided IPv6 CIDR
block with a /56 prefix length for the VPC. You cannot specify the range of IP addresses, or
the size of the CIDR block. Default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cidr<wbr>Block</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The CIDR block for the VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default<wbr>Network<wbr>Acl<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the network ACL created by default on VPC creation
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default<wbr>Route<wbr>Table<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the route table created by default on VPC creation
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default<wbr>Security<wbr>Group<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the security group created by default on VPC creation
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dhcp<wbr>Options<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enable<wbr>Classiclink</td>
            <td class="align-top">
                
                <code>boolean</code>
            </td>
            <td class="align-top">{{% md %}} A boolean flag to enable/disable ClassicLink
for the VPC. Only valid in regions and accounts that support EC2 Classic.
See the [ClassicLink documentation][1] for more information. Defaults false.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enable<wbr>Classiclink<wbr>Dns<wbr>Support</td>
            <td class="align-top">
                
                <code>boolean</code>
            </td>
            <td class="align-top">{{% md %}} A boolean flag to enable/disable ClassicLink DNS Support for the VPC.
Only valid in regions and accounts that support EC2 Classic.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enable<wbr>Dns<wbr>Hostnames</td>
            <td class="align-top">
                
                <code>boolean</code>
            </td>
            <td class="align-top">{{% md %}} A boolean flag to enable/disable DNS hostnames in the VPC. Defaults false.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enable<wbr>Dns<wbr>Support</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} A boolean flag to enable/disable DNS support in the VPC. Defaults true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance<wbr>Tenancy</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} A tenancy option for instances launched into the VPC
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ipv6Association<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The association ID for the IPv6 CIDR block.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ipv6Cidr<wbr>Block</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The IPv6 CIDR block.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">main<wbr>Route<wbr>Table<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the main route table associated with
this VPC. Note that you can change a VPC&#39;s main route table by using an
[`aws.ec2.MainRouteTableAssociation`](https://www.terraform.io/docs/providers/aws/r/main_route_table_association.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">owner<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the AWS account that owns the VPC.
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
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) of VPC
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">assign_<wbr>generated_<wbr>ipv6_<wbr>cidr_<wbr>block</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Requests an Amazon-provided IPv6 CIDR
block with a /56 prefix length for the VPC. You cannot specify the range of IP addresses, or
the size of the CIDR block. Default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cidr_<wbr>block</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The CIDR block for the VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default_<wbr>network_<wbr>acl_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the network ACL created by default on VPC creation
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default_<wbr>route_<wbr>table_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the route table created by default on VPC creation
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default_<wbr>security_<wbr>group_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the security group created by default on VPC creation
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dhcp_<wbr>options_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enable_<wbr>classiclink</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} A boolean flag to enable/disable ClassicLink
for the VPC. Only valid in regions and accounts that support EC2 Classic.
See the [ClassicLink documentation][1] for more information. Defaults false.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enable_<wbr>classiclink_<wbr>dns_<wbr>support</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} A boolean flag to enable/disable ClassicLink DNS Support for the VPC.
Only valid in regions and accounts that support EC2 Classic.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enable_<wbr>dns_<wbr>hostnames</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} A boolean flag to enable/disable DNS hostnames in the VPC. Defaults false.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enable_<wbr>dns_<wbr>support</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} A boolean flag to enable/disable DNS support in the VPC. Defaults true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance_<wbr>tenancy</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} A tenancy option for instances launched into the VPC
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ipv6_<wbr>association_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The association ID for the IPv6 CIDR block.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ipv6_<wbr>cidr_<wbr>block</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The IPv6 CIDR block.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">main_<wbr>route_<wbr>table_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the main route table associated with
this VPC. Note that you can change a VPC&#39;s main route table by using an
[`aws.ec2.MainRouteTableAssociation`](https://www.terraform.io/docs/providers/aws/r/main_route_table_association.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">owner_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the AWS account that owns the VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing Vpc Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ec2/#VpcState">VpcState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ec2/#Vpc">Vpc</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>arn=None<span class="p">, </span>assign_generated_ipv6_cidr_block=None<span class="p">, </span>cidr_block=None<span class="p">, </span>default_network_acl_id=None<span class="p">, </span>default_route_table_id=None<span class="p">, </span>default_security_group_id=None<span class="p">, </span>dhcp_options_id=None<span class="p">, </span>enable_classiclink=None<span class="p">, </span>enable_classiclink_dns_support=None<span class="p">, </span>enable_dns_hostnames=None<span class="p">, </span>enable_dns_support=None<span class="p">, </span>instance_tenancy=None<span class="p">, </span>ipv6_association_id=None<span class="p">, </span>ipv6_cidr_block=None<span class="p">, </span>main_route_table_id=None<span class="p">, </span>owner_id=None<span class="p">, </span>tags=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetVpc<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#VpcState">VpcState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#Vpc">Vpc</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.Vpc.html">Vpc</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.VpcState.html">VpcState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Get an existing Vpc resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) of VPC
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Assign<wbr>Generated<wbr>Ipv6Cidr<wbr>Block</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Requests an Amazon-provided IPv6 CIDR
block with a /56 prefix length for the VPC. You cannot specify the range of IP addresses, or
the size of the CIDR block. Default is `false`.
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
The CIDR block for the VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Network<wbr>Acl<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the network ACL created by default on VPC creation
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Route<wbr>Table<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the route table created by default on VPC creation
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Security<wbr>Group<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the security group created by default on VPC creation
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dhcp<wbr>Options<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enable<wbr>Classiclink</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A boolean flag to enable/disable ClassicLink
for the VPC. Only valid in regions and accounts that support EC2 Classic.
See the [ClassicLink documentation][1] for more information. Defaults false.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enable<wbr>Classiclink<wbr>Dns<wbr>Support</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A boolean flag to enable/disable ClassicLink DNS Support for the VPC.
Only valid in regions and accounts that support EC2 Classic.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enable<wbr>Dns<wbr>Hostnames</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A boolean flag to enable/disable DNS hostnames in the VPC. Defaults false.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enable<wbr>Dns<wbr>Support</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A boolean flag to enable/disable DNS support in the VPC. Defaults true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Tenancy</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A tenancy option for instances launched into the VPC
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ipv6Association<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The association ID for the IPv6 CIDR block.
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
            <td class="align-top">Main<wbr>Route<wbr>Table<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the main route table associated with
this VPC. Note that you can change a VPC&#39;s main route table by using an
[`aws.ec2.MainRouteTableAssociation`](https://www.terraform.io/docs/providers/aws/r/main_route_table_association.html).
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
The ID of the AWS account that owns the VPC.
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
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) of VPC
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Assign<wbr>Generated<wbr>Ipv6Cidr<wbr>Block</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Requests an Amazon-provided IPv6 CIDR
block with a /56 prefix length for the VPC. You cannot specify the range of IP addresses, or
the size of the CIDR block. Default is `false`.
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
The CIDR block for the VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Network<wbr>Acl<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the network ACL created by default on VPC creation
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Route<wbr>Table<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the route table created by default on VPC creation
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Security<wbr>Group<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the security group created by default on VPC creation
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dhcp<wbr>Options<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enable<wbr>Classiclink</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A boolean flag to enable/disable ClassicLink
for the VPC. Only valid in regions and accounts that support EC2 Classic.
See the [ClassicLink documentation][1] for more information. Defaults false.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enable<wbr>Classiclink<wbr>Dns<wbr>Support</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A boolean flag to enable/disable ClassicLink DNS Support for the VPC.
Only valid in regions and accounts that support EC2 Classic.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enable<wbr>Dns<wbr>Hostnames</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A boolean flag to enable/disable DNS hostnames in the VPC. Defaults false.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enable<wbr>Dns<wbr>Support</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A boolean flag to enable/disable DNS support in the VPC. Defaults true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Tenancy</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A tenancy option for instances launched into the VPC
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ipv6Association<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The association ID for the IPv6 CIDR block.
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
            <td class="align-top">Main<wbr>Route<wbr>Table<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the main route table associated with
this VPC. Note that you can change a VPC&#39;s main route table by using an
[`aws.ec2.MainRouteTableAssociation`](https://www.terraform.io/docs/providers/aws/r/main_route_table_association.html).
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
The ID of the AWS account that owns the VPC.
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
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) of VPC
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">assign<wbr>Generated<wbr>Ipv6Cidr<wbr>Block</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Requests an Amazon-provided IPv6 CIDR
block with a /56 prefix length for the VPC. You cannot specify the range of IP addresses, or
the size of the CIDR block. Default is `false`.
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
The CIDR block for the VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default<wbr>Network<wbr>Acl<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the network ACL created by default on VPC creation
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default<wbr>Route<wbr>Table<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the route table created by default on VPC creation
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default<wbr>Security<wbr>Group<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the security group created by default on VPC creation
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dhcp<wbr>Options<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enable<wbr>Classiclink</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A boolean flag to enable/disable ClassicLink
for the VPC. Only valid in regions and accounts that support EC2 Classic.
See the [ClassicLink documentation][1] for more information. Defaults false.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enable<wbr>Classiclink<wbr>Dns<wbr>Support</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A boolean flag to enable/disable ClassicLink DNS Support for the VPC.
Only valid in regions and accounts that support EC2 Classic.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enable<wbr>Dns<wbr>Hostnames</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A boolean flag to enable/disable DNS hostnames in the VPC. Defaults false.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enable<wbr>Dns<wbr>Support</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A boolean flag to enable/disable DNS support in the VPC. Defaults true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance<wbr>Tenancy</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A tenancy option for instances launched into the VPC
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ipv6Association<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The association ID for the IPv6 CIDR block.
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
            <td class="align-top">main<wbr>Route<wbr>Table<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the main route table associated with
this VPC. Note that you can change a VPC&#39;s main route table by using an
[`aws.ec2.MainRouteTableAssociation`](https://www.terraform.io/docs/providers/aws/r/main_route_table_association.html).
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
The ID of the AWS account that owns the VPC.
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
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) of VPC
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">assign_<wbr>generated_<wbr>ipv6_<wbr>cidr_<wbr>block</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Requests an Amazon-provided IPv6 CIDR
block with a /56 prefix length for the VPC. You cannot specify the range of IP addresses, or
the size of the CIDR block. Default is `false`.
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
The CIDR block for the VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default_<wbr>network_<wbr>acl_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the network ACL created by default on VPC creation
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default_<wbr>route_<wbr>table_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the route table created by default on VPC creation
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default_<wbr>security_<wbr>group_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the security group created by default on VPC creation
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dhcp_<wbr>options_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enable_<wbr>classiclink</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A boolean flag to enable/disable ClassicLink
for the VPC. Only valid in regions and accounts that support EC2 Classic.
See the [ClassicLink documentation][1] for more information. Defaults false.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enable_<wbr>classiclink_<wbr>dns_<wbr>support</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A boolean flag to enable/disable ClassicLink DNS Support for the VPC.
Only valid in regions and accounts that support EC2 Classic.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enable_<wbr>dns_<wbr>hostnames</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A boolean flag to enable/disable DNS hostnames in the VPC. Defaults false.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enable_<wbr>dns_<wbr>support</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A boolean flag to enable/disable DNS support in the VPC. Defaults true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance_<wbr>tenancy</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A tenancy option for instances launched into the VPC
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ipv6_<wbr>association_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The association ID for the IPv6 CIDR block.
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
            <td class="align-top">main_<wbr>route_<wbr>table_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the main route table associated with
this VPC. Note that you can change a VPC&#39;s main route table by using an
[`aws.ec2.MainRouteTableAssociation`](https://www.terraform.io/docs/providers/aws/r/main_route_table_association.html).
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
The ID of the AWS account that owns the VPC.
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
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}









