
---
title: "Zone"
block_external_search_index: true
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>

Manages a Route53 Hosted Zone.

## Example Usage

### Public Zone

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const primary = new aws.route53.Zone("primary", {});
```

### Public Subdomain Zone

For use in subdomains, note that you need to create a
`aws.route53.Record` of type `NS` as well as the subdomain
zone.

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const main = new aws.route53.Zone("main", {});
const dev = new aws.route53.Zone("dev", {
    tags: {
        Environment: "dev",
    },
});
const dev_ns = new aws.route53.Record("dev-ns", {
    name: "dev.example.com",
    records: [
        dev.nameServers[0],
        dev.nameServers[1],
        dev.nameServers[2],
        dev.nameServers[3],
    ],
    ttl: 30,
    type: "NS",
    zoneId: main.zoneId,
});
```

### Private Zone

> **NOTE:** This provider provides both exclusive VPC associations defined in-line in this resource via `vpc` configuration blocks and a separate [Zone VPC Association](https://www.terraform.io/docs/providers/aws/r/route53_zone_association.html) resource. At this time, you cannot use in-line VPC associations in conjunction with any `aws.route53.ZoneAssociation` resources with the same zone ID otherwise it will cause a perpetual difference in plan output. You can optionally use the generic this provider resource [lifecycle configuration block](https://www.terraform.io/docs/configuration/resources.html#lifecycle) with `ignore_changes` to manage additional associations via the `aws.route53.ZoneAssociation` resource.

> **NOTE:** Private zones require at least one VPC association at all times.

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const privateZone = new aws.route53.Zone("private", {
    vpcs: [{
        vpcId: aws_vpc_example.id,
    }],
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/route53_zone.html.markdown.



## Create a Zone Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/route53/#Zone">Zone</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/route53/#ZoneArgs">ZoneArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Zone</span><span class="p">(resource_name, opts=None, </span>comment=None<span class="p">, </span>delegation_set_id=None<span class="p">, </span>force_destroy=None<span class="p">, </span>name=None<span class="p">, </span>tags=None<span class="p">, </span>vpcs=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewZone<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/route53?tab=doc#ZoneArgs">ZoneArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/route53?tab=doc#Zone">Zone</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Route53.Zone.html">Zone</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Route53.ZoneArgs.html">ZoneArgs</a></span>? <span class="nx">args = null<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a Zone resource with the given unique name, arguments, and options.

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
            <td class="align-top">Comment</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A comment for the hosted zone. Defaults to &#39;Managed by Pulumi&#39;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Delegation<wbr>Set<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the reusable delegation set whose NS records you want to assign to the hosted zone. Conflicts with `vpc` as delegation sets can only be used for public zones.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Force<wbr>Destroy</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to destroy all records (possibly managed outside of this provider) in the zone when destroying the zone.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
This is the name of the hosted zone.
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
A mapping of tags to assign to the zone.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpcs</td>
            <td class="align-top">
                
                <code><a href="#zonevpc">List&lt;Pulumi.<wbr>Aws.<wbr>Route53.<wbr>Zone<wbr>Vpc<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block(s) specifying VPC(s) to associate with a private hosted zone. Conflicts with the `delegation_set_id` argument in this resource and any [`aws.route53.ZoneAssociation` resource](https://www.terraform.io/docs/providers/aws/r/route53_zone_association.html) specifying the same zone ID. Detailed below.
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
            <td class="align-top">Comment</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A comment for the hosted zone. Defaults to &#39;Managed by Pulumi&#39;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Delegation<wbr>Set<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the reusable delegation set whose NS records you want to assign to the hosted zone. Conflicts with `vpc` as delegation sets can only be used for public zones.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Force<wbr>Destroy</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to destroy all records (possibly managed outside of this provider) in the zone when destroying the zone.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
This is the name of the hosted zone.
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
A mapping of tags to assign to the zone.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpcs</td>
            <td class="align-top">
                
                <code><a href="#zonevpc">[]Zone<wbr>Vpc</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block(s) specifying VPC(s) to associate with a private hosted zone. Conflicts with the `delegation_set_id` argument in this resource and any [`aws.route53.ZoneAssociation` resource](https://www.terraform.io/docs/providers/aws/r/route53_zone_association.html) specifying the same zone ID. Detailed below.
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
            <td class="align-top">comment</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A comment for the hosted zone. Defaults to &#39;Managed by Pulumi&#39;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">delegation<wbr>Set<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the reusable delegation set whose NS records you want to assign to the hosted zone. Conflicts with `vpc` as delegation sets can only be used for public zones.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">force<wbr>Destroy</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to destroy all records (possibly managed outside of this provider) in the zone when destroying the zone.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
This is the name of the hosted zone.
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
A mapping of tags to assign to the zone.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpcs</td>
            <td class="align-top">
                
                <code><a href="#zonevpc">route53.<wbr>Zone<wbr>Vpc[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block(s) specifying VPC(s) to associate with a private hosted zone. Conflicts with the `delegation_set_id` argument in this resource and any [`aws.route53.ZoneAssociation` resource](https://www.terraform.io/docs/providers/aws/r/route53_zone_association.html) specifying the same zone ID. Detailed below.
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
            <td class="align-top">comment</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A comment for the hosted zone. Defaults to &#39;Managed by Pulumi&#39;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">delegation_<wbr>set_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the reusable delegation set whose NS records you want to assign to the hosted zone. Conflicts with `vpc` as delegation sets can only be used for public zones.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">force_<wbr>destroy</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to destroy all records (possibly managed outside of this provider) in the zone when destroying the zone.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
This is the name of the hosted zone.
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
A mapping of tags to assign to the zone.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpcs</td>
            <td class="align-top">
                
                <code><a href="#zonevpc">List[Zone<wbr>Vpc]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block(s) specifying VPC(s) to associate with a private hosted zone. Conflicts with the `delegation_set_id` argument in this resource and any [`aws.route53.ZoneAssociation` resource](https://www.terraform.io/docs/providers/aws/r/route53_zone_association.html) specifying the same zone ID. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## Zone Output Properties

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
            <td class="align-top">Comment</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A comment for the hosted zone. Defaults to &#39;Managed by Pulumi&#39;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Delegation<wbr>Set<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the reusable delegation set whose NS records you want to assign to the hosted zone. Conflicts with `vpc` as delegation sets can only be used for public zones.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Force<wbr>Destroy</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} Whether to destroy all records (possibly managed outside of this provider) in the zone when destroying the zone.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} This is the name of the hosted zone.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name<wbr>Servers</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} A list of name servers in associated (or default) delegation set.
Find more about delegation sets in [AWS docs](https://docs.aws.amazon.com/Route53/latest/APIReference/actions-on-reusable-delegation-sets.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the zone.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpcs</td>
            <td class="align-top">
                
                <code><a href="#zonevpc">List&lt;Pulumi.<wbr>Aws.<wbr>Route53.<wbr>Zone<wbr>Vpc&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block(s) specifying VPC(s) to associate with a private hosted zone. Conflicts with the `delegation_set_id` argument in this resource and any [`aws.route53.ZoneAssociation` resource](https://www.terraform.io/docs/providers/aws/r/route53_zone_association.html) specifying the same zone ID. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Zone<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Hosted Zone ID. This can be referenced by zone records.
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
            <td class="align-top">Comment</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A comment for the hosted zone. Defaults to &#39;Managed by Pulumi&#39;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Delegation<wbr>Set<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the reusable delegation set whose NS records you want to assign to the hosted zone. Conflicts with `vpc` as delegation sets can only be used for public zones.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Force<wbr>Destroy</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether to destroy all records (possibly managed outside of this provider) in the zone when destroying the zone.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} This is the name of the hosted zone.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name<wbr>Servers</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} A list of name servers in associated (or default) delegation set.
Find more about delegation sets in [AWS docs](https://docs.aws.amazon.com/Route53/latest/APIReference/actions-on-reusable-delegation-sets.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the zone.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpcs</td>
            <td class="align-top">
                
                <code><a href="#zonevpc">[]Zone<wbr>Vpc</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block(s) specifying VPC(s) to associate with a private hosted zone. Conflicts with the `delegation_set_id` argument in this resource and any [`aws.route53.ZoneAssociation` resource](https://www.terraform.io/docs/providers/aws/r/route53_zone_association.html) specifying the same zone ID. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Zone<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Hosted Zone ID. This can be referenced by zone records.
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
            <td class="align-top">comment</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A comment for the hosted zone. Defaults to &#39;Managed by Pulumi&#39;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">delegation<wbr>Set<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the reusable delegation set whose NS records you want to assign to the hosted zone. Conflicts with `vpc` as delegation sets can only be used for public zones.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">force<wbr>Destroy</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} Whether to destroy all records (possibly managed outside of this provider) in the zone when destroying the zone.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} This is the name of the hosted zone.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name<wbr>Servers</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} A list of name servers in associated (or default) delegation set.
Find more about delegation sets in [AWS docs](https://docs.aws.amazon.com/Route53/latest/APIReference/actions-on-reusable-delegation-sets.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the zone.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpcs</td>
            <td class="align-top">
                
                <code><a href="#zonevpc">route53.<wbr>Zone<wbr>Vpc[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block(s) specifying VPC(s) to associate with a private hosted zone. Conflicts with the `delegation_set_id` argument in this resource and any [`aws.route53.ZoneAssociation` resource](https://www.terraform.io/docs/providers/aws/r/route53_zone_association.html) specifying the same zone ID. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">zone<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Hosted Zone ID. This can be referenced by zone records.
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
            <td class="align-top">comment</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} A comment for the hosted zone. Defaults to &#39;Managed by Pulumi&#39;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">delegation_<wbr>set_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the reusable delegation set whose NS records you want to assign to the hosted zone. Conflicts with `vpc` as delegation sets can only be used for public zones.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">force_<wbr>destroy</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether to destroy all records (possibly managed outside of this provider) in the zone when destroying the zone.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} This is the name of the hosted zone.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name_<wbr>servers</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} A list of name servers in associated (or default) delegation set.
Find more about delegation sets in [AWS docs](https://docs.aws.amazon.com/Route53/latest/APIReference/actions-on-reusable-delegation-sets.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the zone.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpcs</td>
            <td class="align-top">
                
                <code><a href="#zonevpc">List[Zone<wbr>Vpc]</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block(s) specifying VPC(s) to associate with a private hosted zone. Conflicts with the `delegation_set_id` argument in this resource and any [`aws.route53.ZoneAssociation` resource](https://www.terraform.io/docs/providers/aws/r/route53_zone_association.html) specifying the same zone ID. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">zone_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The Hosted Zone ID. This can be referenced by zone records.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing Zone Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/route53/#ZoneState">ZoneState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/route53/#Zone">Zone</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>comment=None<span class="p">, </span>delegation_set_id=None<span class="p">, </span>force_destroy=None<span class="p">, </span>name=None<span class="p">, </span>name_servers=None<span class="p">, </span>tags=None<span class="p">, </span>vpcs=None<span class="p">, </span>zone_id=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetZone<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/route53?tab=doc#ZoneState">ZoneState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/route53?tab=doc#Zone">Zone</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Route53.Zone.html">Zone</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Route53.ZoneState.html">ZoneState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Get an existing Zone resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
            <td class="align-top">Comment</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A comment for the hosted zone. Defaults to &#39;Managed by Pulumi&#39;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Delegation<wbr>Set<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the reusable delegation set whose NS records you want to assign to the hosted zone. Conflicts with `vpc` as delegation sets can only be used for public zones.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Force<wbr>Destroy</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to destroy all records (possibly managed outside of this provider) in the zone when destroying the zone.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
This is the name of the hosted zone.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name<wbr>Servers</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of name servers in associated (or default) delegation set.
Find more about delegation sets in [AWS docs](https://docs.aws.amazon.com/Route53/latest/APIReference/actions-on-reusable-delegation-sets.html).
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
A mapping of tags to assign to the zone.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpcs</td>
            <td class="align-top">
                
                <code><a href="#zonevpc">List&lt;Pulumi.<wbr>Aws.<wbr>Route53.<wbr>Zone<wbr>Vpc<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block(s) specifying VPC(s) to associate with a private hosted zone. Conflicts with the `delegation_set_id` argument in this resource and any [`aws.route53.ZoneAssociation` resource](https://www.terraform.io/docs/providers/aws/r/route53_zone_association.html) specifying the same zone ID. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Zone<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Hosted Zone ID. This can be referenced by zone records.
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
            <td class="align-top">Comment</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A comment for the hosted zone. Defaults to &#39;Managed by Pulumi&#39;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Delegation<wbr>Set<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the reusable delegation set whose NS records you want to assign to the hosted zone. Conflicts with `vpc` as delegation sets can only be used for public zones.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Force<wbr>Destroy</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to destroy all records (possibly managed outside of this provider) in the zone when destroying the zone.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
This is the name of the hosted zone.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name<wbr>Servers</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of name servers in associated (or default) delegation set.
Find more about delegation sets in [AWS docs](https://docs.aws.amazon.com/Route53/latest/APIReference/actions-on-reusable-delegation-sets.html).
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
A mapping of tags to assign to the zone.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpcs</td>
            <td class="align-top">
                
                <code><a href="#zonevpc">[]Zone<wbr>Vpc</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block(s) specifying VPC(s) to associate with a private hosted zone. Conflicts with the `delegation_set_id` argument in this resource and any [`aws.route53.ZoneAssociation` resource](https://www.terraform.io/docs/providers/aws/r/route53_zone_association.html) specifying the same zone ID. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Zone<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Hosted Zone ID. This can be referenced by zone records.
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
            <td class="align-top">comment</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A comment for the hosted zone. Defaults to &#39;Managed by Pulumi&#39;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">delegation<wbr>Set<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the reusable delegation set whose NS records you want to assign to the hosted zone. Conflicts with `vpc` as delegation sets can only be used for public zones.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">force<wbr>Destroy</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to destroy all records (possibly managed outside of this provider) in the zone when destroying the zone.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
This is the name of the hosted zone.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name<wbr>Servers</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of name servers in associated (or default) delegation set.
Find more about delegation sets in [AWS docs](https://docs.aws.amazon.com/Route53/latest/APIReference/actions-on-reusable-delegation-sets.html).
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
A mapping of tags to assign to the zone.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpcs</td>
            <td class="align-top">
                
                <code><a href="#zonevpc">route53.<wbr>Zone<wbr>Vpc[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block(s) specifying VPC(s) to associate with a private hosted zone. Conflicts with the `delegation_set_id` argument in this resource and any [`aws.route53.ZoneAssociation` resource](https://www.terraform.io/docs/providers/aws/r/route53_zone_association.html) specifying the same zone ID. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">zone<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Hosted Zone ID. This can be referenced by zone records.
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
            <td class="align-top">comment</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A comment for the hosted zone. Defaults to &#39;Managed by Pulumi&#39;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">delegation_<wbr>set_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the reusable delegation set whose NS records you want to assign to the hosted zone. Conflicts with `vpc` as delegation sets can only be used for public zones.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">force_<wbr>destroy</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to destroy all records (possibly managed outside of this provider) in the zone when destroying the zone.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
This is the name of the hosted zone.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name_<wbr>servers</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of name servers in associated (or default) delegation set.
Find more about delegation sets in [AWS docs](https://docs.aws.amazon.com/Route53/latest/APIReference/actions-on-reusable-delegation-sets.html).
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
A mapping of tags to assign to the zone.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpcs</td>
            <td class="align-top">
                
                <code><a href="#zonevpc">List[Zone<wbr>Vpc]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block(s) specifying VPC(s) to associate with a private hosted zone. Conflicts with the `delegation_set_id` argument in this resource and any [`aws.route53.ZoneAssociation` resource](https://www.terraform.io/docs/providers/aws/r/route53_zone_association.html) specifying the same zone ID. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">zone_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Hosted Zone ID. This can be referenced by zone records.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### ZoneVpc
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ZoneVpc">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ZoneVpc">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/route53?tab=doc#ZoneVpcArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/route53?tab=doc#ZoneVpcOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Route53.ZoneVpcArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Route53.ZoneVpc.html">output</a> API doc for this type.
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
            <td class="align-top">Vpc<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
ID of the VPC to associate.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Region</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Region of the VPC to associate. Defaults to AWS provider region.
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
            <td class="align-top">Vpc<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
ID of the VPC to associate.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Region</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Region of the VPC to associate. Defaults to AWS provider region.
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
            <td class="align-top">vpc<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
ID of the VPC to associate.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc<wbr>Region</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Region of the VPC to associate. Defaults to AWS provider region.
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
            <td class="align-top">vpc_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
ID of the VPC to associate.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc_<wbr>region</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Region of the VPC to associate. Defaults to AWS provider region.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







