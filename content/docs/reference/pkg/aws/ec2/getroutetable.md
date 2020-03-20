
---
title: "GetRouteTable"
block_external_search_index: true
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>

`aws.ec2.RouteTable` provides details about a specific Route Table.

This resource can prove useful when a module accepts a Subnet id as
an input variable and needs to, for example, add a route in
the Route Table.

## Example Usage

The following example shows how one might accept a Route Table id as a variable
and use this data source to obtain the data necessary to create a route.

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const config = new pulumi.Config();
const subnetId = config.require("subnetId");

const selected = aws.ec2.getRouteTable({
    subnetId: subnetId,
});
const route = new aws.ec2.Route("route", {
    destinationCidrBlock: "10.0.1.0/22",
    routeTableId: selected.id,
    vpcPeeringConnectionId: "pcx-45ff3dc1",
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/route_table.html.markdown.





## Using GetRouteTable

{{< langchoose csharp nojavascript >}}


<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getRouteTable<span class="p">(</span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ec2/#GetRouteTableArgs">GetRouteTableArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#InvokeOptions">pulumi.InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ec2/#GetRouteTableResult">GetRouteTableResult</a></span>></span></code></pre></div>


<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_route_table(</span>filters=None<span class="p">, </span>gateway_id=None<span class="p">, </span>route_table_id=None<span class="p">, </span>subnet_id=None<span class="p">, </span>tags=None<span class="p">, </span>vpc_id=None<span class="p">, </span>opts=None<span class="p">)</span></code></pre></div>


<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupRouteTable<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#LookupRouteTableArgs">LookupRouteTableArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#InvokeOption">pulumi.InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#LookupRouteTableResult">LookupRouteTableResult</a></span>, error)</span></code></pre></div>


<div class="highlight">
<pre class="chroma">
<code class="language-csharp" data-lang="csharp"><span class="k">public static class </span><span class="nx">GetRouteTable </span><span class="p">{</span>
    <span class="k">public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.GetRouteTableResult.html">Pulumi.Aws.Ec2.GetRouteTableResult</a></span>> <span class="p">InvokeAsync(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.GetRouteTableArgs.html">GetRouteTableArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/InvokeOptions.html">InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span>
<span class="p">}</span></code></pre>
</div>



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
            <td class="align-top">Filters</td>
            <td class="align-top">
                
                <code><a href="#getroutetablefilter">List&lt;Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Get<wbr>Route<wbr>Table<wbr>Filter<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Custom filter block as described below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The id of an Internet Gateway or Virtual Private Gateway which is connected to the Route Table (not exported if not passed as a parameter).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Route<wbr>Table<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The id of the specific Route Table to retrieve.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Subnet<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The id of a Subnet which is connected to the Route Table (not exported if not passed as a parameter).
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
A mapping of tags, each pair of which must exactly match
a pair on the desired Route Table.
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
The id of the VPC that the desired Route Table belongs to.
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
            <td class="align-top">Filters</td>
            <td class="align-top">
                
                <code><a href="#getroutetablefilter">[]Get<wbr>Route<wbr>Table<wbr>Filter</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Custom filter block as described below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The id of an Internet Gateway or Virtual Private Gateway which is connected to the Route Table (not exported if not passed as a parameter).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Route<wbr>Table<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The id of the specific Route Table to retrieve.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Subnet<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The id of a Subnet which is connected to the Route Table (not exported if not passed as a parameter).
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
A mapping of tags, each pair of which must exactly match
a pair on the desired Route Table.
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
The id of the VPC that the desired Route Table belongs to.
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
            <td class="align-top">filters</td>
            <td class="align-top">
                
                <code><a href="#getroutetablefilter">ec2.<wbr>Get<wbr>Route<wbr>Table<wbr>Filter[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Custom filter block as described below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The id of an Internet Gateway or Virtual Private Gateway which is connected to the Route Table (not exported if not passed as a parameter).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">route<wbr>Table<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The id of the specific Route Table to retrieve.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">subnet<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The id of a Subnet which is connected to the Route Table (not exported if not passed as a parameter).
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
A mapping of tags, each pair of which must exactly match
a pair on the desired Route Table.
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
The id of the VPC that the desired Route Table belongs to.
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
            <td class="align-top">filters</td>
            <td class="align-top">
                
                <code><a href="#getroutetablefilter">List[Get<wbr>Route<wbr>Table<wbr>Filter]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Custom filter block as described below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">gateway_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The id of an Internet Gateway or Virtual Private Gateway which is connected to the Route Table (not exported if not passed as a parameter).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">route_<wbr>table_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The id of the specific Route Table to retrieve.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">subnet_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The id of a Subnet which is connected to the Route Table (not exported if not passed as a parameter).
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
A mapping of tags, each pair of which must exactly match
a pair on the desired Route Table.
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
The id of the VPC that the desired Route Table belongs to.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## GetRouteTable Result

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
            <td class="align-top">Associations</td>
            <td class="align-top">
                
                <code><a href="#getroutetableassociation">List&lt;Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Get<wbr>Route<wbr>Table<wbr>Association&gt;</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Filters</td>
            <td class="align-top">
                
                <code><a href="#getroutetablefilter">List&lt;Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Get<wbr>Route<wbr>Table<wbr>Filter&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Gateway ID. Only set when associated with an Internet Gateway or Virtual Private Gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} id is the provider-assigned unique ID for this managed resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Owner<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the AWS account that owns the route table
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Route<wbr>Table<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Route Table ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Routes</td>
            <td class="align-top">
                
                <code><a href="#getroutetableroute">List&lt;Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Get<wbr>Route<wbr>Table<wbr>Route&gt;</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Subnet<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Subnet ID. Only set when associated with a Subnet.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
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
            <td class="align-top">Associations</td>
            <td class="align-top">
                
                <code><a href="#getroutetableassociation">[]Get<wbr>Route<wbr>Table<wbr>Association<wbr>Type</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Filters</td>
            <td class="align-top">
                
                <code><a href="#getroutetablefilter">[]Get<wbr>Route<wbr>Table<wbr>Filter</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Gateway ID. Only set when associated with an Internet Gateway or Virtual Private Gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} id is the provider-assigned unique ID for this managed resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Owner<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the AWS account that owns the route table
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Route<wbr>Table<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Route Table ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Routes</td>
            <td class="align-top">
                
                <code><a href="#getroutetableroute">[]Get<wbr>Route<wbr>Table<wbr>Route</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Subnet<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Subnet ID. Only set when associated with a Subnet.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
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
            <td class="align-top">associations</td>
            <td class="align-top">
                
                <code><a href="#getroutetableassociation">ec2.<wbr>Get<wbr>Route<wbr>Table<wbr>Association[]</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">filters</td>
            <td class="align-top">
                
                <code><a href="#getroutetablefilter">ec2.<wbr>Get<wbr>Route<wbr>Table<wbr>Filter[]?</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Gateway ID. Only set when associated with an Internet Gateway or Virtual Private Gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} id is the provider-assigned unique ID for this managed resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">owner<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the AWS account that owns the route table
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">route<wbr>Table<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Route Table ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">routes</td>
            <td class="align-top">
                
                <code><a href="#getroutetableroute">ec2.<wbr>Get<wbr>Route<wbr>Table<wbr>Route[]</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">subnet<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Subnet ID. Only set when associated with a Subnet.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>{[key: string]: any}</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
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
            <td class="align-top">associations</td>
            <td class="align-top">
                
                <code><a href="#getroutetableassociation">List[Get<wbr>Route<wbr>Table<wbr>Association]</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">filters</td>
            <td class="align-top">
                
                <code><a href="#getroutetablefilter">List[Get<wbr>Route<wbr>Table<wbr>Filter]</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">gateway_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The Gateway ID. Only set when associated with an Internet Gateway or Virtual Private Gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} id is the provider-assigned unique ID for this managed resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">owner_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the AWS account that owns the route table
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">route_<wbr>table_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The Route Table ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">routes</td>
            <td class="align-top">
                
                <code><a href="#getroutetableroute">List[Get<wbr>Route<wbr>Table<wbr>Route]</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">subnet_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The Subnet ID. Only set when associated with a Subnet.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Supporting Types

#### GetRouteTableAssociation
{{% lang nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GetRouteTableAssociation">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#GetRouteTableAssociationType">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the   <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.GetRouteTableAssociation.html">output</a> API doc for this type.
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
            <td class="align-top">Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The id of an Internet Gateway or Virtual Private Gateway which is connected to the Route Table (not exported if not passed as a parameter).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Main</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
If the Association due to the Main Route Table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Route<wbr>Table<wbr>Association<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Association ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Route<wbr>Table<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The id of the specific Route Table to retrieve.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Subnet<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The id of a Subnet which is connected to the Route Table (not exported if not passed as a parameter).
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
            <td class="align-top">Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The id of an Internet Gateway or Virtual Private Gateway which is connected to the Route Table (not exported if not passed as a parameter).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Main</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
If the Association due to the Main Route Table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Route<wbr>Table<wbr>Association<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Association ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Route<wbr>Table<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The id of the specific Route Table to retrieve.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Subnet<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The id of a Subnet which is connected to the Route Table (not exported if not passed as a parameter).
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
            <td class="align-top">gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The id of an Internet Gateway or Virtual Private Gateway which is connected to the Route Table (not exported if not passed as a parameter).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">main</td>
            <td class="align-top">
                
                <code>boolean</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
If the Association due to the Main Route Table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">route<wbr>Table<wbr>Association<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Association ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">route<wbr>Table<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The id of the specific Route Table to retrieve.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">subnet<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The id of a Subnet which is connected to the Route Table (not exported if not passed as a parameter).
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
            <td class="align-top">gateway_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The id of an Internet Gateway or Virtual Private Gateway which is connected to the Route Table (not exported if not passed as a parameter).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">main</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
If the Association due to the Main Route Table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">route<wbr>Table<wbr>Association<wbr>Id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Association ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">route_<wbr>table_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The id of the specific Route Table to retrieve.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">subnet_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The id of a Subnet which is connected to the Route Table (not exported if not passed as a parameter).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### GetRouteTableFilter
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#GetRouteTableFilter">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GetRouteTableFilter">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#GetRouteTableFilterArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#GetRouteTableFilter">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.GetRouteTableFilterArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.GetRouteTableFilter.html">output</a> API doc for this type.
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
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the field to filter by, as defined by
[the underlying AWS API](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeRouteTables.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Values</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Set of values that are accepted for the given field.
A Route Table will be selected if any one of the given values matches.
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
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the field to filter by, as defined by
[the underlying AWS API](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeRouteTables.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Values</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Set of values that are accepted for the given field.
A Route Table will be selected if any one of the given values matches.
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
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the field to filter by, as defined by
[the underlying AWS API](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeRouteTables.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">values</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Set of values that are accepted for the given field.
A Route Table will be selected if any one of the given values matches.
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
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the field to filter by, as defined by
[the underlying AWS API](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeRouteTables.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">values</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Set of values that are accepted for the given field.
A Route Table will be selected if any one of the given values matches.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### GetRouteTableRoute
{{% lang nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GetRouteTableRoute">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#GetRouteTableRoute">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the   <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.GetRouteTableRoute.html">output</a> API doc for this type.
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
            <td class="align-top">Cidr<wbr>Block</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The CIDR block of the route.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Egress<wbr>Only<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the Egress Only Internet Gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The id of an Internet Gateway or Virtual Private Gateway which is connected to the Route Table (not exported if not passed as a parameter).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The EC2 instance ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ipv6Cidr<wbr>Block</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The IPv6 CIDR block of the route.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Nat<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The NAT Gateway ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Network<wbr>Interface<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the elastic network interface (eni) to use.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Transit<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The EC2 Transit Gateway ID.
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
The VPC Peering ID.
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
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The CIDR block of the route.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Egress<wbr>Only<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the Egress Only Internet Gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The id of an Internet Gateway or Virtual Private Gateway which is connected to the Route Table (not exported if not passed as a parameter).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The EC2 instance ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ipv6Cidr<wbr>Block</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The IPv6 CIDR block of the route.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Nat<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The NAT Gateway ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Network<wbr>Interface<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the elastic network interface (eni) to use.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Transit<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The EC2 Transit Gateway ID.
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
The VPC Peering ID.
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
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The CIDR block of the route.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">egress<wbr>Only<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the Egress Only Internet Gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The id of an Internet Gateway or Virtual Private Gateway which is connected to the Route Table (not exported if not passed as a parameter).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The EC2 instance ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ipv6Cidr<wbr>Block</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The IPv6 CIDR block of the route.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">nat<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The NAT Gateway ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">network<wbr>Interface<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the elastic network interface (eni) to use.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">transit<wbr>Gateway<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The EC2 Transit Gateway ID.
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
The VPC Peering ID.
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
 (Required)
The CIDR block of the route.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">egress_<wbr>only_<wbr>gateway_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the Egress Only Internet Gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">gateway_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The id of an Internet Gateway or Virtual Private Gateway which is connected to the Route Table (not exported if not passed as a parameter).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The EC2 instance ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ipv6_<wbr>cidr_<wbr>block</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The IPv6 CIDR block of the route.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">nat_<wbr>gateway_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The NAT Gateway ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">network_<wbr>interface_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the elastic network interface (eni) to use.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">transit_<wbr>gateway_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The EC2 Transit Gateway ID.
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
The VPC Peering ID.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







