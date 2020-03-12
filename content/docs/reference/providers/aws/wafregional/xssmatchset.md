
---
title: "XssMatchSet"
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>


Provides a WAF Regional XSS Match Set Resource for use with Application Load Balancer.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const xssMatchSet = new aws.wafregional.XssMatchSet("xss_match_set", {
    xssMatchTuples: [
        {
            fieldToMatch: {
                type: "URI",
            },
            textTransformation: "NONE",
        },
        {
            fieldToMatch: {
                type: "QUERY_STRING",
            },
            textTransformation: "NONE",
        },
    ],
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/wafregional_xss_match_set.html.markdown.



## Create a XssMatchSet Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/wafregional/#XssMatchSet">XssMatchSet</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/wafregional/#XssMatchSetArgs">XssMatchSetArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

```python
def XssMatchSet(resource_name, id, opts=None, name=None, xss_<wbr>match_<wbr>tuples=None, __props__=None)
```

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewXssMatchSet<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/wafregional?tab=doc#XssMatchSetArgs">XssMatchSetArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/wafregional?tab=doc#XssMatchSet">XssMatchSet</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Wafregional.XssMatchSet.html">XssMatchSet</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Wafregional.XssMatchSetArgs.html">XssMatchSetArgs</a></span>? <span class="nx">args = null<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a XssMatchSet resource with the given unique name, arguments, and options.

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
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the set
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Xss<wbr>Match<wbr>Tuples</td>
            <td class="align-top">
                
                <code><a href="#xssmatchsetxssmatchtuple">List&lt;Pulumi.<wbr>Aws.<wbr>Wafregional.<wbr>Xss<wbr>Match<wbr>Set<wbr>Xss<wbr>Match<wbr>Tuple<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The parts of web requests that you want to inspect for cross-site scripting attacks.
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
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the set
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Xss<wbr>Match<wbr>Tuples</td>
            <td class="align-top">
                
                <code><a href="#xssmatchsetxssmatchtuple">[]wafregional.<wbr>Xss<wbr>Match<wbr>Set<wbr>Xss<wbr>Match<wbr>Tuple</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The parts of web requests that you want to inspect for cross-site scripting attacks.
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
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the set
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">xss<wbr>Match<wbr>Tuples</td>
            <td class="align-top">
                
                <code><a href="#xssmatchsetxssmatchtuple">wafregional.<wbr>Xss<wbr>Match<wbr>Set<wbr>Xss<wbr>Match<wbr>Tuple[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The parts of web requests that you want to inspect for cross-site scripting attacks.
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
 (Optional)
The name of the set
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">xss_<wbr>match_<wbr>tuples</td>
            <td class="align-top">
                
                <code><a href="#xssmatchsetxssmatchtuple">list[xss_<wbr>match_<wbr>set_<wbr>xss_<wbr>match_<wbr>tuple]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The parts of web requests that you want to inspect for cross-site scripting attacks.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## XssMatchSet Output Properties

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
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the set
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Xss<wbr>Match<wbr>Tuples</td>
            <td class="align-top">
                
                <code><a href="#xssmatchsetxssmatchtuple">List&lt;Pulumi.<wbr>Aws.<wbr>Wafregional.<wbr>Xss<wbr>Match<wbr>Set<wbr>Xss<wbr>Match<wbr>Tuple&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} The parts of web requests that you want to inspect for cross-site scripting attacks.
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
            <td class="align-top">{{% md %}} The name of the set
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Xss<wbr>Match<wbr>Tuples</td>
            <td class="align-top">
                
                <code><a href="#xssmatchsetxssmatchtuple">[]wafregional.<wbr>Xss<wbr>Match<wbr>Set<wbr>Xss<wbr>Match<wbr>Tuple</a></code>
            </td>
            <td class="align-top">{{% md %}} The parts of web requests that you want to inspect for cross-site scripting attacks.
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
            <td class="align-top">{{% md %}} The name of the set
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">xss<wbr>Match<wbr>Tuples</td>
            <td class="align-top">
                
                <code><a href="#xssmatchsetxssmatchtuple">wafregional.<wbr>Xss<wbr>Match<wbr>Set<wbr>Xss<wbr>Match<wbr>Tuple[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} The parts of web requests that you want to inspect for cross-site scripting attacks.
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
            <td class="align-top">{{% md %}} The name of the set
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">xss_<wbr>match_<wbr>tuples</td>
            <td class="align-top">
                
                <code><a href="#xssmatchsetxssmatchtuple">list[xss_<wbr>match_<wbr>set_<wbr>xss_<wbr>match_<wbr>tuple]</a></code>
            </td>
            <td class="align-top">{{% md %}} The parts of web requests that you want to inspect for cross-site scripting attacks.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing XssMatchSet Resource

{{< langchoose csharp nojavascript >}}

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: XssMatchSetState, opts?: pulumi.CustomResourceOptions): XssMatchSet;
```

```python
def get(resource_name, id, opts=None, name=None, xss_<wbr>match_<wbr>tuples=None)
```

```go
func GetXssMatchSet(ctx *pulumi.Context, name string, id pulumi.IDInput, state *XssMatchSetState, opts ...pulumi.ResourceOption) (*Bucket, error)
```

```csharp
public static XssMatchSet Get(string name, Input<string> id, XssMatchSetState? state = null, CustomResourceOptions? options = null);
```

Get an existing XssMatchSet resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the set
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Xss<wbr>Match<wbr>Tuples</td>
            <td class="align-top">
                
                <code><a href="#xssmatchsetxssmatchtuple">List&lt;Pulumi.<wbr>Aws.<wbr>Wafregional.<wbr>Xss<wbr>Match<wbr>Set<wbr>Xss<wbr>Match<wbr>Tuple<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The parts of web requests that you want to inspect for cross-site scripting attacks.
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
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the set
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Xss<wbr>Match<wbr>Tuples</td>
            <td class="align-top">
                
                <code><a href="#xssmatchsetxssmatchtuple">[]wafregional.<wbr>Xss<wbr>Match<wbr>Set<wbr>Xss<wbr>Match<wbr>Tuple</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The parts of web requests that you want to inspect for cross-site scripting attacks.
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
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the set
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">xss<wbr>Match<wbr>Tuples</td>
            <td class="align-top">
                
                <code><a href="#xssmatchsetxssmatchtuple">wafregional.<wbr>Xss<wbr>Match<wbr>Set<wbr>Xss<wbr>Match<wbr>Tuple[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The parts of web requests that you want to inspect for cross-site scripting attacks.
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
 (Optional)
The name of the set
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">xss_<wbr>match_<wbr>tuples</td>
            <td class="align-top">
                
                <code><a href="#xssmatchsetxssmatchtuple">list[xss_<wbr>match_<wbr>set_<wbr>xss_<wbr>match_<wbr>tuple]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The parts of web requests that you want to inspect for cross-site scripting attacks.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### XssMatchSetXssMatchTuple
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#XssMatchSetXssMatchTuple">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#XssMatchSetXssMatchTuple">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/wafregional?tab=doc#XssMatchSetXssMatchTupleArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/wafregional?tab=doc#XssMatchSetXssMatchTupleOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Wafregional.XssMatchSetXssMatchTupleArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Wafregional.XssMatchSetXssMatchTuple.html">output</a> API doc for this type.
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
            <td class="align-top">Field<wbr>To<wbr>Match</td>
            <td class="align-top">
                
                <code><a href="#xssmatchsetxssmatchtuplefieldtomatch">Pulumi.<wbr>Aws.<wbr>Wafregional.<wbr>Xss<wbr>Match<wbr>Set<wbr>Xss<wbr>Match<wbr>Tuple<wbr>Field<wbr>To<wbr>Match<wbr>Args</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies where in a web request to look for cross-site scripting attacks.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Text<wbr>Transformation</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Which text transformation, if any, to perform on the web request before inspecting the request for cross-site scripting attacks.
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
            <td class="align-top">Field<wbr>To<wbr>Match</td>
            <td class="align-top">
                
                <code><a href="#xssmatchsetxssmatchtuplefieldtomatch">wafregional.<wbr>Xss<wbr>Match<wbr>Set<wbr>Xss<wbr>Match<wbr>Tuple<wbr>Field<wbr>To<wbr>Match</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies where in a web request to look for cross-site scripting attacks.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Text<wbr>Transformation</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Which text transformation, if any, to perform on the web request before inspecting the request for cross-site scripting attacks.
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
            <td class="align-top">field<wbr>To<wbr>Match</td>
            <td class="align-top">
                
                <code><a href="#xssmatchsetxssmatchtuplefieldtomatch">wafregional.<wbr>Xss<wbr>Match<wbr>Set<wbr>Xss<wbr>Match<wbr>Tuple<wbr>Field<wbr>To<wbr>Match</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies where in a web request to look for cross-site scripting attacks.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">text<wbr>Transformation</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Which text transformation, if any, to perform on the web request before inspecting the request for cross-site scripting attacks.
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
            <td class="align-top">field_<wbr>to_<wbr>match</td>
            <td class="align-top">
                
                <code><a href="#xssmatchsetxssmatchtuplefieldtomatch">dict{xss_<wbr>match_<wbr>set_<wbr>xss_<wbr>match_<wbr>tuple_<wbr>field_<wbr>to_<wbr>match}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies where in a web request to look for cross-site scripting attacks.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">text_<wbr>transformation</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Which text transformation, if any, to perform on the web request before inspecting the request for cross-site scripting attacks.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### XssMatchSetXssMatchTupleFieldToMatch
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#XssMatchSetXssMatchTupleFieldToMatch">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#XssMatchSetXssMatchTupleFieldToMatch">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/wafregional?tab=doc#XssMatchSetXssMatchTupleFieldToMatchArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/wafregional?tab=doc#XssMatchSetXssMatchTupleFieldToMatchOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Wafregional.XssMatchSetXssMatchTupleFieldToMatchArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Wafregional.XssMatchSetXssMatchTupleFieldToMatch.html">output</a> API doc for this type.
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
            <td class="align-top">Data</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When the value of `type` is `HEADER`, enter the name of the header that you want the WAF to search, for example, `User-Agent` or `Referer`. If the value of `type` is any other value, omit `data`.
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
The part of the web request that you want AWS WAF to search for a specified string. e.g. `HEADER` or `METHOD`
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
            <td class="align-top">Data</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When the value of `type` is `HEADER`, enter the name of the header that you want the WAF to search, for example, `User-Agent` or `Referer`. If the value of `type` is any other value, omit `data`.
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
The part of the web request that you want AWS WAF to search for a specified string. e.g. `HEADER` or `METHOD`
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
            <td class="align-top">data</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When the value of `type` is `HEADER`, enter the name of the header that you want the WAF to search, for example, `User-Agent` or `Referer`. If the value of `type` is any other value, omit `data`.
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
The part of the web request that you want AWS WAF to search for a specified string. e.g. `HEADER` or `METHOD`
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
            <td class="align-top">data</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When the value of `type` is `HEADER`, enter the name of the header that you want the WAF to search, for example, `User-Agent` or `Referer`. If the value of `type` is any other value, omit `data`.
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
The part of the web request that you want AWS WAF to search for a specified string. e.g. `HEADER` or `METHOD`
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







