
---
title: "SqlInjectionMatchSet"
block_external_search_index: true
---



Provides a WAF SQL Injection Match Set Resource

{{% examples %}}
## Example Usage
{{% example %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const sqlInjectionMatchSet = new aws.waf.SqlInjectionMatchSet("sql_injection_match_set", {
    sqlInjectionMatchTuples: [{
        fieldToMatch: {
            type: "QUERY_STRING",
        },
        textTransformation: "URL_DECODE",
    }],
});
```

{{% /example %}}
{{% /examples %}}



## Create a SqlInjectionMatchSet Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/waf/#SqlInjectionMatchSet">SqlInjectionMatchSet</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/waf/#SqlInjectionMatchSetArgs">SqlInjectionMatchSetArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">SqlInjectionMatchSet</span><span class="p">(resource_name, opts=None, </span>name=None<span class="p">, </span>sql_injection_match_tuples=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewSqlInjectionMatchSet<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/waf?tab=doc#SqlInjectionMatchSetArgs">SqlInjectionMatchSetArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/waf?tab=doc#SqlInjectionMatchSet">SqlInjectionMatchSet</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Waf.SqlInjectionMatchSet.html">SqlInjectionMatchSet</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Waf.SqlInjectionMatchSetArgs.html">SqlInjectionMatchSetArgs</a></span>? <span class="nx">args = null<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language nodejs %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resource.</dd>
    <dt class="property-optional" title="Optional">
        <span>args</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The arguments to use to populate this resource's properties.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

{{% choosable language python %}}
<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resource.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>
{{% /choosable %}}

{{% choosable language go %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resource.</dd>
    <dt class="property-optional" title="Optional">
        <span>args</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The arguments to use to populate this resource's properties.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

{{% choosable language csharp %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resource.</dd>
    <dt class="property-optional" title="Optional">
        <span>args</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The arguments to use to populate this resource's properties.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

#### Resource Arguments




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name or description of the SQL Injection Match Set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sql<wbr>Injection<wbr>Match<wbr>Tuples</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#sqlinjectionmatchsetsqlinjectionmatchtuple">List&lt;Sql<wbr>Injection<wbr>Match<wbr>Set<wbr>Sql<wbr>Injection<wbr>Match<wbr>Tuple<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}The parts of web requests that you want AWS WAF to inspect for malicious SQL code and, if you want AWS WAF to inspect a header, the name of the header.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name or description of the SQL Injection Match Set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sql<wbr>Injection<wbr>Match<wbr>Tuples</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#sqlinjectionmatchsetsqlinjectionmatchtuple">[]Sql<wbr>Injection<wbr>Match<wbr>Set<wbr>Sql<wbr>Injection<wbr>Match<wbr>Tuple</a></span>
    </dt>
    <dd>{{% md %}}The parts of web requests that you want AWS WAF to inspect for malicious SQL code and, if you want AWS WAF to inspect a header, the name of the header.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name or description of the SQL Injection Match Set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sql<wbr>Injection<wbr>Match<wbr>Tuples</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#sqlinjectionmatchsetsqlinjectionmatchtuple">Sql<wbr>Injection<wbr>Match<wbr>Set<wbr>Sql<wbr>Injection<wbr>Match<wbr>Tuple[]?</a></span>
    </dt>
    <dd>{{% md %}}The parts of web requests that you want AWS WAF to inspect for malicious SQL code and, if you want AWS WAF to inspect a header, the name of the header.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name or description of the SQL Injection Match Set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sql_<wbr>injection_<wbr>match_<wbr>tuples</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#sqlinjectionmatchsetsqlinjectionmatchtuple">List[Sql<wbr>Injection<wbr>Match<wbr>Set<wbr>Sql<wbr>Injection<wbr>Match<wbr>Tuple]</a></span>
    </dt>
    <dd>{{% md %}}The parts of web requests that you want AWS WAF to inspect for malicious SQL code and, if you want AWS WAF to inspect a header, the name of the header.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## SqlInjectionMatchSet Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name or description of the SQL Injection Match Set.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Sql<wbr>Injection<wbr>Match<wbr>Tuples</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#sqlinjectionmatchsetsqlinjectionmatchtuple">List&lt;Sql<wbr>Injection<wbr>Match<wbr>Set<wbr>Sql<wbr>Injection<wbr>Match<wbr>Tuple&gt;?</a></span>
    </dt>
    <dd>{{% md %}}The parts of web requests that you want AWS WAF to inspect for malicious SQL code and, if you want AWS WAF to inspect a header, the name of the header.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name or description of the SQL Injection Match Set.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Sql<wbr>Injection<wbr>Match<wbr>Tuples</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#sqlinjectionmatchsetsqlinjectionmatchtuple">[]Sql<wbr>Injection<wbr>Match<wbr>Set<wbr>Sql<wbr>Injection<wbr>Match<wbr>Tuple</a></span>
    </dt>
    <dd>{{% md %}}The parts of web requests that you want AWS WAF to inspect for malicious SQL code and, if you want AWS WAF to inspect a header, the name of the header.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name or description of the SQL Injection Match Set.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>sql<wbr>Injection<wbr>Match<wbr>Tuples</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#sqlinjectionmatchsetsqlinjectionmatchtuple">Sql<wbr>Injection<wbr>Match<wbr>Set<wbr>Sql<wbr>Injection<wbr>Match<wbr>Tuple[]?</a></span>
    </dt>
    <dd>{{% md %}}The parts of web requests that you want AWS WAF to inspect for malicious SQL code and, if you want AWS WAF to inspect a header, the name of the header.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name or description of the SQL Injection Match Set.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>sql_<wbr>injection_<wbr>match_<wbr>tuples</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#sqlinjectionmatchsetsqlinjectionmatchtuple">List[Sql<wbr>Injection<wbr>Match<wbr>Set<wbr>Sql<wbr>Injection<wbr>Match<wbr>Tuple]</a></span>
    </dt>
    <dd>{{% md %}}The parts of web requests that you want AWS WAF to inspect for malicious SQL code and, if you want AWS WAF to inspect a header, the name of the header.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing SqlInjectionMatchSet Resource

Get an existing SqlInjectionMatchSet resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/waf/#SqlInjectionMatchSetState">SqlInjectionMatchSetState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/waf/#SqlInjectionMatchSet">SqlInjectionMatchSet</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>name=None<span class="p">, </span>sql_injection_match_tuples=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetSqlInjectionMatchSet<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/waf?tab=doc#SqlInjectionMatchSetState">SqlInjectionMatchSetState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/waf?tab=doc#SqlInjectionMatchSet">SqlInjectionMatchSet</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Waf.SqlInjectionMatchSet.html">SqlInjectionMatchSet</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Waf.SqlInjectionMatchSetState.html">SqlInjectionMatchSetState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language nodejs %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resulting resource.</dd>
    <dt class="property-required" title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The <em>unique</em> provider ID of the resource to lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>state</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>Any extra arguments used during the lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

{{% choosable language python %}}
<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>resource_name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resulting resource.</dd>
    <dt class="property-required" title="Optional">
        <span>id</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The <em>unique</em> provider ID of the resource to lookup.</dd>
</dl>
{{% /choosable %}}

{{% choosable language go %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resulting resource.</dd>
    <dt class="property-required" title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The <em>unique</em> provider ID of the resource to lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>state</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>Any extra arguments used during the lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

{{% choosable language csharp %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resulting resource.</dd>
    <dt class="property-required" title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The <em>unique</em> provider ID of the resource to lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>state</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>Any extra arguments used during the lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

The following state arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name or description of the SQL Injection Match Set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sql<wbr>Injection<wbr>Match<wbr>Tuples</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#sqlinjectionmatchsetsqlinjectionmatchtuple">List&lt;Sql<wbr>Injection<wbr>Match<wbr>Set<wbr>Sql<wbr>Injection<wbr>Match<wbr>Tuple<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}The parts of web requests that you want AWS WAF to inspect for malicious SQL code and, if you want AWS WAF to inspect a header, the name of the header.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name or description of the SQL Injection Match Set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sql<wbr>Injection<wbr>Match<wbr>Tuples</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#sqlinjectionmatchsetsqlinjectionmatchtuple">[]Sql<wbr>Injection<wbr>Match<wbr>Set<wbr>Sql<wbr>Injection<wbr>Match<wbr>Tuple</a></span>
    </dt>
    <dd>{{% md %}}The parts of web requests that you want AWS WAF to inspect for malicious SQL code and, if you want AWS WAF to inspect a header, the name of the header.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name or description of the SQL Injection Match Set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sql<wbr>Injection<wbr>Match<wbr>Tuples</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#sqlinjectionmatchsetsqlinjectionmatchtuple">Sql<wbr>Injection<wbr>Match<wbr>Set<wbr>Sql<wbr>Injection<wbr>Match<wbr>Tuple[]?</a></span>
    </dt>
    <dd>{{% md %}}The parts of web requests that you want AWS WAF to inspect for malicious SQL code and, if you want AWS WAF to inspect a header, the name of the header.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name or description of the SQL Injection Match Set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sql_<wbr>injection_<wbr>match_<wbr>tuples</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#sqlinjectionmatchsetsqlinjectionmatchtuple">List[Sql<wbr>Injection<wbr>Match<wbr>Set<wbr>Sql<wbr>Injection<wbr>Match<wbr>Tuple]</a></span>
    </dt>
    <dd>{{% md %}}The parts of web requests that you want AWS WAF to inspect for malicious SQL code and, if you want AWS WAF to inspect a header, the name of the header.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Sql<wbr>Injection<wbr>Match<wbr>Set<wbr>Sql<wbr>Injection<wbr>Match<wbr>Tuple</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#SqlInjectionMatchSetSqlInjectionMatchTuple">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#SqlInjectionMatchSetSqlInjectionMatchTuple">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/waf?tab=doc#SqlInjectionMatchSetSqlInjectionMatchTupleArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/waf?tab=doc#SqlInjectionMatchSetSqlInjectionMatchTupleOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Field<wbr>To<wbr>Match</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#sqlinjectionmatchsetsqlinjectionmatchtuplefieldtomatch">Sql<wbr>Injection<wbr>Match<wbr>Set<wbr>Sql<wbr>Injection<wbr>Match<wbr>Tuple<wbr>Field<wbr>To<wbr>Match<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}Specifies where in a web request to look for snippets of malicious SQL code.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Text<wbr>Transformation</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Text transformations used to eliminate unusual formatting that attackers use in web requests in an effort to bypass AWS WAF.
If you specify a transformation, AWS WAF performs the transformation on `field_to_match` before inspecting a request for a match.
e.g. `CMD_LINE`, `HTML_ENTITY_DECODE` or `NONE`.
See [docs](http://docs.aws.amazon.com/waf/latest/APIReference/API_SqlInjectionMatchTuple.html#WAF-Type-SqlInjectionMatchTuple-TextTransformation)
for all supported values.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Field<wbr>To<wbr>Match</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#sqlinjectionmatchsetsqlinjectionmatchtuplefieldtomatch">Sql<wbr>Injection<wbr>Match<wbr>Set<wbr>Sql<wbr>Injection<wbr>Match<wbr>Tuple<wbr>Field<wbr>To<wbr>Match</a></span>
    </dt>
    <dd>{{% md %}}Specifies where in a web request to look for snippets of malicious SQL code.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Text<wbr>Transformation</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Text transformations used to eliminate unusual formatting that attackers use in web requests in an effort to bypass AWS WAF.
If you specify a transformation, AWS WAF performs the transformation on `field_to_match` before inspecting a request for a match.
e.g. `CMD_LINE`, `HTML_ENTITY_DECODE` or `NONE`.
See [docs](http://docs.aws.amazon.com/waf/latest/APIReference/API_SqlInjectionMatchTuple.html#WAF-Type-SqlInjectionMatchTuple-TextTransformation)
for all supported values.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>field<wbr>To<wbr>Match</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#sqlinjectionmatchsetsqlinjectionmatchtuplefieldtomatch">Sql<wbr>Injection<wbr>Match<wbr>Set<wbr>Sql<wbr>Injection<wbr>Match<wbr>Tuple<wbr>Field<wbr>To<wbr>Match</a></span>
    </dt>
    <dd>{{% md %}}Specifies where in a web request to look for snippets of malicious SQL code.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>text<wbr>Transformation</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Text transformations used to eliminate unusual formatting that attackers use in web requests in an effort to bypass AWS WAF.
If you specify a transformation, AWS WAF performs the transformation on `field_to_match` before inspecting a request for a match.
e.g. `CMD_LINE`, `HTML_ENTITY_DECODE` or `NONE`.
See [docs](http://docs.aws.amazon.com/waf/latest/APIReference/API_SqlInjectionMatchTuple.html#WAF-Type-SqlInjectionMatchTuple-TextTransformation)
for all supported values.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>field<wbr>To<wbr>Match</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#sqlinjectionmatchsetsqlinjectionmatchtuplefieldtomatch">Dict[Sql<wbr>Injection<wbr>Match<wbr>Set<wbr>Sql<wbr>Injection<wbr>Match<wbr>Tuple<wbr>Field<wbr>To<wbr>Match]</a></span>
    </dt>
    <dd>{{% md %}}Specifies where in a web request to look for snippets of malicious SQL code.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>text<wbr>Transformation</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Text transformations used to eliminate unusual formatting that attackers use in web requests in an effort to bypass AWS WAF.
If you specify a transformation, AWS WAF performs the transformation on `field_to_match` before inspecting a request for a match.
e.g. `CMD_LINE`, `HTML_ENTITY_DECODE` or `NONE`.
See [docs](http://docs.aws.amazon.com/waf/latest/APIReference/API_SqlInjectionMatchTuple.html#WAF-Type-SqlInjectionMatchTuple-TextTransformation)
for all supported values.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Sql<wbr>Injection<wbr>Match<wbr>Set<wbr>Sql<wbr>Injection<wbr>Match<wbr>Tuple<wbr>Field<wbr>To<wbr>Match</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#SqlInjectionMatchSetSqlInjectionMatchTupleFieldToMatch">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#SqlInjectionMatchSetSqlInjectionMatchTupleFieldToMatch">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/waf?tab=doc#SqlInjectionMatchSetSqlInjectionMatchTupleFieldToMatchArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/waf?tab=doc#SqlInjectionMatchSetSqlInjectionMatchTupleFieldToMatchOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}When `type` is `HEADER`, enter the name of the header that you want to search, e.g. `User-Agent` or `Referer`.
If `type` is any other value, omit this field.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The part of the web request that you want AWS WAF to search for a specified string.
e.g. `HEADER`, `METHOD` or `BODY`.
See [docs](http://docs.aws.amazon.com/waf/latest/APIReference/API_FieldToMatch.html)
for all supported values.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}When `type` is `HEADER`, enter the name of the header that you want to search, e.g. `User-Agent` or `Referer`.
If `type` is any other value, omit this field.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The part of the web request that you want AWS WAF to search for a specified string.
e.g. `HEADER`, `METHOD` or `BODY`.
See [docs](http://docs.aws.amazon.com/waf/latest/APIReference/API_FieldToMatch.html)
for all supported values.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>data</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}When `type` is `HEADER`, enter the name of the header that you want to search, e.g. `User-Agent` or `Referer`.
If `type` is any other value, omit this field.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The part of the web request that you want AWS WAF to search for a specified string.
e.g. `HEADER`, `METHOD` or `BODY`.
See [docs](http://docs.aws.amazon.com/waf/latest/APIReference/API_FieldToMatch.html)
for all supported values.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>data</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}When `type` is `HEADER`, enter the name of the header that you want to search, e.g. `User-Agent` or `Referer`.
If `type` is any other value, omit this field.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The part of the web request that you want AWS WAF to search for a specified string.
e.g. `HEADER`, `METHOD` or `BODY`.
See [docs](http://docs.aws.amazon.com/waf/latest/APIReference/API_FieldToMatch.html)
for all supported values.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}









<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-aws">https://github.com/pulumi/pulumi-aws</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    <dt>Notes</dt>
	<dd>This Pulumi package is based on the [`aws` Terraform Provider](https://github.com/terraform-providers/terraform-provider-aws).</dd>
</dl>

