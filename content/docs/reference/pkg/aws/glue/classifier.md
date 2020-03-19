
---
title: "Classifier"
block_external_search_index: true
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>

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

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/glue/#Classifier">Classifier</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/glue/#ClassifierArgs">ClassifierArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Classifier</span><span class="p">(resource_name, opts=None, </span>csv_classifier=None<span class="p">, </span>grok_classifier=None<span class="p">, </span>json_classifier=None<span class="p">, </span>name=None<span class="p">, </span>xml_classifier=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewClassifier<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/glue?tab=doc#ClassifierArgs">ClassifierArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/glue?tab=doc#Classifier">Classifier</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Glue.Classifier.html">Classifier</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Glue.ClassifierArgs.html">ClassifierArgs</a></span>? <span class="nx">args = null<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a Classifier resource with the given unique name, arguments, and options.

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
            <td class="align-top">Csv<wbr>Classifier</td>
            <td class="align-top">
                
                <code><a href="#classifiercsvclassifier">Pulumi.<wbr>Aws.<wbr>Glue.<wbr>Classifier<wbr>Csv<wbr>Classifier<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A classifier for Csv content. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Grok<wbr>Classifier</td>
            <td class="align-top">
                
                <code><a href="#classifiergrokclassifier">Pulumi.<wbr>Aws.<wbr>Glue.<wbr>Classifier<wbr>Grok<wbr>Classifier<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A classifier that uses grok patterns. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Json<wbr>Classifier</td>
            <td class="align-top">
                
                <code><a href="#classifierjsonclassifier">Pulumi.<wbr>Aws.<wbr>Glue.<wbr>Classifier<wbr>Json<wbr>Classifier<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A classifier for JSON content. Defined below.
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
The name of the classifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Xml<wbr>Classifier</td>
            <td class="align-top">
                
                <code><a href="#classifierxmlclassifier">Pulumi.<wbr>Aws.<wbr>Glue.<wbr>Classifier<wbr>Xml<wbr>Classifier<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A classifier for XML content. Defined below.
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
            <td class="align-top">Csv<wbr>Classifier</td>
            <td class="align-top">
                
                <code><a href="#classifiercsvclassifier">*glue.<wbr>Classifier<wbr>Csv<wbr>Classifier</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A classifier for Csv content. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Grok<wbr>Classifier</td>
            <td class="align-top">
                
                <code><a href="#classifiergrokclassifier">*glue.<wbr>Classifier<wbr>Grok<wbr>Classifier</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A classifier that uses grok patterns. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Json<wbr>Classifier</td>
            <td class="align-top">
                
                <code><a href="#classifierjsonclassifier">*glue.<wbr>Classifier<wbr>Json<wbr>Classifier</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A classifier for JSON content. Defined below.
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
The name of the classifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Xml<wbr>Classifier</td>
            <td class="align-top">
                
                <code><a href="#classifierxmlclassifier">*glue.<wbr>Classifier<wbr>Xml<wbr>Classifier</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A classifier for XML content. Defined below.
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
            <td class="align-top">csv<wbr>Classifier</td>
            <td class="align-top">
                
                <code><a href="#classifiercsvclassifier">glue.<wbr>Classifier<wbr>Csv<wbr>Classifier?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A classifier for Csv content. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">grok<wbr>Classifier</td>
            <td class="align-top">
                
                <code><a href="#classifiergrokclassifier">glue.<wbr>Classifier<wbr>Grok<wbr>Classifier?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A classifier that uses grok patterns. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">json<wbr>Classifier</td>
            <td class="align-top">
                
                <code><a href="#classifierjsonclassifier">glue.<wbr>Classifier<wbr>Json<wbr>Classifier?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A classifier for JSON content. Defined below.
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
The name of the classifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">xml<wbr>Classifier</td>
            <td class="align-top">
                
                <code><a href="#classifierxmlclassifier">glue.<wbr>Classifier<wbr>Xml<wbr>Classifier?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A classifier for XML content. Defined below.
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
            <td class="align-top">csv_<wbr>classifier</td>
            <td class="align-top">
                
                <code><a href="#classifiercsvclassifier">Dict[Classifier<wbr>Csv<wbr>Classifier]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A classifier for Csv content. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">grok_<wbr>classifier</td>
            <td class="align-top">
                
                <code><a href="#classifiergrokclassifier">Dict[Classifier<wbr>Grok<wbr>Classifier]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A classifier that uses grok patterns. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">json_<wbr>classifier</td>
            <td class="align-top">
                
                <code><a href="#classifierjsonclassifier">Dict[Classifier<wbr>Json<wbr>Classifier]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A classifier for JSON content. Defined below.
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
The name of the classifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">xml_<wbr>classifier</td>
            <td class="align-top">
                
                <code><a href="#classifierxmlclassifier">Dict[Classifier<wbr>Xml<wbr>Classifier]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A classifier for XML content. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## Classifier Output Properties

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
            <td class="align-top">Csv<wbr>Classifier</td>
            <td class="align-top">
                
                <code><a href="#classifiercsvclassifier">Pulumi.<wbr>Aws.<wbr>Glue.<wbr>Classifier<wbr>Csv<wbr>Classifier?</a></code>
            </td>
            <td class="align-top">{{% md %}} A classifier for Csv content. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Grok<wbr>Classifier</td>
            <td class="align-top">
                
                <code><a href="#classifiergrokclassifier">Pulumi.<wbr>Aws.<wbr>Glue.<wbr>Classifier<wbr>Grok<wbr>Classifier?</a></code>
            </td>
            <td class="align-top">{{% md %}} A classifier that uses grok patterns. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Json<wbr>Classifier</td>
            <td class="align-top">
                
                <code><a href="#classifierjsonclassifier">Pulumi.<wbr>Aws.<wbr>Glue.<wbr>Classifier<wbr>Json<wbr>Classifier?</a></code>
            </td>
            <td class="align-top">{{% md %}} A classifier for JSON content. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the classifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Xml<wbr>Classifier</td>
            <td class="align-top">
                
                <code><a href="#classifierxmlclassifier">Pulumi.<wbr>Aws.<wbr>Glue.<wbr>Classifier<wbr>Xml<wbr>Classifier?</a></code>
            </td>
            <td class="align-top">{{% md %}} A classifier for XML content. Defined below.
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
            <td class="align-top">Csv<wbr>Classifier</td>
            <td class="align-top">
                
                <code><a href="#classifiercsvclassifier">*glue.<wbr>Classifier<wbr>Csv<wbr>Classifier</a></code>
            </td>
            <td class="align-top">{{% md %}} A classifier for Csv content. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Grok<wbr>Classifier</td>
            <td class="align-top">
                
                <code><a href="#classifiergrokclassifier">*glue.<wbr>Classifier<wbr>Grok<wbr>Classifier</a></code>
            </td>
            <td class="align-top">{{% md %}} A classifier that uses grok patterns. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Json<wbr>Classifier</td>
            <td class="align-top">
                
                <code><a href="#classifierjsonclassifier">*glue.<wbr>Classifier<wbr>Json<wbr>Classifier</a></code>
            </td>
            <td class="align-top">{{% md %}} A classifier for JSON content. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the classifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Xml<wbr>Classifier</td>
            <td class="align-top">
                
                <code><a href="#classifierxmlclassifier">*glue.<wbr>Classifier<wbr>Xml<wbr>Classifier</a></code>
            </td>
            <td class="align-top">{{% md %}} A classifier for XML content. Defined below.
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
            <td class="align-top">csv<wbr>Classifier</td>
            <td class="align-top">
                
                <code><a href="#classifiercsvclassifier">glue.<wbr>Classifier<wbr>Csv<wbr>Classifier?</a></code>
            </td>
            <td class="align-top">{{% md %}} A classifier for Csv content. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">grok<wbr>Classifier</td>
            <td class="align-top">
                
                <code><a href="#classifiergrokclassifier">glue.<wbr>Classifier<wbr>Grok<wbr>Classifier?</a></code>
            </td>
            <td class="align-top">{{% md %}} A classifier that uses grok patterns. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">json<wbr>Classifier</td>
            <td class="align-top">
                
                <code><a href="#classifierjsonclassifier">glue.<wbr>Classifier<wbr>Json<wbr>Classifier?</a></code>
            </td>
            <td class="align-top">{{% md %}} A classifier for JSON content. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the classifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">xml<wbr>Classifier</td>
            <td class="align-top">
                
                <code><a href="#classifierxmlclassifier">glue.<wbr>Classifier<wbr>Xml<wbr>Classifier?</a></code>
            </td>
            <td class="align-top">{{% md %}} A classifier for XML content. Defined below.
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
            <td class="align-top">csv_<wbr>classifier</td>
            <td class="align-top">
                
                <code><a href="#classifiercsvclassifier">Dict[Classifier<wbr>Csv<wbr>Classifier]</a></code>
            </td>
            <td class="align-top">{{% md %}} A classifier for Csv content. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">grok_<wbr>classifier</td>
            <td class="align-top">
                
                <code><a href="#classifiergrokclassifier">Dict[Classifier<wbr>Grok<wbr>Classifier]</a></code>
            </td>
            <td class="align-top">{{% md %}} A classifier that uses grok patterns. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">json_<wbr>classifier</td>
            <td class="align-top">
                
                <code><a href="#classifierjsonclassifier">Dict[Classifier<wbr>Json<wbr>Classifier]</a></code>
            </td>
            <td class="align-top">{{% md %}} A classifier for JSON content. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of the classifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">xml_<wbr>classifier</td>
            <td class="align-top">
                
                <code><a href="#classifierxmlclassifier">Dict[Classifier<wbr>Xml<wbr>Classifier]</a></code>
            </td>
            <td class="align-top">{{% md %}} A classifier for XML content. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing Classifier Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/glue/#ClassifierState">ClassifierState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/glue/#Classifier">Classifier</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>csv_classifier=None<span class="p">, </span>grok_classifier=None<span class="p">, </span>json_classifier=None<span class="p">, </span>name=None<span class="p">, </span>xml_classifier=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetClassifier<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/glue?tab=doc#ClassifierState">ClassifierState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/glue?tab=doc#Classifier">Classifier</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Glue.Classifier.html">Classifier</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Glue.ClassifierState.html">ClassifierState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Get an existing Classifier resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
            <td class="align-top">Csv<wbr>Classifier</td>
            <td class="align-top">
                
                <code><a href="#classifiercsvclassifier">Pulumi.<wbr>Aws.<wbr>Glue.<wbr>Classifier<wbr>Csv<wbr>Classifier<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A classifier for Csv content. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Grok<wbr>Classifier</td>
            <td class="align-top">
                
                <code><a href="#classifiergrokclassifier">Pulumi.<wbr>Aws.<wbr>Glue.<wbr>Classifier<wbr>Grok<wbr>Classifier<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A classifier that uses grok patterns. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Json<wbr>Classifier</td>
            <td class="align-top">
                
                <code><a href="#classifierjsonclassifier">Pulumi.<wbr>Aws.<wbr>Glue.<wbr>Classifier<wbr>Json<wbr>Classifier<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A classifier for JSON content. Defined below.
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
The name of the classifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Xml<wbr>Classifier</td>
            <td class="align-top">
                
                <code><a href="#classifierxmlclassifier">Pulumi.<wbr>Aws.<wbr>Glue.<wbr>Classifier<wbr>Xml<wbr>Classifier<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A classifier for XML content. Defined below.
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
            <td class="align-top">Csv<wbr>Classifier</td>
            <td class="align-top">
                
                <code><a href="#classifiercsvclassifier">*glue.<wbr>Classifier<wbr>Csv<wbr>Classifier</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A classifier for Csv content. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Grok<wbr>Classifier</td>
            <td class="align-top">
                
                <code><a href="#classifiergrokclassifier">*glue.<wbr>Classifier<wbr>Grok<wbr>Classifier</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A classifier that uses grok patterns. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Json<wbr>Classifier</td>
            <td class="align-top">
                
                <code><a href="#classifierjsonclassifier">*glue.<wbr>Classifier<wbr>Json<wbr>Classifier</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A classifier for JSON content. Defined below.
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
The name of the classifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Xml<wbr>Classifier</td>
            <td class="align-top">
                
                <code><a href="#classifierxmlclassifier">*glue.<wbr>Classifier<wbr>Xml<wbr>Classifier</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A classifier for XML content. Defined below.
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
            <td class="align-top">csv<wbr>Classifier</td>
            <td class="align-top">
                
                <code><a href="#classifiercsvclassifier">glue.<wbr>Classifier<wbr>Csv<wbr>Classifier?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A classifier for Csv content. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">grok<wbr>Classifier</td>
            <td class="align-top">
                
                <code><a href="#classifiergrokclassifier">glue.<wbr>Classifier<wbr>Grok<wbr>Classifier?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A classifier that uses grok patterns. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">json<wbr>Classifier</td>
            <td class="align-top">
                
                <code><a href="#classifierjsonclassifier">glue.<wbr>Classifier<wbr>Json<wbr>Classifier?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A classifier for JSON content. Defined below.
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
The name of the classifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">xml<wbr>Classifier</td>
            <td class="align-top">
                
                <code><a href="#classifierxmlclassifier">glue.<wbr>Classifier<wbr>Xml<wbr>Classifier?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A classifier for XML content. Defined below.
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
            <td class="align-top">csv_<wbr>classifier</td>
            <td class="align-top">
                
                <code><a href="#classifiercsvclassifier">Dict[Classifier<wbr>Csv<wbr>Classifier]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A classifier for Csv content. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">grok_<wbr>classifier</td>
            <td class="align-top">
                
                <code><a href="#classifiergrokclassifier">Dict[Classifier<wbr>Grok<wbr>Classifier]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A classifier that uses grok patterns. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">json_<wbr>classifier</td>
            <td class="align-top">
                
                <code><a href="#classifierjsonclassifier">Dict[Classifier<wbr>Json<wbr>Classifier]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A classifier for JSON content. Defined below.
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
The name of the classifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">xml_<wbr>classifier</td>
            <td class="align-top">
                
                <code><a href="#classifierxmlclassifier">Dict[Classifier<wbr>Xml<wbr>Classifier]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A classifier for XML content. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### ClassifierCsvClassifier
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ClassifierCsvClassifier">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ClassifierCsvClassifier">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/glue?tab=doc#ClassifierCsvClassifierArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/glue?tab=doc#ClassifierCsvClassifierOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Glue.ClassifierCsvClassifierArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Glue.ClassifierCsvClassifier.html">output</a> API doc for this type.
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
            <td class="align-top">Allow<wbr>Single<wbr>Column</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Enables the processing of files that contain only one column.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Contains<wbr>Header</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether the CSV file contains a header. This can be one of &#34;ABSENT&#34;, &#34;PRESENT&#34;, or &#34;UNKNOWN&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Delimiter</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The delimiter used in the Csv to separate columns.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Disable<wbr>Value<wbr>Trimming</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether to trim column values. 
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Headers</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of strings representing column names.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Quote<wbr>Symbol</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A custom symbol to denote what combines content into a single column value. It must be different from the column delimiter.
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
            <td class="align-top">Allow<wbr>Single<wbr>Column</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Enables the processing of files that contain only one column.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Contains<wbr>Header</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether the CSV file contains a header. This can be one of &#34;ABSENT&#34;, &#34;PRESENT&#34;, or &#34;UNKNOWN&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Delimiter</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The delimiter used in the Csv to separate columns.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Disable<wbr>Value<wbr>Trimming</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether to trim column values. 
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Headers</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of strings representing column names.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Quote<wbr>Symbol</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A custom symbol to denote what combines content into a single column value. It must be different from the column delimiter.
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
            <td class="align-top">allow<wbr>Single<wbr>Column</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Enables the processing of files that contain only one column.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">contains<wbr>Header</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether the CSV file contains a header. This can be one of &#34;ABSENT&#34;, &#34;PRESENT&#34;, or &#34;UNKNOWN&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">delimiter</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The delimiter used in the Csv to separate columns.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">disable<wbr>Value<wbr>Trimming</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether to trim column values. 
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">headers</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of strings representing column names.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">quote<wbr>Symbol</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A custom symbol to denote what combines content into a single column value. It must be different from the column delimiter.
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
            <td class="align-top">allow<wbr>Single<wbr>Column</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Enables the processing of files that contain only one column.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">contains<wbr>Header</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether the CSV file contains a header. This can be one of &#34;ABSENT&#34;, &#34;PRESENT&#34;, or &#34;UNKNOWN&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">delimiter</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The delimiter used in the Csv to separate columns.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">disable<wbr>Value<wbr>Trimming</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether to trim column values. 
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">headers</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of strings representing column names.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">quote<wbr>Symbol</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A custom symbol to denote what combines content into a single column value. It must be different from the column delimiter.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### ClassifierGrokClassifier
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ClassifierGrokClassifier">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ClassifierGrokClassifier">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/glue?tab=doc#ClassifierGrokClassifierArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/glue?tab=doc#ClassifierGrokClassifierOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Glue.ClassifierGrokClassifierArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Glue.ClassifierGrokClassifier.html">output</a> API doc for this type.
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
            <td class="align-top">Classification</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
