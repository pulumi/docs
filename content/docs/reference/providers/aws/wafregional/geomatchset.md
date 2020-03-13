
---
title: "GeoMatchSet"
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>


Provides a WAF Regional Geo Match Set Resource

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const geoMatchSet = new aws.wafregional.GeoMatchSet("geo_match_set", {
    geoMatchConstraints: [
        {
            type: "Country",
            value: "US",
        },
        {
            type: "Country",
            value: "CA",
        },
    ],
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/wafregional_geo_match_set.html.markdown.



## Create a GeoMatchSet Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/wafregional/#GeoMatchSet">GeoMatchSet</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/wafregional/#GeoMatchSetArgs">GeoMatchSetArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">GeoMatchSet</span><span class="p">(resource_name, id, opts=None, </span>geo_match_constraints=None<span class="p">, </span>name=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewGeoMatchSet<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/wafregional?tab=doc#GeoMatchSetArgs">GeoMatchSetArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/wafregional?tab=doc#GeoMatchSet">GeoMatchSet</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Wafregional.GeoMatchSet.html">GeoMatchSet</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Wafregional.GeoMatchSetArgs.html">GeoMatchSetArgs</a></span>? <span class="nx">args = null<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a GeoMatchSet resource with the given unique name, arguments, and options.

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
            <td class="align-top">Geo<wbr>Match<wbr>Constraints</td>
            <td class="align-top">
                
                <code><a href="#geomatchsetgeomatchconstraint">List&lt;Pulumi.<wbr>Aws.<wbr>Wafregional.<wbr>Geo<wbr>Match<wbr>Set<wbr>Geo<wbr>Match<wbr>Constraint<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Geo Match Constraint objects which contain the country that you want AWS WAF to search for.
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
The name or description of the Geo Match Set.
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
            <td class="align-top">Geo<wbr>Match<wbr>Constraints</td>
            <td class="align-top">
                
                <code><a href="#geomatchsetgeomatchconstraint">[]wafregional.<wbr>Geo<wbr>Match<wbr>Set<wbr>Geo<wbr>Match<wbr>Constraint</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Geo Match Constraint objects which contain the country that you want AWS WAF to search for.
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
The name or description of the Geo Match Set.
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
            <td class="align-top">geo<wbr>Match<wbr>Constraints</td>
            <td class="align-top">
                
                <code><a href="#geomatchsetgeomatchconstraint">wafregional.<wbr>Geo<wbr>Match<wbr>Set<wbr>Geo<wbr>Match<wbr>Constraint[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Geo Match Constraint objects which contain the country that you want AWS WAF to search for.
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
The name or description of the Geo Match Set.
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
            <td class="align-top">geo_<wbr>match_<wbr>constraints</td>
            <td class="align-top">
                
                <code><a href="#geomatchsetgeomatchconstraint">list[geo_<wbr>match_<wbr>set_<wbr>geo_<wbr>match_<wbr>constraint]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Geo Match Constraint objects which contain the country that you want AWS WAF to search for.
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
The name or description of the Geo Match Set.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## GeoMatchSet Output Properties

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
            <td class="align-top">Geo<wbr>Match<wbr>Constraints</td>
            <td class="align-top">
                
                <code><a href="#geomatchsetgeomatchconstraint">List&lt;Pulumi.<wbr>Aws.<wbr>Wafregional.<wbr>Geo<wbr>Match<wbr>Set<wbr>Geo<wbr>Match<wbr>Constraint&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} The Geo Match Constraint objects which contain the country that you want AWS WAF to search for.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name or description of the Geo Match Set.
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
            <td class="align-top">Geo<wbr>Match<wbr>Constraints</td>
            <td class="align-top">
                
                <code><a href="#geomatchsetgeomatchconstraint">[]wafregional.<wbr>Geo<wbr>Match<wbr>Set<wbr>Geo<wbr>Match<wbr>Constraint</a></code>
            </td>
            <td class="align-top">{{% md %}} The Geo Match Constraint objects which contain the country that you want AWS WAF to search for.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name or description of the Geo Match Set.
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
            <td class="align-top">geo<wbr>Match<wbr>Constraints</td>
            <td class="align-top">
                
                <code><a href="#geomatchsetgeomatchconstraint">wafregional.<wbr>Geo<wbr>Match<wbr>Set<wbr>Geo<wbr>Match<wbr>Constraint[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} The Geo Match Constraint objects which contain the country that you want AWS WAF to search for.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name or description of the Geo Match Set.
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
            <td class="align-top">geo_<wbr>match_<wbr>constraints</td>
            <td class="align-top">
                
                <code><a href="#geomatchsetgeomatchconstraint">list[geo_<wbr>match_<wbr>set_<wbr>geo_<wbr>match_<wbr>constraint]</a></code>
            </td>
            <td class="align-top">{{% md %}} The Geo Match Constraint objects which contain the country that you want AWS WAF to search for.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name or description of the Geo Match Set.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing GeoMatchSet Resource

{{< langchoose csharp nojavascript >}}

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: GeoMatchSetState, opts?: pulumi.CustomResourceOptions): GeoMatchSet;
```

```python
def get(resource_name, id, opts=None, geo_<wbr>match_<wbr>constraints=None, name=None)
```

```go
func GetGeoMatchSet(ctx *pulumi.Context, name string, id pulumi.IDInput, state *GeoMatchSetState, opts ...pulumi.ResourceOption) (*Bucket, error)
```

```csharp
public static GeoMatchSet Get(string name, Input<string> id, GeoMatchSetState? state = null, CustomResourceOptions? options = null);
```

Get an existing GeoMatchSet resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
            <td class="align-top">Geo<wbr>Match<wbr>Constraints</td>
            <td class="align-top">
                
                <code><a href="#geomatchsetgeomatchconstraint">List&lt;Pulumi.<wbr>Aws.<wbr>Wafregional.<wbr>Geo<wbr>Match<wbr>Set<wbr>Geo<wbr>Match<wbr>Constraint<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Geo Match Constraint objects which contain the country that you want AWS WAF to search for.
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
The name or description of the Geo Match Set.
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
            <td class="align-top">Geo<wbr>Match<wbr>Constraints</td>
            <td class="align-top">
                
                <code><a href="#geomatchsetgeomatchconstraint">[]wafregional.<wbr>Geo<wbr>Match<wbr>Set<wbr>Geo<wbr>Match<wbr>Constraint</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Geo Match Constraint objects which contain the country that you want AWS WAF to search for.
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
The name or description of the Geo Match Set.
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
            <td class="align-top">geo<wbr>Match<wbr>Constraints</td>
            <td class="align-top">
                
                <code><a href="#geomatchsetgeomatchconstraint">wafregional.<wbr>Geo<wbr>Match<wbr>Set<wbr>Geo<wbr>Match<wbr>Constraint[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Geo Match Constraint objects which contain the country that you want AWS WAF to search for.
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
The name or description of the Geo Match Set.
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
            <td class="align-top">geo_<wbr>match_<wbr>constraints</td>
            <td class="align-top">
                
                <code><a href="#geomatchsetgeomatchconstraint">list[geo_<wbr>match_<wbr>set_<wbr>geo_<wbr>match_<wbr>constraint]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Geo Match Constraint objects which contain the country that you want AWS WAF to search for.
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
The name or description of the Geo Match Set.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### GeoMatchSetGeoMatchConstraint
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#GeoMatchSetGeoMatchConstraint">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GeoMatchSetGeoMatchConstraint">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/wafregional?tab=doc#GeoMatchSetGeoMatchConstraintArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/wafregional?tab=doc#GeoMatchSetGeoMatchConstraintOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Wafregional.GeoMatchSetGeoMatchConstraintArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Wafregional.GeoMatchSetGeoMatchConstraint.html">output</a> API doc for this type.
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
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of geographical area you want AWS WAF to search for. Currently Country is the only valid value.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Value</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The country that you want AWS WAF to search for.
This is the two-letter country code, e.g. `US`, `CA`, `RU`, `CN`, etc.
See [docs](https://docs.aws.amazon.com/waf/latest/APIReference/API_GeoMatchConstraint.html) for all supported values.
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
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of geographical area you want AWS WAF to search for. Currently Country is the only valid value.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Value</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The country that you want AWS WAF to search for.
This is the two-letter country code, e.g. `US`, `CA`, `RU`, `CN`, etc.
See [docs](https://docs.aws.amazon.com/waf/latest/APIReference/API_GeoMatchConstraint.html) for all supported values.
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
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of geographical area you want AWS WAF to search for. Currently Country is the only valid value.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">value</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The country that you want AWS WAF to search for.
This is the two-letter country code, e.g. `US`, `CA`, `RU`, `CN`, etc.
See [docs](https://docs.aws.amazon.com/waf/latest/APIReference/API_GeoMatchConstraint.html) for all supported values.
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
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of geographical area you want AWS WAF to search for. Currently Country is the only valid value.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">value</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The country that you want AWS WAF to search for.
This is the two-letter country code, e.g. `US`, `CA`, `RU`, `CN`, etc.
See [docs](https://docs.aws.amazon.com/waf/latest/APIReference/API_GeoMatchConstraint.html) for all supported values.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







