
---
title: "GremlinGraph"
block_external_search_index: true
---



Manages a Gremlin Graph within a Cosmos DB Account.

{{% examples %}}
{{% /examples %}}



## Create a GremlinGraph Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/cosmosdb/#GremlinGraph">GremlinGraph</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/cosmosdb/#GremlinGraphArgs">GremlinGraphArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">GremlinGraph</span><span class="p">(resource_name, opts=None, </span>account_name=None<span class="p">, </span>conflict_resolution_policies=None<span class="p">, </span>database_name=None<span class="p">, </span>index_policies=None<span class="p">, </span>name=None<span class="p">, </span>partition_key_path=None<span class="p">, </span>resource_group_name=None<span class="p">, </span>throughput=None<span class="p">, </span>unique_keys=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewGremlinGraph<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/cosmosdb?tab=doc#GremlinGraphArgs">GremlinGraphArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/cosmosdb?tab=doc#GremlinGraph">GremlinGraph</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.CosmosDB.GremlinGraph.html">GremlinGraph</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.CosmosDB.GremlinGraphArgs.html">GremlinGraphArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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

    <dt class="property-required"
            title="Required">
        <span>Account<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the CosmosDB Account to create the Gremlin Graph within. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Conflict<wbr>Resolution<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#gremlingraphconflictresolutionpolicy">List&lt;Gremlin<wbr>Graph<wbr>Conflict<wbr>Resolution<wbr>Policy<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}The conflict resolution policy for the graph. One or more `conflict_resolution_policy` blocks as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Database<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the Cosmos DB Graph Database in which the Cosmos DB Gremlin Graph is created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Index<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#gremlingraphindexpolicy">List&lt;Gremlin<wbr>Graph<wbr>Index<wbr>Policy<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}The configuration of the indexing policy. One or more `index_policy` blocks as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which the Cosmos DB Gremlin Graph is created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the name of the Cosmos DB Gremlin Graph. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Partition<wbr>Key<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Define a partition key. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Throughput</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The throughput of the Gremlin database (RU/s). Must be set in increments of `100`. The minimum value is `400`. This must be set upon database creation otherwise it cannot be updated without a manual resource destroy-apply.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Unique<wbr>Keys</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#gremlingraphuniquekey">List&lt;Gremlin<wbr>Graph<wbr>Unique<wbr>Key<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}One or more `unique_key` blocks as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Account<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the CosmosDB Account to create the Gremlin Graph within. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Conflict<wbr>Resolution<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#gremlingraphconflictresolutionpolicy">[]Gremlin<wbr>Graph<wbr>Conflict<wbr>Resolution<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}The conflict resolution policy for the graph. One or more `conflict_resolution_policy` blocks as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Database<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the Cosmos DB Graph Database in which the Cosmos DB Gremlin Graph is created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Index<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#gremlingraphindexpolicy">[]Gremlin<wbr>Graph<wbr>Index<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}The configuration of the indexing policy. One or more `index_policy` blocks as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which the Cosmos DB Gremlin Graph is created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the name of the Cosmos DB Gremlin Graph. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Partition<wbr>Key<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Define a partition key. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Throughput</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The throughput of the Gremlin database (RU/s). Must be set in increments of `100`. The minimum value is `400`. This must be set upon database creation otherwise it cannot be updated without a manual resource destroy-apply.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Unique<wbr>Keys</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#gremlingraphuniquekey">[]Gremlin<wbr>Graph<wbr>Unique<wbr>Key</a></span>
    </dt>
    <dd>{{% md %}}One or more `unique_key` blocks as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>account<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the CosmosDB Account to create the Gremlin Graph within. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>conflict<wbr>Resolution<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#gremlingraphconflictresolutionpolicy">Gremlin<wbr>Graph<wbr>Conflict<wbr>Resolution<wbr>Policy[]</a></span>
    </dt>
    <dd>{{% md %}}The conflict resolution policy for the graph. One or more `conflict_resolution_policy` blocks as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>database<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the Cosmos DB Graph Database in which the Cosmos DB Gremlin Graph is created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>index<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#gremlingraphindexpolicy">Gremlin<wbr>Graph<wbr>Index<wbr>Policy[]</a></span>
    </dt>
    <dd>{{% md %}}The configuration of the indexing policy. One or more `index_policy` blocks as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which the Cosmos DB Gremlin Graph is created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the name of the Cosmos DB Gremlin Graph. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>partition<wbr>Key<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Define a partition key. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>throughput</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The throughput of the Gremlin database (RU/s). Must be set in increments of `100`. The minimum value is `400`. This must be set upon database creation otherwise it cannot be updated without a manual resource destroy-apply.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>unique<wbr>Keys</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#gremlingraphuniquekey">Gremlin<wbr>Graph<wbr>Unique<wbr>Key[]</a></span>
    </dt>
    <dd>{{% md %}}One or more `unique_key` blocks as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>account_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The name of the CosmosDB Account to create the Gremlin Graph within. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>conflict_<wbr>resolution_<wbr>policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#gremlingraphconflictresolutionpolicy">List[Gremlin<wbr>Graph<wbr>Conflict<wbr>Resolution<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}The conflict resolution policy for the graph. One or more `conflict_resolution_policy` blocks as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>database_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The name of the Cosmos DB Graph Database in which the Cosmos DB Gremlin Graph is created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>index_<wbr>policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#gremlingraphindexpolicy">List[Gremlin<wbr>Graph<wbr>Index<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}The configuration of the indexing policy. One or more `index_policy` blocks as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>resource_<wbr>group_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which the Cosmos DB Gremlin Graph is created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Specifies the name of the Cosmos DB Gremlin Graph. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>partition_<wbr>key_<wbr>path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Define a partition key. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>throughput</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The throughput of the Gremlin database (RU/s). Must be set in increments of `100`. The minimum value is `400`. This must be set upon database creation otherwise it cannot be updated without a manual resource destroy-apply.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>unique_<wbr>keys</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#gremlingraphuniquekey">List[Gremlin<wbr>Graph<wbr>Unique<wbr>Key]</a></span>
    </dt>
    <dd>{{% md %}}One or more `unique_key` blocks as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Look up an Existing GremlinGraph Resource