An identifier of the data format that the classifier matches.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Custom<wbr>Patterns</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Custom grok patterns used by this classifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Grok<wbr>Pattern</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The grok pattern used by this classifier.
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
            <td class="align-top">Classification</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
An identifier of the data format that the classifier matches.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Custom<wbr>Patterns</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Custom grok patterns used by this classifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Grok<wbr>Pattern</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The grok pattern used by this classifier.
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
            <td class="align-top">classification</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
An identifier of the data format that the classifier matches.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">custom<wbr>Patterns</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Custom grok patterns used by this classifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">grok<wbr>Pattern</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The grok pattern used by this classifier.
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
            <td class="align-top">classification</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
An identifier of the data format that the classifier matches.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">custom<wbr>Patterns</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Custom grok patterns used by this classifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">grok<wbr>Pattern</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The grok pattern used by this classifier.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### ClassifierJsonClassifier
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ClassifierJsonClassifier">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ClassifierJsonClassifier">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/glue?tab=doc#ClassifierJsonClassifierArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/glue?tab=doc#ClassifierJsonClassifierOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Glue.ClassifierJsonClassifierArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Glue.ClassifierJsonClassifier.html">output</a> API doc for this type.
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
            <td class="align-top">Json<wbr>Path</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A `JsonPath` string defining the JSON data for the classifier to classify. AWS Glue supports a subset of `JsonPath`, as described in [Writing JsonPath Custom Classifiers](https://docs.aws.amazon.com/glue/latest/dg/custom-classifier.html#custom-classifier-json).
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
            <td class="align-top">Json<wbr>Path</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A `JsonPath` string defining the JSON data for the classifier to classify. AWS Glue supports a subset of `JsonPath`, as described in [Writing JsonPath Custom Classifiers](https://docs.aws.amazon.com/glue/latest/dg/custom-classifier.html#custom-classifier-json).
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
            <td class="align-top">json<wbr>Path</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A `JsonPath` string defining the JSON data for the classifier to classify. AWS Glue supports a subset of `JsonPath`, as described in [Writing JsonPath Custom Classifiers](https://docs.aws.amazon.com/glue/latest/dg/custom-classifier.html#custom-classifier-json).
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
            <td class="align-top">json<wbr>Path</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A `JsonPath` string defining the JSON data for the classifier to classify. AWS Glue supports a subset of `JsonPath`, as described in [Writing JsonPath Custom Classifiers](https://docs.aws.amazon.com/glue/latest/dg/custom-classifier.html#custom-classifier-json).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### ClassifierXmlClassifier
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ClassifierXmlClassifier">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ClassifierXmlClassifier">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/glue?tab=doc#ClassifierXmlClassifierArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/glue?tab=doc#ClassifierXmlClassifierOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Glue.ClassifierXmlClassifierArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Glue.ClassifierXmlClassifier.html">output</a> API doc for this type.
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
            <td class="align-top">Classification</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
An identifier of the data format that the classifier matches.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Row<wbr>Tag</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The XML tag designating the element that contains each record in an XML document being parsed. Note that this cannot identify a self-closing element (closed by `/&gt;`). An empty row element that contains only attributes can be parsed as long as it ends with a closing tag (for example, `&lt;row item_a=&#34;A&#34; item_b=&#34;B&#34;&gt;&lt;/row&gt;` is okay, but `&lt;row item_a=&#34;A&#34; item_b=&#34;B&#34; /&gt;` is not).
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
            <td class="align-top">Classification</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
An identifier of the data format that the classifier matches.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Row<wbr>Tag</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The XML tag designating the element that contains each record in an XML document being parsed. Note that this cannot identify a self-closing element (closed by `/&gt;`). An empty row element that contains only attributes can be parsed as long as it ends with a closing tag (for example, `&lt;row item_a=&#34;A&#34; item_b=&#34;B&#34;&gt;&lt;/row&gt;` is okay, but `&lt;row item_a=&#34;A&#34; item_b=&#34;B&#34; /&gt;` is not).
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
            <td class="align-top">classification</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
An identifier of the data format that the classifier matches.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">row<wbr>Tag</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The XML tag designating the element that contains each record in an XML document being parsed. Note that this cannot identify a self-closing element (closed by `/&gt;`). An empty row element that contains only attributes can be parsed as long as it ends with a closing tag (for example, `&lt;row item_a=&#34;A&#34; item_b=&#34;B&#34;&gt;&lt;/row&gt;` is okay, but `&lt;row item_a=&#34;A&#34; item_b=&#34;B&#34; /&gt;` is not).
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
            <td class="align-top">classification</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
An identifier of the data format that the classifier matches.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">row<wbr>Tag</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The XML tag designating the element that contains each record in an XML document being parsed. Note that this cannot identify a self-closing element (closed by `/&gt;`). An empty row element that contains only attributes can be parsed as long as it ends with a closing tag (for example, `&lt;row item_a=&#34;A&#34; item_b=&#34;B&#34;&gt;&lt;/row&gt;` is okay, but `&lt;row item_a=&#34;A&#34; item_b=&#34;B&#34; /&gt;` is not).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







