
---
title: "GetScript"
block_external_search_index: true
---

Use this data source to generate a Glue script from a Directed Acyclic Graph (DAG).

## Example Usage

### Generate Python Script

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const example = pulumi.all([aws_glue_catalog_database_source.name, aws_glue_catalog_table_source.name, aws_glue_catalog_database_destination.name, aws_glue_catalog_table_destination.name, aws_glue_catalog_database_destination.name, aws_glue_catalog_table_destination.name]).apply(([aws_glue_catalog_database_sourceName, aws_glue_catalog_table_sourceName, aws_glue_catalog_database_destinationName, aws_glue_catalog_table_destinationName, aws_glue_catalog_database_destinationName1, aws_glue_catalog_table_destinationName1]) => aws.glue.getScript({
    dagEdges: [
        {
            source: "datasource0",
            target: "applymapping1",
        },
        {
            source: "applymapping1",
            target: "selectfields2",
        },
        {
            source: "selectfields2",
            target: "resolvechoice3",
        },
        {
            source: "resolvechoice3",
            target: "datasink4",
        },
    ],
    dagNodes: [
        {
            args: [
                {
                    name: "database",
                    value: `"${aws_glue_catalog_database_sourceName}"`,
                },
                {
                    name: "table_name",
                    value: `"${aws_glue_catalog_table_sourceName}"`,
                },
            ],
            id: "datasource0",
            nodeType: "DataSource",
        },
        {
            args: [{
                name: "mapping",
                value: "[(\"column1\", \"string\", \"column1\", \"string\")]",
            }],
            id: "applymapping1",
            nodeType: "ApplyMapping",
        },
        {
            args: [{
                name: "paths",
                value: "[\"column1\"]",
            }],
            id: "selectfields2",
            nodeType: "SelectFields",
        },
        {
            args: [
                {
                    name: "choice",
                    value: "\"MATCH_CATALOG\"",
                },
                {
                    name: "database",
                    value: `"${aws_glue_catalog_database_destinationName}"`,
                },
                {
                    name: "table_name",
                    value: `"${aws_glue_catalog_table_destinationName}"`,
                },
            ],
            id: "resolvechoice3",
            nodeType: "ResolveChoice",
        },
        {
            args: [
                {
                    name: "database",
                    value: `"${aws_glue_catalog_database_destinationName1}"`,
                },
                {
                    name: "table_name",
                    value: `"${aws_glue_catalog_table_destinationName1}"`,
                },
            ],
            id: "datasink4",
            nodeType: "DataSink",
        },
    ],
    language: "PYTHON",
}));

