
---
title: "RegexMatchSet"
block_external_search_index: true
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>

Provides a WAF Regional Regex Match Set Resource

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const exampleRegexPatternSet = new aws.wafregional.RegexPatternSet("example", {
    regexPatternStrings: [
        "one",
        "two",
    ],
});
const exampleRegexMatchSet = new aws.wafregional.RegexMatchSet("example", {
    regexMatchTuples: [{
        fieldToMatch: {
            data: "User-Agent",
            type: "HEADER",
        },
        regexPatternSetId: exampleRegexPatternSet.id,
        textTransformation: "NONE",
    }],
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/wafregional_regex_match_set.html.markdown.



## Create a RegexMatchSet Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/wafregional/#RegexMatchSet">RegexMatchSet</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/wafregional/#RegexMatchSetArgs">RegexMatchSetArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">RegexMatchSet</span><span class="p">(resource_name, opts=None, </span>name=None<span class="p">, </span>regex_match_tuples=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewRegexMatchSet<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/wafregional?tab=doc#RegexMatchSetArgs">RegexMatchSetArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/wafregional?tab=doc#RegexMatchSet">RegexMatchSet</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Wafregional.RegexMatchSet.html">RegexMatchSet</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Wafregional.RegexMatchSetArgs.html">RegexMatchSetArgs</a></span>? <span class="nx">args = null<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a RegexMatchSet resource with the given unique name, arguments, and options.

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
The name or description of the Regex Match Set.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Regex<wbr>Match<wbr>Tuples</td>
            <td class="align-top">
                
                <code><a href="#regexmatchsetregexmatchtuple">List&lt;Pulumi.<wbr>Aws.<wbr>Wafregional.<wbr>Regex<wbr>Match<wbr>Set<wbr>Regex<wbr>Match<wbr>Tuple<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The regular expression pattern that you want AWS WAF to search for in web requests,
the location in requests that you want AWS WAF to search, and other settings. See below.
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
The name or description of the Regex Match Set.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Regex<wbr>Match<wbr>Tuples</td>
            <td class="align-top">
                
                <code><a href="#regexmatchsetregexmatchtuple">[]wafregional.<wbr>Regex<wbr>Match<wbr>Set<wbr>Regex<wbr>Match<wbr>Tuple</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The regular expression pattern that you want AWS WAF to search for in web requests,
the location in requests that you want AWS WAF to search, and other settings. See below.
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
The name or description of the Regex Match Set.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">regex<wbr>Match<wbr>Tuples</td>
            <td class="align-top">
                
                <code><a href="#regexmatchsetregexmatchtuple">wafregional.<wbr>Regex<wbr>Match<wbr>Set<wbr>Regex<wbr>Match<wbr>Tuple[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The regular expression pattern that you want AWS WAF to search for in web requests,
the location in requests that you want AWS WAF to search, and other settings. See below.
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
The name or description of the Regex Match Set.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">regex_<wbr>match_<wbr>tuples</td>
            <td class="align-top">
                
                <code><a href="#regexmatchsetregexmatchtuple">List[Regex<wbr>Match<wbr>Set<wbr>Regex<wbr>Match<wbr>Tuple]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The regular expression pattern that you want AWS WAF to search for in web requests,
the location in requests that you want AWS WAF to search, and other settings. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## RegexMatchSet Output Properties

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
            <td class="align-top">{{% md %}} The name or description of the Regex Match Set.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Regex<wbr>Match<wbr>Tuples</td>
            <td class="align-top">
                
                <code><a href="#regexmatchsetregexmatchtuple">List&lt;Pulumi.<wbr>Aws.<wbr>Wafregional.<wbr>Regex<wbr>Match<wbr>Set<wbr>Regex<wbr>Match<wbr>Tuple&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} The regular expression pattern that you want AWS WAF to search for in web requests,
the location in requests that you want AWS WAF to search, and other settings. See below.
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
            <td class="align-top">{{% md %}} The name or description of the Regex Match Set.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Regex<wbr>Match<wbr>Tuples</td>
            <td class="align-top">
                
                <code><a href="#regexmatchsetregexmatchtuple">[]wafregional.<wbr>Regex<wbr>Match<wbr>Set<wbr>Regex<wbr>Match<wbr>Tuple</a></code>
            </td>
            <td class="align-top">{{% md %}} The regular expression pattern that you want AWS WAF to search for in web requests,
the location in requests that you want AWS WAF to search, and other settings. See below.
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
            <td class="align-top">{{% md %}} The name or description of the Regex Match Set.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">regex<wbr>Match<wbr>Tuples</td>
            <td class="align-top">
                
                <code><a href="#regexmatchsetregexmatchtuple">wafregional.<wbr>Regex<wbr>Match<wbr>Set<wbr>Regex<wbr>Match<wbr>Tuple[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} The regular expression pattern that you want AWS WAF to search for in web requests,
the location in requests that you want AWS WAF to search, and other settings. See below.
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
            <td class="align-top">{{% md %}} The name or description of the Regex Match Set.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">regex_<wbr>match_<wbr>tuples</td>
            <td class="align-top">
                
                <code><a href="#regexmatchsetregexmatchtuple">List[Regex<wbr>Match<wbr>Set<wbr>Regex<wbr>Match<wbr>Tuple]</a></code>
            </td>
            <td class="align-top">{{% md %}} The regular expression pattern that you want AWS WAF to search for in web requests,
the location in requests that you want AWS WAF to search, and other settings. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing RegexMatchSet Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/wafregional/#RegexMatchSetState">RegexMatchSetState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/wafregional/#RegexMatchSet">RegexMatchSet</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>name=None<span class="p">, </span>regex_match_tuples=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetRegexMatchSet<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/wafregional?tab=doc#RegexMatchSetState">RegexMatchSetState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/wafregional?tab=doc#RegexMatchSet">RegexMatchSet</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Wafregional.RegexMatchSet.html">RegexMatchSet</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Wafregional.RegexMatchSetState.html">RegexMatchSetState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Get an existing RegexMatchSet resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
The name or description of the Regex Match Set.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Regex<wbr>Match<wbr>Tuples</td>
            <td class="align-top">
                
                <code><a href="#regexmatchsetregexmatchtuple">List&lt;Pulumi.<wbr>Aws.<wbr>Wafregional.<wbr>Regex<wbr>Match<wbr>Set<wbr>Regex<wbr>Match<wbr>Tuple<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The regular expression pattern that you want AWS WAF to search for in web requests,
the location in requests that you want AWS WAF to search, and other settings. See below.
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
The name or description of the Regex Match Set.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Regex<wbr>Match<wbr>Tuples</td>
            <td class="align-top">
                
                <code><a href="#regexmatchsetregexmatchtuple">[]wafregional.<wbr>Regex<wbr>Match<wbr>Set<wbr>Regex<wbr>Match<wbr>Tuple</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The regular expression pattern that you want AWS WAF to search for in web requests,
the location in requests that you want AWS WAF to search, and other settings. See below.
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
The name or description of the Regex Match Set.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">regex<wbr>Match<wbr>Tuples</td>
            <td class="align-top">
                
                <code><a href="#regexmatchsetregexmatchtuple">wafregional.<wbr>Regex<wbr>Match<wbr>Set<wbr>Regex<wbr>Match<wbr>Tuple[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The regular expression pattern that you want AWS WAF to search for in web requests,
the location in requests that you want AWS WAF to search, and other settings. See below.
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
The name or description of the Regex Match Set.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">regex_<wbr>match_<wbr>tuples</td>
            <td class="align-top">
                
                <code><a href="#regexmatchsetregexmatchtuple">List[Regex<wbr>Match<wbr>Set<wbr>Regex<wbr>Match<wbr>Tuple]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The regular expression pattern that you want AWS WAF to search for in web requests,
the location in requests that you want AWS WAF to search, and other settings. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### RegexMatchSetRegexMatchTuple
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#RegexMatchSetRegexMatchTuple">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#RegexMatchSetRegexMatchTuple">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/wafregional?tab=doc#RegexMatchSetRegexMatchTupleArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/wafregional?tab=doc#RegexMatchSetRegexMatchTupleOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Wafregional.RegexMatchSetRegexMatchTupleArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Wafregional.RegexMatchSetRegexMatchTuple.html">output</a> API doc for this type.
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
                
                <code><a href="#regexmatchsetregexmatchtuplefieldtomatch">Pulumi.<wbr>Aws.<wbr>Wafregional.<wbr>Regex<wbr>Match<wbr>Set<wbr>Regex<wbr>Match<wbr>Tuple<wbr>Field<wbr>To<wbr>Match<wbr>Args</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The part of a web request that you want to search, such as a specified header or a query string.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Regex<wbr>Pattern<wbr>Set<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of a [Regex Pattern Set](https://www.terraform.io/docs/providers/aws/r/waf_regex_pattern_set.html).
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
Text transformations used to eliminate unusual formatting that attackers use in web requests in an effort to bypass AWS WAF.
e.g. `CMD_LINE`, `HTML_ENTITY_DECODE` or `NONE`.
See [docs](http://docs.aws.amazon.com/waf/latest/APIReference/API_ByteMatchTuple.html#WAF-Type-ByteMatchTuple-TextTransformation)
for all supported values.
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
                
                <code><a href="#regexmatchsetregexmatchtuplefieldtomatch">wafregional.<wbr>Regex<wbr>Match<wbr>Set<wbr>Regex<wbr>Match<wbr>Tuple<wbr>Field<wbr>To<wbr>Match</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The part of a web request that you want to search, such as a specified header or a query string.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Regex<wbr>Pattern<wbr>Set<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of a [Regex Pattern Set](https://www.terraform.io/docs/providers/aws/r/waf_regex_pattern_set.html).
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
Text transformations used to eliminate unusual formatting that attackers use in web requests in an effort to bypass AWS WAF.
e.g. `CMD_LINE`, `HTML_ENTITY_DECODE` or `NONE`.
See [docs](http://docs.aws.amazon.com/waf/latest/APIReference/API_ByteMatchTuple.html#WAF-Type-ByteMatchTuple-TextTransformation)
for all supported values.
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
                
                <code><a href="#regexmatchsetregexmatchtuplefieldtomatch">wafregional.<wbr>Regex<wbr>Match<wbr>Set<wbr>Regex<wbr>Match<wbr>Tuple<wbr>Field<wbr>To<wbr>Match</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The part of a web request that you want to search, such as a specified header or a query string.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">regex<wbr>Pattern<wbr>Set<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of a [Regex Pattern Set](https://www.terraform.io/docs/providers/aws/r/waf_regex_pattern_set.html).
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
Text transformations used to eliminate unusual formatting that attackers use in web requests in an effort to bypass AWS WAF.
e.g. `CMD_LINE`, `HTML_ENTITY_DECODE` or `NONE`.
See [docs](http://docs.aws.amazon.com/waf/latest/APIReference/API_ByteMatchTuple.html#WAF-Type-ByteMatchTuple-TextTransformation)
for all supported values.
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
            <td class="align-top">field<wbr>To<wbr>Match</td>
            <td class="align-top">
                
                <code><a href="#regexmatchsetregexmatchtuplefieldtomatch">Dict[Regex<wbr>Match<wbr>Set<wbr>Regex<wbr>Match<wbr>Tuple<wbr>Field<wbr>To<wbr>Match]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The part of a web request that you want to search, such as a specified header or a query string.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">regex<wbr>Pattern<wbr>Set<wbr>Id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of a [Regex Pattern Set](https://www.terraform.io/docs/providers/aws/r/waf_regex_pattern_set.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">text<wbr>Transformation</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Text transformations used to eliminate unusual formatting that attackers use in web requests in an effort to bypass AWS WAF.
e.g. `CMD_LINE`, `HTML_ENTITY_DECODE` or `NONE`.
See [docs](http://docs.aws.amazon.com/waf/latest/APIReference/API_ByteMatchTuple.html#WAF-Type-ByteMatchTuple-TextTransformation)
for all supported values.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### RegexMatchSetRegexMatchTupleFieldToMatch
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#RegexMatchSetRegexMatchTupleFieldToMatch">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#RegexMatchSetRegexMatchTupleFieldToMatch">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/wafregional?tab=doc#RegexMatchSetRegexMatchTupleFieldToMatchArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/wafregional?tab=doc#RegexMatchSetRegexMatchTupleFieldToMatchOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Wafregional.RegexMatchSetRegexMatchTupleFieldToMatchArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Wafregional.RegexMatchSetRegexMatchTupleFieldToMatch.html">output</a> API doc for this type.
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
When `type` is `HEADER`, enter the name of the header that you want to search, e.g. `User-Agent` or `Referer`.
If `type` is any other value, omit this field.
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
The part of the web request that you want AWS WAF to search for a specified string.
e.g. `HEADER`, `METHOD` or `BODY`.
See [docs](http://docs.aws.amazon.com/waf/latest/APIReference/API_FieldToMatch.html)
for all supported values.
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
When `type` is `HEADER`, enter the name of the header that you want to search, e.g. `User-Agent` or `Referer`.
If `type` is any other value, omit this field.
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
The part of the web request that you want AWS WAF to search for a specified string.
e.g. `HEADER`, `METHOD` or `BODY`.
See [docs](http://docs.aws.amazon.com/waf/latest/APIReference/API_FieldToMatch.html)
for all supported values.
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
When `type` is `HEADER`, enter the name of the header that you want to search, e.g. `User-Agent` or `Referer`.
If `type` is any other value, omit this field.
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
The part of the web request that you want AWS WAF to search for a specified string.
e.g. `HEADER`, `METHOD` or `BODY`.
See [docs](http://docs.aws.amazon.com/waf/latest/APIReference/API_FieldToMatch.html)
for all supported values.
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
When `type` is `HEADER`, enter the name of the header that you want to search, e.g. `User-Agent` or `Referer`.
If `type` is any other value, omit this field.
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
The part of the web request that you want AWS WAF to search for a specified string.
e.g. `HEADER`, `METHOD` or `BODY`.
See [docs](http://docs.aws.amazon.com/waf/latest/APIReference/API_FieldToMatch.html)
for all supported values.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







