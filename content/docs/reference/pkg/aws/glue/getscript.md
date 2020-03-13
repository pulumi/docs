
---
title: "GetScript"
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>


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

{{< langchoose csharp nojavascript >}}


<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getScript<span class="p">(</span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/glue/#GetScriptArgs">GetScriptArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#InvokeOptions">pulumi.InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/glue/#GetScriptResult">GetScriptResult</a></span>></span></code></pre></div>


<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_script(</span>dag_edges=None<span class="p">, </span>dag_nodes=None<span class="p">, </span>language=None<span class="p">, </span>opts=None<span class="p">)</span></code></pre></div>


<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupScript<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/glue?tab=doc#GetScriptArgs">GetScriptArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#InvokeOption">pulumi.InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/glue?tab=doc#LookupScriptResult">LookupScriptResult</a></span>, error)</span></code></pre></div>


<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Glue.GetScriptResult.html">Pulumi.Aws.Glue.GetScriptResult</a></span>> <span class="p">GetScript(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Glue.GetScriptArgs.html">GetScriptArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/InvokeOptions.html">InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>



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
            <td class="align-top">Dag<wbr>Edges</td>
            <td class="align-top">
                
                <code><a href="#getscriptdagedge">List&lt;Pulumi.<wbr>Aws.<wbr>Glue.<wbr>Get<wbr>Script<wbr>Dag<wbr>Edge<wbr>Args&gt;</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A list of the edges in the DAG. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dag<wbr>Nodes</td>
            <td class="align-top">
                
                <code><a href="#getscriptdagnode">List&lt;Pulumi.<wbr>Aws.<wbr>Glue.<wbr>Get<wbr>Script<wbr>Dag<wbr>Node<wbr>Args&gt;</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A list of the nodes in the DAG. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Language</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The programming language of the resulting code from the DAG. Defaults to `PYTHON`. Valid values are `PYTHON` and `SCALA`.
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
            <td class="align-top">Dag<wbr>Edges</td>
            <td class="align-top">
                
                <code><a href="#getscriptdagedge">[]glue.<wbr>Get<wbr>Script<wbr>Dag<wbr>Edge</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A list of the edges in the DAG. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dag<wbr>Nodes</td>
            <td class="align-top">
                
                <code><a href="#getscriptdagnode">[]glue.<wbr>Get<wbr>Script<wbr>Dag<wbr>Node</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A list of the nodes in the DAG. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Language</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The programming language of the resulting code from the DAG. Defaults to `PYTHON`. Valid values are `PYTHON` and `SCALA`.
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
            <td class="align-top">dag<wbr>Edges</td>
            <td class="align-top">
                
                <code><a href="#getscriptdagedge">glue.<wbr>Get<wbr>Script<wbr>Dag<wbr>Edge[]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A list of the edges in the DAG. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dag<wbr>Nodes</td>
            <td class="align-top">
                
                <code><a href="#getscriptdagnode">glue.<wbr>Get<wbr>Script<wbr>Dag<wbr>Node[]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A list of the nodes in the DAG. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">language</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The programming language of the resulting code from the DAG. Defaults to `PYTHON`. Valid values are `PYTHON` and `SCALA`.
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
            <td class="align-top">dag_<wbr>edges</td>
            <td class="align-top">
                
                <code><a href="#getscriptdagedge">list[get_<wbr>script_<wbr>dag_<wbr>edge]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A list of the edges in the DAG. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dag_<wbr>nodes</td>
            <td class="align-top">
                
                <code><a href="#getscriptdagnode">list[get_<wbr>script_<wbr>dag_<wbr>node]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A list of the nodes in the DAG. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">language</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The programming language of the resulting code from the DAG. Defaults to `PYTHON`. Valid values are `PYTHON` and `SCALA`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## GetScript Result

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
            <td class="align-top">Dag<wbr>Edges</td>
            <td class="align-top">
                
                <code><a href="#getscriptdagedge">List&lt;Pulumi.<wbr>Aws.<wbr>Glue.<wbr>Get<wbr>Script<wbr>Dag<wbr>Edge&gt;</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dag<wbr>Nodes</td>
            <td class="align-top">
                
                <code><a href="#getscriptdagnode">List&lt;Pulumi.<wbr>Aws.<wbr>Glue.<wbr>Get<wbr>Script<wbr>Dag<wbr>Node&gt;</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
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
            <td class="align-top">Language</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Python<wbr>Script</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Python script generated from the DAG when the `language` argument is set to `PYTHON`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Scala<wbr>Code</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Scala code generated from the DAG when the `language` argument is set to `SCALA`.
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
            <td class="align-top">Dag<wbr>Edges</td>
            <td class="align-top">
                
                <code><a href="#getscriptdagedge">[]glue.<wbr>Get<wbr>Script<wbr>Dag<wbr>Edge</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dag<wbr>Nodes</td>
            <td class="align-top">
                
                <code><a href="#getscriptdagnode">[]glue.<wbr>Get<wbr>Script<wbr>Dag<wbr>Node</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
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
            <td class="align-top">Language</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Python<wbr>Script</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Python script generated from the DAG when the `language` argument is set to `PYTHON`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Scala<wbr>Code</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Scala code generated from the DAG when the `language` argument is set to `SCALA`.
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
            <td class="align-top">dag<wbr>Edges</td>
            <td class="align-top">
                
                <code><a href="#getscriptdagedge">glue.<wbr>Get<wbr>Script<wbr>Dag<wbr>Edge[]</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dag<wbr>Nodes</td>
            <td class="align-top">
                
                <code><a href="#getscriptdagnode">glue.<wbr>Get<wbr>Script<wbr>Dag<wbr>Node[]</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
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
            <td class="align-top">language</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">python<wbr>Script</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Python script generated from the DAG when the `language` argument is set to `PYTHON`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">scala<wbr>Code</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Scala code generated from the DAG when the `language` argument is set to `SCALA`.
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
            <td class="align-top">dag_<wbr>edges</td>
            <td class="align-top">
                
                <code><a href="#getscriptdagedge">list[get_<wbr>script_<wbr>dag_<wbr>edge]</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dag_<wbr>nodes</td>
            <td class="align-top">
                
                <code><a href="#getscriptdagnode">list[get_<wbr>script_<wbr>dag_<wbr>node]</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
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
            <td class="align-top">language</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">python_<wbr>script</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The Python script generated from the DAG when the `language` argument is set to `PYTHON`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">scala_<wbr>code</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The Scala code generated from the DAG when the `language` argument is set to `SCALA`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Supporting Types

#### GetScriptDagEdge
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#GetScriptDagEdge">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GetScriptDagEdge">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/glue?tab=doc#GetScriptDagEdgeArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/glue?tab=doc#GetScriptDagEdge">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Glue.GetScriptDagEdgeArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Glue.GetScriptDagEdge.html">output</a> API doc for this type.
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
            <td class="align-top">Source</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the node at which the edge starts.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Target</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the node at which the edge ends.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Target<wbr>Parameter</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The target of the edge.
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
            <td class="align-top">Source</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the node at which the edge starts.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Target</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the node at which the edge ends.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Target<wbr>Parameter</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The target of the edge.
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
            <td class="align-top">source</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the node at which the edge starts.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the node at which the edge ends.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target<wbr>Parameter</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The target of the edge.
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
            <td class="align-top">source</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the node at which the edge starts.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the node at which the edge ends.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target_<wbr>parameter</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The target of the edge.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### GetScriptDagNode
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#GetScriptDagNode">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GetScriptDagNode">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/glue?tab=doc#GetScriptDagNodeArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/glue?tab=doc#GetScriptDagNode">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Glue.GetScriptDagNodeArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Glue.GetScriptDagNode.html">output</a> API doc for this type.
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
            <td class="align-top">Args</td>
            <td class="align-top">
                
                <code><a href="#getscriptdagnodearg">List&lt;Pulumi.<wbr>Aws.<wbr>Glue.<wbr>Get<wbr>Script<wbr>Dag<wbr>Node<wbr>Arg<wbr>Args&gt;</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Nested configuration an argument or property of a node. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A node identifier that is unique within the node&#39;s graph.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Line<wbr>Number</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The line number of the node.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Node<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of node this is.
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
            <td class="align-top">Args</td>
            <td class="align-top">
                
                <code><a href="#getscriptdagnodearg">[]glue.<wbr>Get<wbr>Script<wbr>Dag<wbr>Node<wbr>Arg</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Nested configuration an argument or property of a node. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A node identifier that is unique within the node&#39;s graph.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Line<wbr>Number</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The line number of the node.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Node<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of node this is.
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
            <td class="align-top">args</td>
            <td class="align-top">
                
                <code><a href="#getscriptdagnodearg">glue.<wbr>Get<wbr>Script<wbr>Dag<wbr>Node<wbr>Arg[]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Nested configuration an argument or property of a node. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A node identifier that is unique within the node&#39;s graph.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">line<wbr>Number</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The line number of the node.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">node<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of node this is.
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
            <td class="align-top">args</td>
            <td class="align-top">
                
                <code><a href="#getscriptdagnodearg">list[get_<wbr>script_<wbr>dag_<wbr>node_<wbr>arg]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Nested configuration an argument or property of a node. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A node identifier that is unique within the node&#39;s graph.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">line_<wbr>number</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The line number of the node.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">node_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of node this is.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### GetScriptDagNodeArg
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#GetScriptDagNodeArg">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GetScriptDagNodeArg">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/glue?tab=doc#GetScriptDagNodeArgArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/glue?tab=doc#GetScriptDagNodeArg">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Glue.GetScriptDagNodeArgArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Glue.GetScriptDagNodeArg.html">output</a> API doc for this type.
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
The name of the argument or property.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Param</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean if the value is used as a parameter. Defaults to `false`.
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
The value of the argument or property.
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
The name of the argument or property.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Param</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean if the value is used as a parameter. Defaults to `false`.
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
The value of the argument or property.
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
The name of the argument or property.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">param</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean if the value is used as a parameter. Defaults to `false`.
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
The value of the argument or property.
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
The name of the argument or property.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">param</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean if the value is used as a parameter. Defaults to `false`.
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
The value of the argument or property.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