export const pythonScript = example.pythonScript;
```

### Generate Scala Code

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const example = pulumi.all([aws_glue_catalog_database_source.name, aws_glue_catalog_table_source.name, aws_glue_catalog_database_destination.name, aws_glue_catalog_table_destination.name, aws_glue_catalog_database_destination.name, aws_glue_catalog_table_destination.name]).apply(([aws_glue_catalog_database_sourceName, aws_glue_catalog_table_sourceName, aws_glue_catalog_database_destinationName, aws_glue_catalog_table_destinationName, aws_glue_catalog_database_destinationName1, aws_glue_catalog_table_destinationName1]) => aws.glue.getScript({
    dagEdges: [
        {
            source: "datasource0",
            target: "applymapping1",
        },
        {
            source: "applymapping1",
            target: "selectfields2",
        },
        {
            source: "selectfields2",
            target: "resolvechoice3",
        },
        {
            source: "resolvechoice3",
            target: "datasink4",
        },
    ],
    dagNodes: [
        {
            args: [
                {
                    name: "database",
                    value: `"${aws_glue_catalog_database_sourceName}"`,
                },
                {
                    name: "table_name",
                    value: `"${aws_glue_catalog_table_sourceName}"`,
                },
            ],
            id: "datasource0",
            nodeType: "DataSource",
        },
        {
            args: [{
                name: "mappings",
                value: "[(\"column1\", \"string\", \"column1\", \"string\")]",
            }],
            id: "applymapping1",
            nodeType: "ApplyMapping",
        },
        {
            args: [{
                name: "paths",
                value: "[\"column1\"]",
            }],
            id: "selectfields2",
            nodeType: "SelectFields",
        },
        {
            args: [
                {
                    name: "choice",
                    value: "\"MATCH_CATALOG\"",
                },
                {
                    name: "database",
                    value: `"${aws_glue_catalog_database_destinationName}"`,
                },
                {
                    name: "table_name",
                    value: `"${aws_glue_catalog_table_destinationName}"`,
                },
            ],
            id: "resolvechoice3",
            nodeType: "ResolveChoice",
        },
        {
            args: [
                {
                    name: "database",
                    value: `"${aws_glue_catalog_database_destinationName1}"`,
                },
                {
                    name: "table_name",
                    value: `"${aws_glue_catalog_table_destinationName1}"`,
                },
            ],
            id: "datasink4",
            nodeType: "DataSink",
        },
    ],
    language: "SCALA",
}));

export const scalaCode = example.scalaCode;
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/glue_script.html.markdown.





## Using GetScript

{{< chooser language "javascript,typescript,python,go,csharp" / >}}


{{% choosable language typescript %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getScript<span class="p">(</span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/glue/#GetScriptArgs">GetScriptArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#InvokeOptions">pulumi.InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/glue/#GetScriptResult">GetScriptResult</a></span>></span></code></pre></div>
{{% /choosable %}}


{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_script(</span>dag_edges=None<span class="p">, </span>dag_nodes=None<span class="p">, </span>language=None<span class="p">, </span>opts=None<span class="p">)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupScript<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/glue?tab=doc#LookupScriptArgs">LookupScriptArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#InvokeOption">pulumi.InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/glue?tab=doc#LookupScriptResult">LookupScriptResult</a></span>, error)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static class </span><span class="nx">GetScript </span><span class="p">{</span><span class="k">public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Glue.GetScriptResult.html">GetScriptResult</a></span>> <span class="p">InvokeAsync(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Glue.Inputs.GetScriptArgs.html">GetScriptArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.InvokeOptions.html">Pulumi.InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span><span class="p">}</span></code></pre></div>
{{% /choosable %}}



The following arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Dag<wbr>Edges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getscriptdagedge">List&lt;Get<wbr>Script<wbr>Dag<wbr>Edge<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}A list of the edges in the DAG. Defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Dag<wbr>Nodes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getscriptdagnode">List&lt;Get<wbr>Script<wbr>Dag<wbr>Node<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}A list of the nodes in the DAG. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Language</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The programming language of the resulting code from the DAG. Defaults to `PYTHON`. Valid values are `PYTHON` and `SCALA`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Dag<wbr>Edges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getscriptdagedge">[]Get<wbr>Script<wbr>Dag<wbr>Edge</a></span>
    </dt>
    <dd>{{% md %}}A list of the edges in the DAG. Defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Dag<wbr>Nodes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getscriptdagnode">[]Get<wbr>Script<wbr>Dag<wbr>Node</a></span>
    </dt>
    <dd>{{% md %}}A list of the nodes in the DAG. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Language</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The programming language of the resulting code from the DAG. Defaults to `PYTHON`. Valid values are `PYTHON` and `SCALA`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>dag<wbr>Edges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getscriptdagedge">Get<wbr>Script<wbr>Dag<wbr>Edge[]</a></span>
    </dt>
    <dd>{{% md %}}A list of the edges in the DAG. Defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>dag<wbr>Nodes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getscriptdagnode">Get<wbr>Script<wbr>Dag<wbr>Node[]</a></span>
    </dt>
    <dd>{{% md %}}A list of the nodes in the DAG. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>language</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The programming language of the resulting code from the DAG. Defaults to `PYTHON`. Valid values are `PYTHON` and `SCALA`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>dag_<wbr>edges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getscriptdagedge">List[Get<wbr>Script<wbr>Dag<wbr>Edge]</a></span>
    </dt>
    <dd>{{% md %}}A list of the edges in the DAG. Defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>dag_<wbr>nodes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getscriptdagnode">List[Get<wbr>Script<wbr>Dag<wbr>Node]</a></span>
    </dt>
    <dd>{{% md %}}A list of the nodes in the DAG. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>language</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The programming language of the resulting code from the DAG. Defaults to `PYTHON`. Valid values are `PYTHON` and `SCALA`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## GetScript Result

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Dag<wbr>Edges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getscriptdagedge">List&lt;Get<wbr>Script<wbr>Dag<wbr>Edge&gt;</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Dag<wbr>Nodes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getscriptdagnode">List&lt;Get<wbr>Script<wbr>Dag<wbr>Node&gt;</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Language</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Python<wbr>Script</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Python script generated from the DAG when the `language` argument is set to `PYTHON`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Scala<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Scala code generated from the DAG when the `language` argument is set to `SCALA`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Dag<wbr>Edges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getscriptdagedge">[]Get<wbr>Script<wbr>Dag<wbr>Edge</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Dag<wbr>Nodes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getscriptdagnode">[]Get<wbr>Script<wbr>Dag<wbr>Node</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Language</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Python<wbr>Script</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Python script generated from the DAG when the `language` argument is set to `PYTHON`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Scala<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Scala code generated from the DAG when the `language` argument is set to `SCALA`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>dag<wbr>Edges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getscriptdagedge">Get<wbr>Script<wbr>Dag<wbr>Edge[]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>dag<wbr>Nodes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getscriptdagnode">Get<wbr>Script<wbr>Dag<wbr>Node[]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>language</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>python<wbr>Script</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Python script generated from the DAG when the `language` argument is set to `PYTHON`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>scala<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Scala code generated from the DAG when the `language` argument is set to `SCALA`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>dag_<wbr>edges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getscriptdagedge">List[Get<wbr>Script<wbr>Dag<wbr>Edge]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>dag_<wbr>nodes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getscriptdagnode">List[Get<wbr>Script<wbr>Dag<wbr>Node]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>language</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>python_<wbr>script</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Python script generated from the DAG when the `language` argument is set to `PYTHON`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>scala_<wbr>code</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Scala code generated from the DAG when the `language` argument is set to `SCALA`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Supporting Types

#### Get&lt;wbr&gt;Script&lt;wbr&gt;Dag&lt;wbr&gt;Edge
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#GetScriptDagEdge">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GetScriptDagEdge">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/glue?tab=doc#GetScriptDagEdgeArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/glue?tab=doc#GetScriptDagEdge">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Source</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the node at which the edge starts.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Target</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the node at which the edge ends.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>Parameter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The target of the edge.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Source</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the node at which the edge starts.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Target</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the node at which the edge ends.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>Parameter</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The target of the edge.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>source</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the node at which the edge starts.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>target</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the node at which the edge ends.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target<wbr>Parameter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The target of the edge.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>source</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the node at which the edge starts.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>target</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the node at which the edge ends.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target<wbr>Parameter</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The target of the edge.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





#### Get&lt;wbr&gt;Script&lt;wbr&gt;Dag&lt;wbr&gt;Node
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#GetScriptDagNode">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GetScriptDagNode">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/glue?tab=doc#GetScriptDagNodeArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/glue?tab=doc#GetScriptDagNode">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Args</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getscriptdagnodearg">List&lt;Get<wbr>Script<wbr>Dag<wbr>Node<wbr>Arg<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}Nested configuration an argument or property of a node. Defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A node identifier that is unique within the node's graph.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Line<wbr>Number</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The line number of the node.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Node<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of node this is.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Args</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getscriptdagnodearg">[]Get<wbr>Script<wbr>Dag<wbr>Node<wbr>Arg</a></span>
    </dt>
    <dd>{{% md %}}Nested configuration an argument or property of a node. Defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A node identifier that is unique within the node's graph.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Line<wbr>Number</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The line number of the node.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Node<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of node this is.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>args</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getscriptdagnodearg">Get<wbr>Script<wbr>Dag<wbr>Node<wbr>Arg[]</a></span>
    </dt>
    <dd>{{% md %}}Nested configuration an argument or property of a node. Defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A node identifier that is unique within the node's graph.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>line<wbr>Number</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The line number of the node.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>node<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of node this is.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>args</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getscriptdagnodearg">List[Get<wbr>Script<wbr>Dag<wbr>Node<wbr>Arg]</a></span>
    </dt>
    <dd>{{% md %}}Nested configuration an argument or property of a node. Defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A node identifier that is unique within the node's graph.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>line<wbr>Number</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The line number of the node.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>node_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The type of node this is.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





#### Get&lt;wbr&gt;Script&lt;wbr&gt;Dag&lt;wbr&gt;Node&lt;wbr&gt;Arg
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#GetScriptDagNodeArg">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GetScriptDagNodeArg">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/glue?tab=doc#GetScriptDagNodeArgArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/glue?tab=doc#GetScriptDagNodeArg">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the argument or property.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Param</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Boolean if the value is used as a parameter. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The value of the argument or property.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the argument or property.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Param</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Boolean if the value is used as a parameter. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The value of the argument or property.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the argument or property.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>param</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Boolean if the value is used as a parameter. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The value of the argument or property.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the argument or property.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>param</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Boolean if the value is used as a parameter. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>value</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The value of the argument or property.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