Get an existing GremlinGraph resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/cosmosdb/#GremlinGraphState">GremlinGraphState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/cosmosdb/#GremlinGraph">GremlinGraph</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>account_name=None<span class="p">, </span>conflict_resolution_policies=None<span class="p">, </span>database_name=None<span class="p">, </span>index_policies=None<span class="p">, </span>name=None<span class="p">, </span>partition_key_path=None<span class="p">, </span>resource_group_name=None<span class="p">, </span>throughput=None<span class="p">, </span>unique_keys=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetGremlinGraph<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/cosmosdb?tab=doc#GremlinGraphState">GremlinGraphState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/cosmosdb?tab=doc#GremlinGraph">GremlinGraph</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.CosmosDB.GremlinGraph.html">GremlinGraph</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.CosmosDB.GremlinGraphState.html">GremlinGraphState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Account<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the CosmosDB Account to create the Gremlin Graph within. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Conflict<wbr>Resolution<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#gremlingraphconflictresolutionpolicy">List&lt;Gremlin<wbr>Graph<wbr>Conflict<wbr>Resolution<wbr>Policy<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}The conflict resolution policy for the graph. One or more `conflict_resolution_policy` blocks as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Database<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the Cosmos DB Graph Database in which the Cosmos DB Gremlin Graph is created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Index<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#gremlingraphindexpolicy">List&lt;Gremlin<wbr>Graph<wbr>Index<wbr>Policy<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}The configuration of the indexing policy. One or more `index_policy` blocks as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the name of the Cosmos DB Gremlin Graph. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Partition<wbr>Key<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Define a partition key. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which the Cosmos DB Gremlin Graph is created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Throughput</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The throughput of the Gremlin database (RU/s). Must be set in increments of `100`. The minimum value is `400`. This must be set upon database creation otherwise it cannot be updated without a manual resource destroy-apply.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Unique<wbr>Keys</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#gremlingraphuniquekey">List&lt;Gremlin<wbr>Graph<wbr>Unique<wbr>Key<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}One or more `unique_key` blocks as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Account<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the CosmosDB Account to create the Gremlin Graph within. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Conflict<wbr>Resolution<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#gremlingraphconflictresolutionpolicy">[]Gremlin<wbr>Graph<wbr>Conflict<wbr>Resolution<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}The conflict resolution policy for the graph. One or more `conflict_resolution_policy` blocks as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Database<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the Cosmos DB Graph Database in which the Cosmos DB Gremlin Graph is created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Index<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#gremlingraphindexpolicy">[]Gremlin<wbr>Graph<wbr>Index<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}The configuration of the indexing policy. One or more `index_policy` blocks as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the name of the Cosmos DB Gremlin Graph. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Partition<wbr>Key<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Define a partition key. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which the Cosmos DB Gremlin Graph is created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Throughput</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The throughput of the Gremlin database (RU/s). Must be set in increments of `100`. The minimum value is `400`. This must be set upon database creation otherwise it cannot be updated without a manual resource destroy-apply.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Unique<wbr>Keys</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#gremlingraphuniquekey">[]Gremlin<wbr>Graph<wbr>Unique<wbr>Key</a></span>
    </dt>
    <dd>{{% md %}}One or more `unique_key` blocks as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>account<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the CosmosDB Account to create the Gremlin Graph within. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>conflict<wbr>Resolution<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#gremlingraphconflictresolutionpolicy">Gremlin<wbr>Graph<wbr>Conflict<wbr>Resolution<wbr>Policy[]</a></span>
    </dt>
    <dd>{{% md %}}The conflict resolution policy for the graph. One or more `conflict_resolution_policy` blocks as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>database<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the Cosmos DB Graph Database in which the Cosmos DB Gremlin Graph is created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>index<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#gremlingraphindexpolicy">Gremlin<wbr>Graph<wbr>Index<wbr>Policy[]</a></span>
    </dt>
    <dd>{{% md %}}The configuration of the indexing policy. One or more `index_policy` blocks as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the name of the Cosmos DB Gremlin Graph. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>partition<wbr>Key<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Define a partition key. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which the Cosmos DB Gremlin Graph is created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>throughput</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The throughput of the Gremlin database (RU/s). Must be set in increments of `100`. The minimum value is `400`. This must be set upon database creation otherwise it cannot be updated without a manual resource destroy-apply.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>unique<wbr>Keys</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#gremlingraphuniquekey">Gremlin<wbr>Graph<wbr>Unique<wbr>Key[]</a></span>
    </dt>
    <dd>{{% md %}}One or more `unique_key` blocks as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>account_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The name of the CosmosDB Account to create the Gremlin Graph within. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>conflict_<wbr>resolution_<wbr>policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#gremlingraphconflictresolutionpolicy">List[Gremlin<wbr>Graph<wbr>Conflict<wbr>Resolution<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}The conflict resolution policy for the graph. One or more `conflict_resolution_policy` blocks as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>database_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The name of the Cosmos DB Graph Database in which the Cosmos DB Gremlin Graph is created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>index_<wbr>policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#gremlingraphindexpolicy">List[Gremlin<wbr>Graph<wbr>Index<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}The configuration of the indexing policy. One or more `index_policy` blocks as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Specifies the name of the Cosmos DB Gremlin Graph. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>partition_<wbr>key_<wbr>path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Define a partition key. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource_<wbr>group_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which the Cosmos DB Gremlin Graph is created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>throughput</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The throughput of the Gremlin database (RU/s). Must be set in increments of `100`. The minimum value is `400`. This must be set upon database creation otherwise it cannot be updated without a manual resource destroy-apply.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>unique_<wbr>keys</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#gremlingraphuniquekey">List[Gremlin<wbr>Graph<wbr>Unique<wbr>Key]</a></span>
    </dt>
    <dd>{{% md %}}One or more `unique_key` blocks as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Gremlin<wbr>Graph<wbr>Conflict<wbr>Resolution<wbr>Policy</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#GremlinGraphConflictResolutionPolicy">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#GremlinGraphConflictResolutionPolicy">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/cosmosdb?tab=doc#GremlinGraphConflictResolutionPolicyArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/cosmosdb?tab=doc#GremlinGraphConflictResolutionPolicyOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Indicates the conflict resolution mode. Possible values include: `LastWriterWins`, `Custom`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Conflict<wbr>Resolution<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The conflict resolution path in the case of LastWriterWins mode.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Conflict<wbr>Resolution<wbr>Procedure</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The procedure to resolve conflicts in the case of custom mode.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Indicates the conflict resolution mode. Possible values include: `LastWriterWins`, `Custom`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Conflict<wbr>Resolution<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The conflict resolution path in the case of LastWriterWins mode.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Conflict<wbr>Resolution<wbr>Procedure</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The procedure to resolve conflicts in the case of custom mode.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Indicates the conflict resolution mode. Possible values include: `LastWriterWins`, `Custom`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>conflict<wbr>Resolution<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The conflict resolution path in the case of LastWriterWins mode.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>conflict<wbr>Resolution<wbr>Procedure</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The procedure to resolve conflicts in the case of custom mode.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Indicates the conflict resolution mode. Possible values include: `LastWriterWins`, `Custom`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>conflict<wbr>Resolution<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The conflict resolution path in the case of LastWriterWins mode.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>conflict<wbr>Resolution<wbr>Procedure</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The procedure to resolve conflicts in the case of custom mode.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Gremlin<wbr>Graph<wbr>Index<wbr>Policy</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#GremlinGraphIndexPolicy">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#GremlinGraphIndexPolicy">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/cosmosdb?tab=doc#GremlinGraphIndexPolicyArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/cosmosdb?tab=doc#GremlinGraphIndexPolicyOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Indexing<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Indicates the indexing mode. Possible values include: `Consistent`, `Lazy`, `None`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Automatic</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Indicates if the indexing policy is automatic. Defaults to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Excluded<wbr>Paths</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}List of paths to exclude from indexing. Required if `indexing_mode` is `Consistent` or `Lazy`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Included<wbr>Paths</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}List of paths to include in the indexing. Required if `indexing_mode` is `Consistent` or `Lazy`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Indexing<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Indicates the indexing mode. Possible values include: `Consistent`, `Lazy`, `None`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Automatic</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Indicates if the indexing policy is automatic. Defaults to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Excluded<wbr>Paths</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}List of paths to exclude from indexing. Required if `indexing_mode` is `Consistent` or `Lazy`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Included<wbr>Paths</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}List of paths to include in the indexing. Required if `indexing_mode` is `Consistent` or `Lazy`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>indexing<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Indicates the indexing mode. Possible values include: `Consistent`, `Lazy`, `None`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>automatic</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Indicates if the indexing policy is automatic. Defaults to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>excluded<wbr>Paths</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}List of paths to exclude from indexing. Required if `indexing_mode` is `Consistent` or `Lazy`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>included<wbr>Paths</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}List of paths to include in the indexing. Required if `indexing_mode` is `Consistent` or `Lazy`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>indexing<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Indicates the indexing mode. Possible values include: `Consistent`, `Lazy`, `None`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>automatic</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Indicates if the indexing policy is automatic. Defaults to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>excluded<wbr>Paths</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}List of paths to exclude from indexing. Required if `indexing_mode` is `Consistent` or `Lazy`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>included<wbr>Paths</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}List of paths to include in the indexing. Required if `indexing_mode` is `Consistent` or `Lazy`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Gremlin<wbr>Graph<wbr>Unique<wbr>Key</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#GremlinGraphUniqueKey">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#GremlinGraphUniqueKey">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/cosmosdb?tab=doc#GremlinGraphUniqueKeyArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/cosmosdb?tab=doc#GremlinGraphUniqueKeyOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Paths</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}A list of paths to use for this unique key.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Paths</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}A list of paths to use for this unique key.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>paths</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}A list of paths to use for this unique key.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>paths</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}A list of paths to use for this unique key.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}









<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-azure">https://github.com/pulumi/pulumi-azure</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    <dt>Notes</dt>
	<dd>This Pulumi package is based on the [`azurerm` Terraform Provider](https://github.com/terraform-providers/terraform-provider-azurerm).</dd>
</dl>

