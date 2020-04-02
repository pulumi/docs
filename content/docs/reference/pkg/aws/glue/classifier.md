
---
title: "Classifier"
block_external_search_index: true
---

Provides a Glue Classifier resource.

> **NOTE:** It is only valid to create one type of classifier (csv, grok, JSON, or XML). Changing classifier types will recreate the classifier.

## Example Usage

### Csv Classifier

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const example = new aws.glue.Classifier("example", {
    csvClassifier: {
        allowSingleColumn: false,
        containsHeader: "PRESENT",
        delimiter: ",",
        disableValueTrimming: false,
        headers: [
            "example1",
            "example2",
        ],
        quoteSymbol: "'",
    },
});
```

### Grok Classifier

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const example = new aws.glue.Classifier("example", {
    grokClassifier: {
        classification: "example",
        grokPattern: "example",
    },
});
```

### JSON Classifier

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const example = new aws.glue.Classifier("example", {
    jsonClassifier: {
        jsonPath: "example",
    },
});
```

### XML Classifier

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const example = new aws.glue.Classifier("example", {
    xmlClassifier: {
        classification: "example",
        rowTag: "example",
    },
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/glue_classifier.html.markdown.



## Create a Classifier Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/glue/#Classifier">Classifier</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/glue/#ClassifierArgs">ClassifierArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Classifier</span><span class="p">(resource_name, opts=None, </span>csv_classifier=None<span class="p">, </span>grok_classifier=None<span class="p">, </span>json_classifier=None<span class="p">, </span>name=None<span class="p">, </span>xml_classifier=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewClassifier<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/glue?tab=doc#ClassifierArgs">ClassifierArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/glue?tab=doc#Classifier">Classifier</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Glue.Classifier.html">Classifier</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Glue.ClassifierArgs.html">ClassifierArgs</a></span>? <span class="nx">args = null<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Csv<wbr>Classifier</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#classifiercsvclassifier">Classifier<wbr>Csv<wbr>Classifier<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A classifier for Csv content. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Grok<wbr>Classifier</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#classifiergrokclassifier">Classifier<wbr>Grok<wbr>Classifier<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A classifier that uses grok patterns. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Json<wbr>Classifier</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#classifierjsonclassifier">Classifier<wbr>Json<wbr>Classifier<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A classifier for JSON content. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the classifier.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Xml<wbr>Classifier</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#classifierxmlclassifier">Classifier<wbr>Xml<wbr>Classifier<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A classifier for XML content. Defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Csv<wbr>Classifier</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#classifiercsvclassifier">*Classifier<wbr>Csv<wbr>Classifier</a></span>
    </dt>
    <dd>{{% md %}}A classifier for Csv content. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Grok<wbr>Classifier</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#classifiergrokclassifier">*Classifier<wbr>Grok<wbr>Classifier</a></span>
    </dt>
    <dd>{{% md %}}A classifier that uses grok patterns. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Json<wbr>Classifier</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#classifierjsonclassifier">*Classifier<wbr>Json<wbr>Classifier</a></span>
    </dt>
    <dd>{{% md %}}A classifier for JSON content. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the classifier.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Xml<wbr>Classifier</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#classifierxmlclassifier">*Classifier<wbr>Xml<wbr>Classifier</a></span>
    </dt>
    <dd>{{% md %}}A classifier for XML content. Defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>csv<wbr>Classifier</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#classifiercsvclassifier">Classifier<wbr>Csv<wbr>Classifier?</a></span>
    </dt>
    <dd>{{% md %}}A classifier for Csv content. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>grok<wbr>Classifier</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#classifiergrokclassifier">Classifier<wbr>Grok<wbr>Classifier?</a></span>
    </dt>
    <dd>{{% md %}}A classifier that uses grok patterns. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>json<wbr>Classifier</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#classifierjsonclassifier">Classifier<wbr>Json<wbr>Classifier?</a></span>
    </dt>
    <dd>{{% md %}}A classifier for JSON content. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the classifier.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>xml<wbr>Classifier</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#classifierxmlclassifier">Classifier<wbr>Xml<wbr>Classifier?</a></span>
    </dt>
    <dd>{{% md %}}A classifier for XML content. Defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>csv_<wbr>classifier</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#classifiercsvclassifier">Dict[Classifier<wbr>Csv<wbr>Classifier]</a></span>
    </dt>
    <dd>{{% md %}}A classifier for Csv content. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>grok_<wbr>classifier</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#classifiergrokclassifier">Dict[Classifier<wbr>Grok<wbr>Classifier]</a></span>
    </dt>
    <dd>{{% md %}}A classifier that uses grok patterns. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>json_<wbr>classifier</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#classifierjsonclassifier">Dict[Classifier<wbr>Json<wbr>Classifier]</a></span>
    </dt>
    <dd>{{% md %}}A classifier for JSON content. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the classifier.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>xml_<wbr>classifier</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#classifierxmlclassifier">Dict[Classifier<wbr>Xml<wbr>Classifier]</a></span>
    </dt>
    <dd>{{% md %}}A classifier for XML content. Defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## Classifier Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Csv<wbr>Classifier</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#classifiercsvclassifier">Classifier<wbr>Csv<wbr>Classifier?</a></span>
    </dt>
    <dd>{{% md %}}A classifier for Csv content. Defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Grok<wbr>Classifier</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#classifiergrokclassifier">Classifier<wbr>Grok<wbr>Classifier?</a></span>
    </dt>
    <dd>{{% md %}}A classifier that uses grok patterns. Defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Json<wbr>Classifier</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#classifierjsonclassifier">Classifier<wbr>Json<wbr>Classifier?</a></span>
    </dt>
    <dd>{{% md %}}A classifier for JSON content. Defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the classifier.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Xml<wbr>Classifier</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#classifierxmlclassifier">Classifier<wbr>Xml<wbr>Classifier?</a></span>
    </dt>
    <dd>{{% md %}}A classifier for XML content. Defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Csv<wbr>Classifier</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#classifiercsvclassifier">*Classifier<wbr>Csv<wbr>Classifier</a></span>
    </dt>
    <dd>{{% md %}}A classifier for Csv content. Defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Grok<wbr>Classifier</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#classifiergrokclassifier">*Classifier<wbr>Grok<wbr>Classifier</a></span>
    </dt>
    <dd>{{% md %}}A classifier that uses grok patterns. Defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Json<wbr>Classifier</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#classifierjsonclassifier">*Classifier<wbr>Json<wbr>Classifier</a></span>
    </dt>
    <dd>{{% md %}}A classifier for JSON content. Defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the classifier.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Xml<wbr>Classifier</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#classifierxmlclassifier">*Classifier<wbr>Xml<wbr>Classifier</a></span>
    </dt>
    <dd>{{% md %}}A classifier for XML content. Defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>csv<wbr>Classifier</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#classifiercsvclassifier">Classifier<wbr>Csv<wbr>Classifier?</a></span>
    </dt>
    <dd>{{% md %}}A classifier for Csv content. Defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>grok<wbr>Classifier</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#classifiergrokclassifier">Classifier<wbr>Grok<wbr>Classifier?</a></span>
    </dt>
    <dd>{{% md %}}A classifier that uses grok patterns. Defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>json<wbr>Classifier</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#classifierjsonclassifier">Classifier<wbr>Json<wbr>Classifier?</a></span>
    </dt>
    <dd>{{% md %}}A classifier for JSON content. Defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the classifier.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>xml<wbr>Classifier</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#classifierxmlclassifier">Classifier<wbr>Xml<wbr>Classifier?</a></span>
    </dt>
    <dd>{{% md %}}A classifier for XML content. Defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>csv_<wbr>classifier</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#classifiercsvclassifier">Dict[Classifier<wbr>Csv<wbr>Classifier]</a></span>
    </dt>
    <dd>{{% md %}}A classifier for Csv content. Defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>grok_<wbr>classifier</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#classifiergrokclassifier">Dict[Classifier<wbr>Grok<wbr>Classifier]</a></span>
    </dt>
    <dd>{{% md %}}A classifier that uses grok patterns. Defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>json_<wbr>classifier</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#classifierjsonclassifier">Dict[Classifier<wbr>Json<wbr>Classifier]</a></span>
    </dt>
    <dd>{{% md %}}A classifier for JSON content. Defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the classifier.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>xml_<wbr>classifier</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#classifierxmlclassifier">Dict[Classifier<wbr>Xml<wbr>Classifier]</a></span>
    </dt>
    <dd>{{% md %}}A classifier for XML content. Defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing Classifier Resource

Get an existing Classifier resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/glue/#ClassifierState">ClassifierState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/glue/#Classifier">Classifier</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>csv_classifier=None<span class="p">, </span>grok_classifier=None<span class="p">, </span>json_classifier=None<span class="p">, </span>name=None<span class="p">, </span>xml_classifier=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetClassifier<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/glue?tab=doc#ClassifierState">ClassifierState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/glue?tab=doc#Classifier">Classifier</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Glue.Classifier.html">Classifier</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Glue.ClassifierState.html">ClassifierState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Csv<wbr>Classifier</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#classifiercsvclassifier">Classifier<wbr>Csv<wbr>Classifier<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A classifier for Csv content. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Grok<wbr>Classifier</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#classifiergrokclassifier">Classifier<wbr>Grok<wbr>Classifier<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A classifier that uses grok patterns. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Json<wbr>Classifier</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#classifierjsonclassifier">Classifier<wbr>Json<wbr>Classifier<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A classifier for JSON content. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the classifier.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Xml<wbr>Classifier</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#classifierxmlclassifier">Classifier<wbr>Xml<wbr>Classifier<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A classifier for XML content. Defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Csv<wbr>Classifier</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#classifiercsvclassifier">*Classifier<wbr>Csv<wbr>Classifier</a></span>
    </dt>
    <dd>{{% md %}}A classifier for Csv content. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Grok<wbr>Classifier</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#classifiergrokclassifier">*Classifier<wbr>Grok<wbr>Classifier</a></span>
    </dt>
    <dd>{{% md %}}A classifier that uses grok patterns. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Json<wbr>Classifier</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#classifierjsonclassifier">*Classifier<wbr>Json<wbr>Classifier</a></span>
    </dt>
    <dd>{{% md %}}A classifier for JSON content. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the classifier.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Xml<wbr>Classifier</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#classifierxmlclassifier">*Classifier<wbr>Xml<wbr>Classifier</a></span>
    </dt>
    <dd>{{% md %}}A classifier for XML content. Defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>csv<wbr>Classifier</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#classifiercsvclassifier">Classifier<wbr>Csv<wbr>Classifier?</a></span>
    </dt>
    <dd>{{% md %}}A classifier for Csv content. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>grok<wbr>Classifier</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#classifiergrokclassifier">Classifier<wbr>Grok<wbr>Classifier?</a></span>
    </dt>
    <dd>{{% md %}}A classifier that uses grok patterns. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>json<wbr>Classifier</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#classifierjsonclassifier">Classifier<wbr>Json<wbr>Classifier?</a></span>
    </dt>
    <dd>{{% md %}}A classifier for JSON content. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the classifier.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>xml<wbr>Classifier</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#classifierxmlclassifier">Classifier<wbr>Xml<wbr>Classifier?</a></span>
    </dt>
    <dd>{{% md %}}A classifier for XML content. Defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>csv_<wbr>classifier</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#classifiercsvclassifier">Dict[Classifier<wbr>Csv<wbr>Classifier]</a></span>
    </dt>
    <dd>{{% md %}}A classifier for Csv content. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>grok_<wbr>classifier</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#classifiergrokclassifier">Dict[Classifier<wbr>Grok<wbr>Classifier]</a></span>
    </dt>
    <dd>{{% md %}}A classifier that uses grok patterns. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>json_<wbr>classifier</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#classifierjsonclassifier">Dict[Classifier<wbr>Json<wbr>Classifier]</a></span>
    </dt>
    <dd>{{% md %}}A classifier for JSON content. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the classifier.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>xml_<wbr>classifier</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#classifierxmlclassifier">Dict[Classifier<wbr>Xml<wbr>Classifier]</a></span>
    </dt>
    <dd>{{% md %}}A classifier for XML content. Defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Classifier<wbr>Csv<wbr>Classifier</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ClassifierCsvClassifier">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ClassifierCsvClassifier">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/glue?tab=doc#ClassifierCsvClassifierArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/glue?tab=doc#ClassifierCsvClassifierOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Single<wbr>Column</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Enables the processing of files that contain only one column.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Contains<wbr>Header</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Indicates whether the CSV file contains a header. This can be one of "ABSENT", "PRESENT", or "UNKNOWN".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Delimiter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The delimiter used in the Csv to separate columns.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disable<wbr>Value<wbr>Trimming</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Specifies whether to trim column values. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of strings representing column names.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Quote<wbr>Symbol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A custom symbol to denote what combines content into a single column value. It must be different from the column delimiter.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Single<wbr>Column</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Enables the processing of files that contain only one column.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Contains<wbr>Header</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Indicates whether the CSV file contains a header. This can be one of "ABSENT", "PRESENT", or "UNKNOWN".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Delimiter</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The delimiter used in the Csv to separate columns.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disable<wbr>Value<wbr>Trimming</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Specifies whether to trim column values. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of strings representing column names.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Quote<wbr>Symbol</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A custom symbol to denote what combines content into a single column value. It must be different from the column delimiter.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Single<wbr>Column</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Enables the processing of files that contain only one column.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>contains<wbr>Header</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Indicates whether the CSV file contains a header. This can be one of "ABSENT", "PRESENT", or "UNKNOWN".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>delimiter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The delimiter used in the Csv to separate columns.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disable<wbr>Value<wbr>Trimming</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Specifies whether to trim column values. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of strings representing column names.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>quote<wbr>Symbol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A custom symbol to denote what combines content into a single column value. It must be different from the column delimiter.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Single<wbr>Column</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enables the processing of files that contain only one column.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>contains<wbr>Header</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Indicates whether the CSV file contains a header. This can be one of "ABSENT", "PRESENT", or "UNKNOWN".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>delimiter</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The delimiter used in the Csv to separate columns.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disable<wbr>Value<wbr>Trimming</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Specifies whether to trim column values. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of strings representing column names.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>quote<wbr>Symbol</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A custom symbol to denote what combines content into a single column value. It must be different from the column delimiter.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Classifier<wbr>Grok<wbr>Classifier</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ClassifierGrokClassifier">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ClassifierGrokClassifier">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/glue?tab=doc#ClassifierGrokClassifierArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/glue?tab=doc#ClassifierGrokClassifierOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Classification</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}An identifier of the data format that the classifier matches.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Custom<wbr>Patterns</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Custom grok patterns used by this classifier.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Grok<wbr>Pattern</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The grok pattern used by this classifier.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Classification</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}An identifier of the data format that the classifier matches.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Custom<wbr>Patterns</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Custom grok patterns used by this classifier.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Grok<wbr>Pattern</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The grok pattern used by this classifier.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>classification</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}An identifier of the data format that the classifier matches.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>custom<wbr>Patterns</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Custom grok patterns used by this classifier.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>grok<wbr>Pattern</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The grok pattern used by this classifier.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>classification</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}An identifier of the data format that the classifier matches.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>custom<wbr>Patterns</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Custom grok patterns used by this classifier.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>grok<wbr>Pattern</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The grok pattern used by this classifier.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Classifier<wbr>Json<wbr>Classifier</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ClassifierJsonClassifier">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ClassifierJsonClassifier">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/glue?tab=doc#ClassifierJsonClassifierArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/glue?tab=doc#ClassifierJsonClassifierOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Json<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A `JsonPath` string defining the JSON data for the classifier to classify. AWS Glue supports a subset of `JsonPath`, as described in [Writing JsonPath Custom Classifiers](https://docs.aws.amazon.com/glue/latest/dg/custom-classifier.html#custom-classifier-json).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Json<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A `JsonPath` string defining the JSON data for the classifier to classify. AWS Glue supports a subset of `JsonPath`, as described in [Writing JsonPath Custom Classifiers](https://docs.aws.amazon.com/glue/latest/dg/custom-classifier.html#custom-classifier-json).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>json<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A `JsonPath` string defining the JSON data for the classifier to classify. AWS Glue supports a subset of `JsonPath`, as described in [Writing JsonPath Custom Classifiers](https://docs.aws.amazon.com/glue/latest/dg/custom-classifier.html#custom-classifier-json).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>json<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A `JsonPath` string defining the JSON data for the classifier to classify. AWS Glue supports a subset of `JsonPath`, as described in [Writing JsonPath Custom Classifiers](https://docs.aws.amazon.com/glue/latest/dg/custom-classifier.html#custom-classifier-json).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Classifier<wbr>Xml<wbr>Classifier</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ClassifierXmlClassifier">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ClassifierXmlClassifier">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/glue?tab=doc#ClassifierXmlClassifierArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/glue?tab=doc#ClassifierXmlClassifierOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Classification</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}An identifier of the data format that the classifier matches.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Row<wbr>Tag</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The XML tag designating the element that contains each record in an XML document being parsed. Note that this cannot identify a self-closing element (closed by `/>`). An empty row element that contains only attributes can be parsed as long as it ends with a closing tag (for example, `<row item_a="A" item_b="B"></row>` is okay, but `<row item_a="A" item_b="B" />` is not).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Classification</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}An identifier of the data format that the classifier matches.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Row<wbr>Tag</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The XML tag designating the element that contains each record in an XML document being parsed. Note that this cannot identify a self-closing element (closed by `/>`). An empty row element that contains only attributes can be parsed as long as it ends with a closing tag (for example, `<row item_a="A" item_b="B"></row>` is okay, but `<row item_a="A" item_b="B" />` is not).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>classification</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}An identifier of the data format that the classifier matches.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>row<wbr>Tag</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The XML tag designating the element that contains each record in an XML document being parsed. Note that this cannot identify a self-closing element (closed by `/>`). An empty row element that contains only attributes can be parsed as long as it ends with a closing tag (for example, `<row item_a="A" item_b="B"></row>` is okay, but `<row item_a="A" item_b="B" />` is not).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>classification</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}An identifier of the data format that the classifier matches.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>row<wbr>Tag</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The XML tag designating the element that contains each record in an XML document being parsed. Note that this cannot identify a self-closing element (closed by `/>`). An empty row element that contains only attributes can be parsed as long as it ends with a closing tag (for example, `<row item_a="A" item_b="B"></row>` is okay, but `<row item_a="A" item_b="B" />` is not).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-aws">https://github.com/pulumi/pulumi-aws</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd></dl>
